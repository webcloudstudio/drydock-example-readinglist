"""List books: GET /books returns stored books as JSON, in the order they were added."""

from pathlib import Path

import pytest

from app_server.book_service import list_books
from persistence import open_database

PROJECT_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(autouse=True)
def store(monkeypatch, tmp_path):
    """Point the application at a fresh store per test, so listing starts from a known state."""
    url = f"sqlite:///{tmp_path / 'list-books.db'}"
    monkeypatch.setenv("DATABASE_URL", url)
    monkeypatch.delenv("DATABASE_PATH", raising=False)
    with open_database(url) as database:
        database.execute_script((PROJECT_ROOT / "schema.sql").read_text())
    return url


def _add(client, title: str, author: str = "List Author") -> None:
    assert client.post("/books", data={"title": title, "author": author}).status_code == 303


def test_get_books_answers_200_with_json(web_client):
    response = web_client.get("/books")

    assert response.status_code == 200
    assert response.is_json


def test_empty_store_lists_empty_array(web_client):
    assert web_client.get("/books").get_json() == []


def test_single_book_is_listed_with_id_title_and_author(web_client):
    _add(web_client, "Dune", "Frank Herbert")

    body = web_client.get("/books").get_json()

    assert len(body) == 1
    assert body[0]["title"] == "Dune"
    assert body[0]["author"] == "Frank Herbert"
    assert isinstance(body[0]["id"], int)


def test_listed_book_carries_exactly_id_title_and_author(web_client):
    _add(web_client, "Dune", "Frank Herbert")

    body = web_client.get("/books").get_json()

    assert set(body[0].keys()) == {"id", "title", "author"}


def test_several_books_are_listed_in_the_order_added(web_client):
    for title in ["Third-added-last", "A-first", "M-second"]:
        _add(web_client, title)

    body = web_client.get("/books").get_json()

    assert [row["title"] for row in body] == ["Third-added-last", "A-first", "M-second"]


def test_listed_ids_ascend_across_the_sequence(web_client):
    for title in ["One", "Two", "Three", "Four"]:
        _add(web_client, title)

    ids = [row["id"] for row in web_client.get("/books").get_json()]

    assert ids == sorted(ids)
    assert len(set(ids)) == len(ids)


def test_book_added_after_a_listing_appears_at_the_end(web_client):
    _add(web_client, "First")
    web_client.get("/books")
    _add(web_client, "Second")

    body = web_client.get("/books").get_json()

    assert [row["title"] for row in body] == ["First", "Second"]


def test_repeated_listing_returns_the_same_sequence(web_client):
    for title in ["Alpha", "Beta"]:
        _add(web_client, title)

    first = web_client.get("/books").get_json()
    second = web_client.get("/books").get_json()

    assert first == second


def test_rejected_submission_is_not_listed(web_client):
    _add(web_client, "Kept")
    assert web_client.post("/books", data={"title": "", "author": "Nobody"}).status_code == 400

    body = web_client.get("/books").get_json()

    assert [row["title"] for row in body] == ["Kept"]


def test_listing_matches_the_persistence_store_order(web_client, store):
    for title in ["Store-one", "Store-two", "Store-three"]:
        _add(web_client, title)

    http_ids = [row["id"] for row in web_client.get("/books").get_json()]
    with open_database(store) as database:
        store_ids = [row.id for row in database.books.list()]

    assert http_ids == store_ids


def test_list_books_service_returns_rows_in_the_order_added(store):
    with open_database(store) as database:
        for title in ["Service-one", "Service-two"]:
            database.books.create(title=title, author="Service Author")

        rows = list_books(database)

    assert [row.title for row in rows] == ["Service-one", "Service-two"]
    assert [row.id for row in rows] == sorted(row.id for row in rows)


def test_list_books_service_on_empty_store_returns_no_rows(store):
    with open_database(store) as database:
        assert list_books(database) == []
