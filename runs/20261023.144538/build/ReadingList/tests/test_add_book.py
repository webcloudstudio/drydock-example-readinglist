"""Add a book: POST /books stores a valid submission and redirects to the start page."""

import uuid
from pathlib import Path

import pytest

from app_server import create_app
from app_server.book_service import BookRejected, add_book
from persistence.testing import committed_session

PROJECT_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def app(monkeypatch, tmp_path):
    """A fresh application over its own store, so no test touches the configured data/app.db."""
    store = tmp_path / "add-book.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{store}")
    monkeypatch.delenv("DATABASE_PATH", raising=False)
    application = create_app()
    application.extensions["database"].execute_script((PROJECT_ROOT / "schema.sql").read_text())
    return application


def _stored(app) -> list[tuple[str, str]]:
    """Read every stored book back through the persistence package, in order added."""
    return [(row.title, row.author) for row in app.extensions["database"].books.list()]


def test_valid_submission_redirects_with_303_to_start_page(app):
    response = app.test_client().post("/books", data={"title": "Dune", "author": "Frank Herbert"})

    assert response.status_code == 303
    assert response.headers["Location"] == "/"


def test_valid_submission_stores_title_and_author(app):
    app.test_client().post("/books", data={"title": "Dune", "author": "Frank Herbert"})

    assert _stored(app) == [("Dune", "Frank Herbert")]


def test_surrounding_whitespace_is_trimmed_before_storing(app):
    app.test_client().post("/books", data={"title": "  Dune \t", "author": "\n Frank Herbert  "})

    assert _stored(app) == [("Dune", "Frank Herbert")]


def test_internal_whitespace_is_kept(app):
    app.test_client().post("/books", data={"title": "Dune  Messiah", "author": "Frank  Herbert"})

    assert _stored(app) == [("Dune  Messiah", "Frank  Herbert")]


def test_new_book_is_appended_after_existing_books(app):
    client = app.test_client()
    client.post("/books", data={"title": "First", "author": "A"})
    client.post("/books", data={"title": "Second", "author": "B"})
    client.post("/books", data={"title": "Third", "author": "C"})

    assert _stored(app) == [("First", "A"), ("Second", "B"), ("Third", "C")]


def test_same_book_submitted_twice_is_stored_twice(app):
    client = app.test_client()
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})

    assert _stored(app) == [("Dune", "Frank Herbert"), ("Dune", "Frank Herbert")]


@pytest.mark.parametrize(
    "form",
    [
        {"title": "", "author": "Frank Herbert"},
        {"title": "   ", "author": "Frank Herbert"},
        {"title": "Dune", "author": ""},
        {"title": "Dune", "author": " \t "},
        {"title": "", "author": ""},
        {"author": "Frank Herbert"},
        {"title": "Dune"},
        {},
    ],
    ids=[
        "empty-title",
        "blank-title",
        "empty-author",
        "blank-author",
        "both-empty",
        "title-absent",
        "author-absent",
        "both-absent",
    ],
)
def test_empty_or_absent_field_is_rejected_with_400_and_not_stored(app, form):
    response = app.test_client().post("/books", data=form)

    assert response.status_code == 400
    assert _stored(app) == []


def test_rejection_states_reason_in_alert_region(app):
    response = app.test_client().post("/books", data={"title": "", "author": "Frank Herbert"})

    assert b'role="alert"' in response.data
    assert b"rejected: title is empty" in response.data


def test_rejected_author_states_reason_in_alert_region(app):
    response = app.test_client().post("/books", data={"title": "Dune", "author": " "})

    assert b"rejected: author is empty" in response.data


def test_rejection_after_valid_submission_keeps_earlier_book(app):
    client = app.test_client()
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})
    client.post("/books", data={"title": "", "author": "Nobody"})

    assert _stored(app) == [("Dune", "Frank Herbert")]


def test_add_book_service_returns_stored_row(app):
    database = app.extensions["database"]

    row = add_book(database, title="Dune", author="Frank Herbert")

    assert (row.title, row.author) == ("Dune", "Frank Herbert")
    assert row.id is not None
    assert database.books.get(id=row.id) == row


def test_add_book_service_refuses_empty_title_with_reason(app):
    database = app.extensions["database"]

    with pytest.raises(BookRejected) as rejected:
        add_book(database, title="", author="Frank Herbert")

    assert rejected.value.reason == "rejected: title is empty"
    assert _stored(app) == []


def test_add_book_service_refuses_empty_author_with_reason(app):
    database = app.extensions["database"]

    with pytest.raises(BookRejected) as rejected:
        add_book(database, title="Dune", author="")

    assert rejected.value.reason == "rejected: author is empty"
    assert _stored(app) == []


# Round trip through the configured store: POST /books, then read the book back via GET /books.


def _unique(label: str) -> str:
    """Return a title no other test or run has used, so the shared store can hold it safely."""
    return f"AddTest-{label}-{uuid.uuid4().hex}"


@pytest.fixture
def added_titles():
    """Collect the titles a test adds, then remove exactly those books from the store afterwards."""
    titles: list[str] = []
    yield titles
    with committed_session() as database:
        for row in database.books.list():
            if row.title in titles:
                database.books.delete(id=row.id)


def _listed(client, title: str) -> list[dict]:
    """Return the listed books whose title is ``title``, read back through GET /books."""
    return [row for row in client.get("/books").get_json() if row["title"] == title]


def test_round_trip_add_answers_303_to_start_page(web_client, added_titles):
    title = _unique("redirect")
    added_titles.append(title)

    response = web_client.post("/books", data={"title": title, "author": "Test Author"})

    assert response.status_code == 303
    assert response.headers["Location"] == "/"


def test_added_book_is_listed_with_submitted_title_and_author(web_client, added_titles):
    title = _unique("roundtrip")
    author = "Round Trip Author"
    added_titles.append(title)

    web_client.post("/books", data={"title": title, "author": author})

    rows = _listed(web_client, title)
    assert len(rows) == 1
    assert rows[0]["title"] == title
    assert rows[0]["author"] == author
    assert isinstance(rows[0]["id"], int)


def test_added_book_is_stored_with_submitted_title_and_author(web_client, added_titles):
    title = _unique("stored")
    author = "Stored Author"
    added_titles.append(title)

    web_client.post("/books", data={"title": title, "author": author})

    with committed_session() as database:
        stored = [row for row in database.books.list() if row.title == title]
    assert len(stored) == 1
    assert stored[0].author == author


def test_round_trip_trims_surrounding_whitespace(web_client, added_titles):
    title = _unique("trimmed")
    added_titles.append(title)

    web_client.post("/books", data={"title": f"  {title}  ", "author": "  Trim Author  "})

    rows = _listed(web_client, title)
    assert len(rows) == 1
    assert rows[0]["author"] == "Trim Author"


def test_two_round_trip_adds_are_both_listed(web_client, added_titles):
    first = _unique("both-first")
    second = _unique("both-second")
    added_titles.extend([first, second])

    web_client.post("/books", data={"title": first, "author": "First Author"})
    web_client.post("/books", data={"title": second, "author": "Second Author"})

    listed_titles = [row["title"] for row in web_client.get("/books").get_json()]
    assert listed_titles.count(first) == 1
    assert listed_titles.count(second) == 1


def test_two_round_trip_adds_keep_the_order_they_were_added(web_client, added_titles):
    first = _unique("order-first")
    second = _unique("order-second")
    added_titles.extend([first, second])

    web_client.post("/books", data={"title": first, "author": "First Author"})
    web_client.post("/books", data={"title": second, "author": "Second Author"})

    ours = [
        row["title"]
        for row in web_client.get("/books").get_json()
        if row["title"] in (first, second)
    ]
    assert ours == [first, second]


def test_each_round_trip_book_keeps_its_own_author(web_client, added_titles):
    first = _unique("author-first")
    second = _unique("author-second")
    added_titles.extend([first, second])

    web_client.post("/books", data={"title": first, "author": "Author One"})
    web_client.post("/books", data={"title": second, "author": "Author Two"})

    assert _listed(web_client, first)[0]["author"] == "Author One"
    assert _listed(web_client, second)[0]["author"] == "Author Two"
