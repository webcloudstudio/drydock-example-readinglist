from types import SimpleNamespace

import pytest

from app_server import create_app
from app_server.books_service import list_books
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


def test_get_books_on_empty_store_returns_200_with_empty_array(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert response.get_json() == []


def test_get_books_returns_one_book_with_its_fields(client):
    added = client.post("/books", json={"title": "Dune", "author": "Frank Herbert"}).get_json()
    listing = client.get("/books").get_json()
    assert listing == [{"id": added["id"], "title": "Dune", "author": "Frank Herbert"}]


def test_get_books_lists_books_in_the_order_they_were_added(client):
    first = client.post("/books", json={"title": "A", "author": "One"}).get_json()
    second = client.post("/books", json={"title": "B", "author": "Two"}).get_json()
    third = client.post("/books", json={"title": "C", "author": "Three"}).get_json()
    listing = client.get("/books").get_json()
    assert [book["id"] for book in listing] == [first["id"], second["id"], third["id"]]
    assert [book["title"] for book in listing] == ["A", "B", "C"]


def test_get_books_reflects_books_added_after_an_earlier_read(client):
    client.post("/books", json={"title": "A", "author": "One"})
    assert len(client.get("/books").get_json()) == 1
    client.post("/books", json={"title": "B", "author": "Two"})
    assert [book["title"] for book in client.get("/books").get_json()] == ["A", "B"]


def test_get_books_does_not_include_rejected_submissions(client):
    client.post("/books", json={"title": "", "author": "Author"})
    client.post("/books", json={"title": "Kept", "author": "Author"})
    assert [book["title"] for book in client.get("/books").get_json()] == ["Kept"]


def test_list_books_returns_stored_books_as_book_rows(db):
    first = db.books.create(title="A", author="One")
    second = db.books.create(title="B", author="Two")
    assert list_books(db) == [
        Book(id=first, title="A", author="One"),
        Book(id=second, title="B", author="Two"),
    ]


def test_list_books_sorts_by_id_when_the_store_returns_rows_out_of_order():
    stored = [Book(id=3, title="C", author="x"), Book(id=1, title="A", author="x"), Book(id=2, title="B", author="x")]
    database = SimpleNamespace(books=SimpleNamespace(list=lambda: list(stored)))
    assert [book.id for book in list_books(database)] == [1, 2, 3]
