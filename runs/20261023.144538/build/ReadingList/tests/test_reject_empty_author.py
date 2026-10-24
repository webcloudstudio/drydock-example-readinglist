"""Reject empty author: a submission without an author answers 400 with a reason and stores nothing."""

from pathlib import Path

import pytest

from app_server import create_app
from app_server.book_service import BookRejected, add_book

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_ACCEPT = {"Accept": "application/json"}
BROWSER_ACCEPT = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}


@pytest.fixture
def app(monkeypatch, tmp_path):
    """A fresh application over its own store, so no test touches the configured data/app.db."""
    store = tmp_path / "reject-empty-author.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{store}")
    monkeypatch.delenv("DATABASE_PATH", raising=False)
    application = create_app()
    application.extensions["database"].execute_script((PROJECT_ROOT / "schema.sql").read_text())
    return application


def _stored(app) -> list[tuple[str, str]]:
    """Read every stored book back through the persistence package, in order added."""
    return [(row.title, row.author) for row in app.extensions["database"].books.list()]


@pytest.mark.parametrize(
    "form",
    [
        {"title": "Dune", "author": ""},
        {"title": "Dune", "author": "   "},
        {"title": "Dune", "author": " \t\n "},
        {"title": "Dune"},
    ],
    ids=["empty-author", "spaces-author", "whitespace-author", "author-absent"],
)
def test_json_rejection_answers_400(app, form):
    response = app.test_client().post("/books", data=form, headers=JSON_ACCEPT)

    assert response.status_code == 400


@pytest.mark.parametrize(
    "form",
    [
        {"title": "Dune", "author": ""},
        {"title": "Dune", "author": "   "},
        {"title": "Dune"},
    ],
    ids=["empty-author", "spaces-author", "author-absent"],
)
def test_json_rejection_body_has_non_empty_reason(app, form):
    response = app.test_client().post("/books", data=form, headers=JSON_ACCEPT)

    body = response.get_json()
    assert isinstance(body["error"], str)
    assert body["error"].strip()


@pytest.mark.parametrize(
    "form",
    [
        {"title": "Dune", "author": ""},
        {"title": "Dune", "author": "   "},
        {"title": "Dune"},
    ],
    ids=["empty-author", "spaces-author", "author-absent"],
)
def test_json_rejection_names_author_field(app, form):
    response = app.test_client().post("/books", data=form, headers=JSON_ACCEPT)

    assert response.get_json()["field"] == "author"


@pytest.mark.parametrize(
    "form",
    [
        {"title": "Dune", "author": ""},
        {"title": "Dune", "author": "   "},
        {"title": "Dune"},
    ],
    ids=["empty-author", "spaces-author", "author-absent"],
)
def test_json_rejection_stores_nothing(app, form):
    app.test_client().post("/books", data=form, headers=JSON_ACCEPT)

    assert _stored(app) == []


def test_whitespace_author_is_trimmed_then_rejected(app):
    response = app.test_client().post(
        "/books", data={"title": "Dune", "author": "\t  \n"}, headers=JSON_ACCEPT
    )

    assert response.status_code == 400
    assert response.get_json()["field"] == "author"
    assert _stored(app) == []


def test_empty_title_and_empty_author_names_title_first(app):
    response = app.test_client().post("/books", data={"title": "", "author": ""}, headers=JSON_ACCEPT)

    assert response.status_code == 400
    assert response.get_json()["field"] == "title"


def test_html_rejection_answers_400(app):
    response = app.test_client().post("/books", data={"title": "Dune", "author": ""})

    assert response.status_code == 400


def test_html_rejection_rerenders_page_with_author_reason_in_alert_region(app):
    response = app.test_client().post("/books", data={"title": "Dune", "author": ""})

    assert response.mimetype == "text/html"
    assert b'role="alert"' in response.data
    assert b"rejected: author is empty" in response.data


def test_html_rejection_for_absent_author_shows_reason(app):
    response = app.test_client().post("/books", data={"title": "Dune"})

    assert response.status_code == 400
    assert b"rejected: author is empty" in response.data


def test_html_rejection_stores_nothing(app):
    app.test_client().post("/books", data={"title": "Dune", "author": ""})

    assert _stored(app) == []


def test_browser_accept_header_gets_html_author_rejection(app):
    response = app.test_client().post(
        "/books", data={"title": "Dune", "author": ""}, headers=BROWSER_ACCEPT
    )

    assert response.status_code == 400
    assert response.mimetype == "text/html"
    assert b"rejected: author is empty" in response.data


def test_wildcard_accept_header_gets_html_author_rejection(app):
    response = app.test_client().post(
        "/books", data={"title": "Dune", "author": ""}, headers={"Accept": "*/*"}
    )

    assert response.mimetype == "text/html"


def test_rejection_leaves_earlier_books_untouched(app):
    client = app.test_client()
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})

    client.post("/books", data={"title": "Emma", "author": ""}, headers=JSON_ACCEPT)

    assert _stored(app) == [("Dune", "Frank Herbert")]


def test_add_book_service_refuses_empty_author_with_field_and_reason(app):
    database = app.extensions["database"]

    with pytest.raises(BookRejected) as rejected:
        add_book(database, title="Dune", author="")

    assert rejected.value.field == "author"
    assert rejected.value.reason.strip()
    assert _stored(app) == []
