from __future__ import annotations

from app_server import create_app
from persistence import open_database


def _client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _remove_titles(*titles: str) -> None:
    database = open_database("data/app.db")
    try:
        for book in database.books.list():
            if book.title in titles:
                database.books.delete(id=book.id)
    finally:
        database.close()


def test_screen_renders_empty_state_and_add_form(monkeypatch):
    from app_server.features.reading_list import routes

    monkeypatch.setattr(routes, "_read_books", lambda: [])
    client = _client()
    response = client.get("/")

    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert 'name="title"' in body
    assert 'name="author"' in body
    assert "Your reading list" in body
    assert "Your list is empty" in body


def test_screen_rejects_blank_fields_without_creating_a_book():
    title = "   "
    author = "   "
    client = _client()

    response = client.post("/books", data={"title": title, "author": author})

    assert response.status_code == 400
    body = response.get_data(as_text=True)
    assert 'aria-invalid="true"' in body
    assert "Title is required." in body
    assert "Author is required." in body
    database = open_database("data/app.db")
    try:
        assert all(book.title != title and book.author != author for book in database.books.list())
    finally:
        database.close()


def test_screen_lists_books_in_insertion_order_and_exposes_each_removal_control():
    titles = ("Screen Order First", "Screen Order Second")
    try:
        client = _client()
        assert client.post("/books", data={"title": titles[0], "author": "First Author"}).status_code == 302
        assert client.post("/books", data={"title": titles[1], "author": "Second Author"}).status_code == 302

        body = client.get("/").get_data(as_text=True)
        assert body.index(titles[0]) < body.index(titles[1])
        assert 'aria-label="Remove Screen Order First"' in body
        assert 'aria-label="Remove Screen Order Second"' in body
    finally:
        _remove_titles(*titles)


def test_screen_removal_redirects_to_list_without_removed_book():
    title = "Screen Removal Control"
    try:
        client = _client()
        assert client.post("/books", data={"title": title, "author": "Removal Author"}).status_code == 302
        database = open_database("data/app.db")
        try:
            book_id = next(book.id for book in database.books.list() if book.title == title)
        finally:
            database.close()

        removed = client.post(f"/books/{book_id}/delete")

        assert removed.status_code == 302
        assert title not in client.get("/").get_data(as_text=True)
    finally:
        _remove_titles(title)
