"""Add book: POST /books answers 201 with the stored book, and the stored row reads back."""

from flask.testing import FlaskClient

from persistence import Database


def test_post_answers_201_with_stored_book_fields(fresh_client: FlaskClient) -> None:
    response = fresh_client.post("/books", json={"title": "Dune", "author": "Frank Herbert"})

    assert response.status_code == 201
    body = response.get_json()
    assert isinstance(body["id"], int)
    assert body["title"] == "Dune"
    assert body["author"] == "Frank Herbert"


def test_post_response_body_carries_exactly_id_title_and_author(fresh_client: FlaskClient) -> None:
    response = fresh_client.post("/books", json={"title": "Dune", "author": "Frank Herbert"})

    assert set(response.get_json()) == {"id", "title", "author"}


def test_posted_book_reads_back_from_store(fresh_client: FlaskClient, fresh_db: Database) -> None:
    body = fresh_client.post("/books", json={"title": "Dune", "author": "Frank Herbert"}).get_json()

    row = fresh_db.books.get(id=body["id"])

    assert row is not None
    assert (row.id, row.title, row.author) == (body["id"], "Dune", "Frank Herbert")


def test_stored_title_and_author_keep_the_supplied_whitespace(fresh_client: FlaskClient) -> None:
    response = fresh_client.post("/books", json={"title": "  Dune  ", "author": " Frank Herbert "})

    body = response.get_json()
    assert body["title"] == "  Dune  "
    assert body["author"] == " Frank Herbert "


def test_two_books_added_in_sequence_receive_ascending_ids(fresh_client: FlaskClient) -> None:
    first = fresh_client.post("/books", json={"title": "One", "author": "A"}).get_json()
    second = fresh_client.post("/books", json={"title": "Two", "author": "A"}).get_json()

    assert first["id"] < second["id"]
