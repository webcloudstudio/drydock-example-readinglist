from __future__ import annotations

from html.parser import HTMLParser

from flask import Flask

from app import create_app


class _BookListParser(HTMLParser):
    """Extract rendered book records from the public list page."""

    def __init__(self) -> None:
        super().__init__()
        self.books: list[tuple[str, str]] = []
        self._in_book = False
        self._in_title = False
        self._title_parts: list[str] = []
        self._status = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        if tag == "li" and "book-card" in classes:
            self._in_book = True
            self._title_parts = []
            self._status = ""
        elif self._in_book and tag == "h3":
            self._in_title = True
        elif self._in_book and tag == "span" and attributes.get("data-status"):
            self._status = attributes["data-status"] or ""

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h3":
            self._in_title = False
        elif tag == "li" and self._in_book:
            self.books.append(("".join(self._title_parts).strip(), self._status))
            self._in_book = False


def _books_from(response_body: str) -> list[tuple[str, str]]:
    parser = _BookListParser()
    parser.feed(response_body)
    return parser.books


def _fresh_app() -> Flask:
    return create_app({"TESTING": True, "DATABASE": ":memory:"})


def test_public_list_is_empty_before_any_book_is_added() -> None:
    app = _fresh_app()

    response = app.test_client().get("/")

    assert response.status_code == 200
    assert _books_from(response.get_data(as_text=True)) == []


def test_public_add_route_persists_a_book_and_displays_it() -> None:
    app = _fresh_app()
    client = app.test_client()

    add_response = client.post(
        "/books", data={"title": "Coverage Book", "author": "Coverage Author"}
    )

    assert add_response.status_code in (200, 302, 303)
    assert _books_from(client.get("/").get_data(as_text=True)) == [
        ("Coverage Book by Coverage Author", "unread")
    ]


def test_public_list_preserves_addition_order() -> None:
    app = _fresh_app()
    client = app.test_client()
    for title, author in (("First", "Author One"), ("Second", "Author Two")):
        response = client.post("/books", data={"title": title, "author": author})
        assert response.status_code in (200, 302, 303)

    assert _books_from(client.get("/").get_data(as_text=True)) == [
        ("First by Author One", "unread"),
        ("Second by Author Two", "unread"),
    ]


def test_public_add_route_rejects_empty_title_and_author_without_persisting() -> None:
    app = _fresh_app()
    client = app.test_client()

    for data in (
        {"title": "", "author": "Known Author"},
        {"title": "Known Title", "author": "   "},
    ):
        response = client.post("/books", data=data)
        assert response.status_code == 400

    assert _books_from(client.get("/").get_data(as_text=True)) == []


def test_public_read_route_persists_and_displays_read_status() -> None:
    app = _fresh_app()
    client = app.test_client()
    client.post("/books", data={"title": "Finished", "author": "Reader"})
    book_id = app.extensions["reading_list_database"].list_books()[0].id

    read_response = client.post(f"/books/{book_id}/read")

    assert read_response.status_code in (200, 302, 303)
    assert _books_from(client.get("/").get_data(as_text=True)) == [
        ("Finished by Reader", "read")
    ]


def test_public_delete_route_removes_only_the_selected_book() -> None:
    app = _fresh_app()
    client = app.test_client()
    client.post("/books", data={"title": "Remove Me", "author": "Author A"})
    client.post("/books", data={"title": "Keep Me", "author": "Author B"})
    first_id = app.extensions["reading_list_database"].list_books()[0].id

    delete_response = client.post(f"/books/{first_id}/delete")

    assert delete_response.status_code in (200, 302, 303)
    assert _books_from(client.get("/").get_data(as_text=True)) == [
        ("Keep Me by Author B", "unread")
    ]
