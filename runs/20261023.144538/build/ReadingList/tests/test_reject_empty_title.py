"""Reject empty title: a submission without a title answers 400 with a reason and stores nothing."""

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
    store = tmp_path / "reject-empty-title.db"
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
        {"title": "", "author": "Frank Herbert"},
        {"title": "   ", "author": "Frank Herbert"},
        {"author": "Frank Herbert"},
        {"title": "", "author": ""},
    ],
    ids=["empty-title", "whitespace-title", "title-absent", "both-empty"],
)
def test_json_rejection_answers_400(app, form):
    response = app.test_client().post("/books", data=form, headers=JSON_ACCEPT)

    assert response.status_code == 400


def test_json_rejection_body_has_non_empty_reason(app):
    response = app.test_client().post(
        "/books", data={"title": "", "author": "Frank Herbert"}, headers=JSON_ACCEPT
    )

    body = response.get_json()
    assert isinstance(body["error"], str)
    assert body["error"].strip()


@pytest.mark.parametrize(
    "form",
    [
        {"title": "", "author": "Frank Herbert"},
        {"title": "  \t ", "author": "Frank Herbert"},
        {"author": "Frank Herbert"},
        {"title": "", "author": ""},
    ],
    ids=["empty-title", "whitespace-title", "title-absent", "both-empty"],
)
def test_json_rejection_names_title_field(app, form):
    response = app.test_client().post("/books", data=form, headers=JSON_ACCEPT)

    assert response.get_json()["field"] == "title"


def test_json_rejection_stores_nothing(app):
    app.test_client().post(
        "/books", data={"title": "", "author": "Frank Herbert"}, headers=JSON_ACCEPT
    )

    assert _stored(app) == []


def test_json_author_rejection_names_author_field(app):
    response = app.test_client().post(
        "/books", data={"title": "Dune", "author": ""}, headers=JSON_ACCEPT
    )

    assert response.status_code == 400
    assert response.get_json()["field"] == "author"


def test_html_rejection_answers_400(app):
    response = app.test_client().post("/books", data={"title": "", "author": "Frank Herbert"})

    assert response.status_code == 400


def test_html_rejection_rerenders_page_with_reason_in_alert_region(app):
    response = app.test_client().post("/books", data={"title": "", "author": "Frank Herbert"})

    assert response.mimetype == "text/html"
    assert b'role="alert"' in response.data
    assert b"rejected: title is empty" in response.data


def test_html_rejection_for_missing_title_shows_reason(app):
    response = app.test_client().post("/books", data={"author": "Frank Herbert"})

    assert response.status_code == 400
    assert b"rejected: title is empty" in response.data


def test_html_rejection_stores_nothing(app):
    app.test_client().post("/books", data={"title": "", "author": "Frank Herbert"})

    assert _stored(app) == []


def test_browser_accept_header_gets_html_rejection(app):
    response = app.test_client().post(
        "/books", data={"title": "", "author": "Frank Herbert"}, headers=BROWSER_ACCEPT
    )

    assert response.status_code == 400
    assert response.mimetype == "text/html"
    assert b"rejected: title is empty" in response.data


def test_wildcard_accept_header_gets_html_rejection(app):
    response = app.test_client().post(
        "/books", data={"title": "", "author": "Frank Herbert"}, headers={"Accept": "*/*"}
    )

    assert response.mimetype == "text/html"


def test_rejection_leaves_earlier_books_untouched(app):
    client = app.test_client()
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})

    client.post("/books", data={"title": "", "author": "Nobody"}, headers=JSON_ACCEPT)

    assert _stored(app) == [("Dune", "Frank Herbert")]


def test_add_book_service_refusal_names_title_field(app):
    database = app.extensions["database"]

    with pytest.raises(BookRejected) as rejected:
        add_book(database, title="", author="Frank Herbert")

    assert rejected.value.field == "title"
    assert rejected.value.reason.strip()
    assert _stored(app) == []
