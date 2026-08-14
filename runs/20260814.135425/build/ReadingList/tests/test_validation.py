from __future__ import annotations

from html.parser import HTMLParser

from app import create_app
from app.database import Database


class _FormAndAlertParser(HTMLParser):
    """Read the validation response through its rendered HTML structure."""

    def __init__(self) -> None:
        super().__init__()
        self.input_values: dict[str, str] = {}
        self.alert_seen = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "input" and attributes.get("name") in {"title", "author"}:
            self.input_values[attributes["name"]] = attributes.get("value", "") or ""
        if tag == "p" and attributes.get("role") == "alert":
            self.alert_seen = True


def test_books_route_rejects_empty_title_with_bad_request(tmp_path):
    path = str(tmp_path / "empty-title.sqlite")
    app = create_app({"TESTING": True, "READING_LIST_DATABASE": path})

    response = app.test_client().post(
        "/books", data={"title": "", "author": "Known Author"}
    )

    assert response.status_code == 400
    assert Database(path).list_books() == []


def test_books_route_rejects_empty_author_with_bad_request(tmp_path):
    path = str(tmp_path / "empty-author.sqlite")
    app = create_app({"TESTING": True, "READING_LIST_DATABASE": path})

    response = app.test_client().post(
        "/books", data={"title": "Known Title", "author": ""}
    )

    assert response.status_code == 400
    assert Database(path).list_books() == []


def test_books_route_rejects_whitespace_only_fields_without_persistence(tmp_path):
    path = str(tmp_path / "whitespace.sqlite")
    app = create_app({"TESTING": True, "READING_LIST_DATABASE": path})

    response = app.test_client().post(
        "/books", data={"title": "   ", "author": "   "}
    )

    assert response.status_code == 400
    assert Database(path).list_books() == []


def test_validation_response_preserves_form_context_and_exposes_error(tmp_path):
    app = create_app(
        {"TESTING": True, "READING_LIST_DATABASE": str(tmp_path / "context.sqlite")}
    )

    response = app.test_client().post(
        "/books", data={"title": "  Keep this  ", "author": "   "}
    )
    parser = _FormAndAlertParser()
    parser.feed(response.get_data(as_text=True))

    assert response.status_code == 400
    assert parser.input_values == {"title": "  Keep this  ", "author": "   "}
    assert parser.alert_seen is True
