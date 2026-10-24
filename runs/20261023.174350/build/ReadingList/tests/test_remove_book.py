"""Remove book: DELETE /books/{id} answers 204 for a stored book and 404 for anything else."""

from pathlib import Path

from flask.testing import FlaskClient

from app_server import create_app
from app_server.config import Config


def _add(client: FlaskClient, title: str) -> int:
    return client.post("/books", json={"title": title, "author": "A"}).get_json()["id"]


def _listed_ids(client: FlaskClient) -> list[int]:
    return [book["id"] for book in client.get("/books").get_json()]


def test_delete_answers_204_with_empty_body(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")

    response = fresh_client.delete(f"/books/{book_id}")

    assert response.status_code == 204
    assert response.data == b""


def test_removed_book_is_absent_from_next_list_read(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")
    assert book_id in _listed_ids(fresh_client)

    fresh_client.delete(f"/books/{book_id}")

    assert book_id not in _listed_ids(fresh_client)


def test_removed_book_stays_absent_after_reopening_the_store(
    fresh_client: FlaskClient, store_path: Path
) -> None:
    book_id = _add(fresh_client, "Dune")
    fresh_client.delete(f"/books/{book_id}")

    reopened = create_app(Config(database_dsn=str(store_path))).test_client()

    assert book_id not in _listed_ids(reopened)


def test_remaining_books_keep_their_order_after_a_middle_removal(fresh_client: FlaskClient) -> None:
    first, middle, last = (_add(fresh_client, f"Book {n}") for n in range(3))

    fresh_client.delete(f"/books/{middle}")

    assert _listed_ids(fresh_client) == [first, last]


def test_removing_an_unknown_id_answers_404_with_error_body(fresh_client: FlaskClient) -> None:
    response = fresh_client.delete("/books/999999")

    assert response.status_code == 404
    assert isinstance(response.get_json()["error"], str)


def test_removing_the_same_id_twice_answers_404_the_second_time(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")

    first = fresh_client.delete(f"/books/{book_id}")
    second = fresh_client.delete(f"/books/{book_id}")

    assert first.status_code == 204
    assert second.status_code == 404


def test_unknown_removal_leaves_the_list_unchanged(fresh_client: FlaskClient) -> None:
    created = [_add(fresh_client, f"Book {n}") for n in range(2)]

    fresh_client.delete("/books/999999")

    assert _listed_ids(fresh_client) == created


def test_non_integer_id_does_not_match_the_route(fresh_client: FlaskClient) -> None:
    response = fresh_client.delete("/books/not-a-number")

    assert response.status_code == 404
