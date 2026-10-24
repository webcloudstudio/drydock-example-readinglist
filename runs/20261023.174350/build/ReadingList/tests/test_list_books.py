"""List books: GET /books answers 200 with every stored book in the order it was added."""

from pathlib import Path

from flask.testing import FlaskClient

from app_server import create_app
from app_server.config import Config


def _add(client: FlaskClient, title: str) -> int:
    return client.post("/books", json={"title": title, "author": "A"}).get_json()["id"]


def test_get_on_empty_store_answers_200_with_empty_array(fresh_client: FlaskClient) -> None:
    response = fresh_client.get("/books")

    assert response.status_code == 200
    assert response.get_json() == []


def test_list_returns_titles_in_the_order_they_were_added(fresh_client: FlaskClient) -> None:
    titles = ["Ulysses", "Dune", "Emma"]
    for title in titles:
        _add(fresh_client, title)

    listed = fresh_client.get("/books").get_json()

    assert [book["title"] for book in listed] == titles


def test_list_returns_added_ids_in_submission_order(fresh_client: FlaskClient) -> None:
    created = [_add(fresh_client, f"Book {n}") for n in range(4)]

    listed_ids = [book["id"] for book in fresh_client.get("/books").get_json()]

    assert listed_ids == created


def test_each_listed_book_carries_id_title_and_author(fresh_client: FlaskClient) -> None:
    book_id = _add(fresh_client, "Dune")

    listed = fresh_client.get("/books").get_json()

    assert {"id": book_id, "title": "Dune", "author": "A"} in listed


def test_order_survives_reopening_the_store(fresh_client: FlaskClient, store_path: Path) -> None:
    created = [_add(fresh_client, f"Book {n}") for n in range(3)]

    reopened = create_app(Config(database_dsn=str(store_path))).test_client()
    listed_ids = [book["id"] for book in reopened.get("/books").get_json()]

    assert listed_ids == created
