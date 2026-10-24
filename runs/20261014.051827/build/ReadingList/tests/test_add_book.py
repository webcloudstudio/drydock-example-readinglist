import pytest

from app_server import create_app
from app_server.books_service import InvalidBook, add_book
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


def test_post_valid_book_returns_201_with_stored_fields(client):
    response = client.post("/books", json={"title": "Dune", "author": "Frank Herbert"})
    assert response.status_code == 201
    body = response.get_json()
    assert isinstance(body["id"], int)
    assert body["title"] == "Dune"
    assert body["author"] == "Frank Herbert"


def test_post_valid_book_is_readable_from_store(client, db):
    body = client.post("/books", json={"title": "Dune", "author": "Frank Herbert"}).get_json()
    assert db.books.get(id=body["id"]) == Book(id=body["id"], title="Dune", author="Frank Herbert")


def test_post_valid_book_is_listed_in_order_added(client, db):
    first = client.post("/books", json={"title": "A", "author": "One"}).get_json()
    second = client.post("/books", json={"title": "B", "author": "Two"}).get_json()
    assert [book.id for book in db.books.list()] == [first["id"], second["id"]]


def test_post_valid_books_receive_distinct_ids(client):
    first = client.post("/books", json={"title": "A", "author": "One"}).get_json()
    second = client.post("/books", json={"title": "B", "author": "Two"}).get_json()
    assert first["id"] != second["id"]


def test_post_trims_surrounding_whitespace_before_storing(client, db):
    body = client.post("/books", json={"title": "  Dune  ", "author": " Frank Herbert "}).get_json()
    assert body["title"] == "Dune"
    assert body["author"] == "Frank Herbert"
    assert db.books.get(id=body["id"]) == Book(id=body["id"], title="Dune", author="Frank Herbert")


@pytest.mark.parametrize("title", ["", "   ", "\t\n"])
def test_post_empty_title_returns_400_naming_title(client, title):
    response = client.post("/books", json={"title": title, "author": "Author"})
    assert response.status_code == 400
    assert response.get_json() == {"field": "title"}


@pytest.mark.parametrize("author", ["", "   ", "\t\n"])
def test_post_empty_author_returns_400_naming_author(client, author):
    response = client.post("/books", json={"title": "Title", "author": author})
    assert response.status_code == 400
    assert response.get_json() == {"field": "author"}


def test_post_missing_title_returns_400_naming_title(client):
    response = client.post("/books", json={"author": "Author"})
    assert response.status_code == 400
    assert response.get_json() == {"field": "title"}


def test_post_missing_author_returns_400_naming_author(client):
    response = client.post("/books", json={"title": "Title"})
    assert response.status_code == 400
    assert response.get_json() == {"field": "author"}


def test_post_non_string_title_returns_400_naming_title(client):
    response = client.post("/books", json={"title": 42, "author": "Author"})
    assert response.status_code == 400
    assert response.get_json() == {"field": "title"}


def test_post_without_json_body_returns_400_naming_title(client):
    response = client.post("/books", data="not json", content_type="text/plain")
    assert response.status_code == 400
    assert response.get_json() == {"field": "title"}


def test_post_json_array_body_returns_400_naming_title(client):
    response = client.post("/books", json=["Dune", "Frank Herbert"])
    assert response.status_code == 400
    assert response.get_json() == {"field": "title"}


def test_rejected_submission_is_not_stored(client, db):
    client.post("/books", json={"title": "", "author": "Author"})
    client.post("/books", json={"title": "Title", "author": " "})
    assert db.books.list() == []


def test_service_stores_and_returns_book_with_assigned_id(app):
    db = app.extensions[DATABASE_EXTENSION]
    book = add_book(db, "Dune", "Frank Herbert")
    assert book.title == "Dune"
    assert book.author == "Frank Herbert"
    assert db.books.get(id=book.id) == book


@pytest.mark.parametrize(
    ("title", "author", "field"),
    [("", "Author", "title"), ("Title", "", "author"), (None, "Author", "title"), ("Title", None, "author")],
)
def test_service_rejects_empty_or_missing_field_with_its_name(app, title, author, field):
    db = app.extensions[DATABASE_EXTENSION]
    with pytest.raises(InvalidBook) as raised:
        add_book(db, title, author)
    assert raised.value.field == field
    assert db.books.list() == []
