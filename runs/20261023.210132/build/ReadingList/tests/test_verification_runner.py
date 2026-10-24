from __future__ import annotations

from app_server.testing import web_client
from persistence import open_database


def _delete_titles(*titles: str) -> None:
    database = open_database("data/app.db")
    try:
        for book in database.books.list():
            if book.title in titles:
                database.books.delete(id=book.id)
    finally:
        database.close()


def test_runner_workflow_adds_and_reads_a_book() -> None:
    title = "Verification Added Book"
    try:
        client = web_client()

        response = client.post("/books", data={"title": title, "author": "A Reader"})

        assert response.status_code == 302
        page = client.get("/")
        assert page.status_code == 200
        assert title in page.get_data(as_text=True)
    finally:
        _delete_titles(title)


def test_runner_workflow_preserves_insertion_order() -> None:
    titles = ("Verification First Book", "Verification Second Book")
    try:
        client = web_client()
        for title in titles:
            assert client.post("/books", data={"title": title, "author": "A Reader"}).status_code == 302

        body = client.get("/").get_data(as_text=True)

        assert body.index(titles[0]) < body.index(titles[1])
    finally:
        _delete_titles(*titles)


def test_runner_workflow_removes_a_selected_book() -> None:
    title = "Verification Removed Book"
    try:
        client = web_client()
        assert client.post("/books", data={"title": title, "author": "A Reader"}).status_code == 302
        database = open_database("data/app.db")
        try:
            book_id = next(book.id for book in database.books.list() if book.title == title)
        finally:
            database.close()

        response = client.post(f"/books/{book_id}/delete")

        assert response.status_code == 302
        assert title not in client.get("/").get_data(as_text=True)
    finally:
        _delete_titles(title)


def test_runner_workflow_rejects_an_empty_title() -> None:
    client = web_client()

    response = client.post("/books", data={"title": "  ", "author": "A Reader"})

    assert response.status_code == 400
    assert 'name="title"' in response.get_data(as_text=True)


def test_runner_workflow_rejects_an_empty_author() -> None:
    client = web_client()

    response = client.post("/books", data={"title": "A Book", "author": "  "})

    assert response.status_code == 400
    assert 'name="author"' in response.get_data(as_text=True)
