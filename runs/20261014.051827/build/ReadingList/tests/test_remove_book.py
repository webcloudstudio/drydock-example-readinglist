import pytest

from app_server import create_app
from app_server.books_service import remove_book
from app_server.settings import DATABASE_EXTENSION
from persistence.schema import Book


@pytest.fixture
def app():
    application = create_app()
    application.config["TESTING"] = True
    yield application
    application.extensions[DATABASE_EXTENSION].close()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    return app.extensions[DATABASE_EXTENSION]


def _add(client, title, author="Author"):
    return client.post("/books", json={"title": title, "author": author}).get_json()["id"]


def test_delete_stored_book_returns_204_with_empty_body(client):
    book_id = _add(client, "Dune")
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 204
    assert response.data == b""


def test_deleted_book_is_absent_from_next_list(client):
    book_id = _add(client, "Dune")
    client.delete(f"/books/{book_id}")
    assert client.get("/books").get_json() == []


def test_delete_removes_only_the_named_book_and_keeps_order(client):
    first = _add(client, "A")
    middle = _add(client, "B")
    last = _add(client, "C")
    client.delete(f"/books/{middle}")
    listing = client.get("/books").get_json()
    assert [book["id"] for book in listing] == [first, last]


def test_delete_removes_book_from_store(client, db):
    book_id = _add(client, "Dune")
    client.delete(f"/books/{book_id}")
    assert db.books.get(id=book_id) is None


def test_delete_missing_id_returns_404_naming_the_id(client):
    response = client.delete("/books/999")
    assert response.status_code == 404
    assert response.get_json() == {"id": 999}


def test_delete_missing_id_leaves_list_unchanged(client):
    first = _add(client, "A")
    _add(client, "B")
    before = client.get("/books").get_json()
    assert client.delete("/books/999").status_code == 404
    assert client.get("/books").get_json() == before
    assert before[0]["id"] == first


def test_delete_same_id_twice_returns_404_the_second_time(client):
    book_id = _add(client, "Dune")
    assert client.delete(f"/books/{book_id}").status_code == 204
    assert client.delete(f"/books/{book_id}").status_code == 404


def test_delete_already_removed_id_leaves_remaining_books_unchanged(client):
    keep = _add(client, "Keep")
    gone = _add(client, "Gone")
    client.delete(f"/books/{gone}")
    before = client.get("/books").get_json()
    assert client.delete(f"/books/{gone}").status_code == 404
    assert client.get("/books").get_json() == before
    assert [book["id"] for book in before] == [keep]


def test_delete_on_empty_store_returns_404(client):
    assert client.delete("/books/1").status_code == 404


def test_delete_non_integer_id_returns_404(client):
    _add(client, "Dune")
    assert client.delete("/books/not-a-number").status_code == 404
    assert len(client.get("/books").get_json()) == 1


def test_delete_does_not_remove_a_book_when_id_only_differs_by_path_suffix(client):
    book_id = _add(client, "Dune")
    assert client.delete(f"/books/{book_id}/extra").status_code == 404
    assert len(client.get("/books").get_json()) == 1


def test_remove_book_returns_true_and_deletes_stored_book(db):
    book_id = db.books.create(title="Dune", author="Frank Herbert")
    assert remove_book(db, book_id) is True
    assert db.books.get(id=book_id) is None


def test_remove_book_returns_false_and_changes_nothing_for_missing_id(db):
    kept = db.books.create(title="Kept", author="Author")
    assert remove_book(db, 999) is False
    assert db.books.get(id=kept) == Book(id=kept, title="Kept", author="Author")
    assert len(db.books.list()) == 1
