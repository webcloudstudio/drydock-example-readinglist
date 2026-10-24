"""Reject empty fields: POST /books answers 400 with a clear error and stores nothing."""

import pytest
from flask.testing import FlaskClient

from persistence import Database

REJECTED_PAYLOADS = [
    {"title": "", "author": "A"},
    {"title": "T", "author": ""},
    {"title": "", "author": ""},
    {"title": "   ", "author": "A"},
    {"title": "T", "author": "\t\n"},
    {"author": "A"},
    {"title": "T"},
    {},
    {"title": 42, "author": "A"},
]


@pytest.mark.parametrize("payload", REJECTED_PAYLOADS)
def test_blank_or_missing_field_answers_400_with_error_message(
    fresh_client: FlaskClient, payload: dict
) -> None:
    response = fresh_client.post("/books", json=payload)

    assert response.status_code == 400
    assert isinstance(response.get_json()["error"], str)


@pytest.mark.parametrize(
    "payload, field",
    [({"title": "", "author": "A"}, "title"), ({"title": "T", "author": "  "}, "author")],
)
def test_error_names_the_offending_field(fresh_client: FlaskClient, payload: dict, field: str) -> None:
    error = fresh_client.post("/books", json=payload).get_json()["error"]

    assert field in error


def test_non_json_body_answers_400(fresh_client: FlaskClient) -> None:
    response = fresh_client.post("/books", data="not json", content_type="text/plain")

    assert response.status_code == 400


def test_rejected_submissions_store_nothing(fresh_client: FlaskClient, fresh_db: Database) -> None:
    kept = fresh_client.post("/books", json={"title": "Dune", "author": "A"}).get_json()
    before = [book.id for book in fresh_db.books.list()]

    for payload in REJECTED_PAYLOADS:
        assert fresh_client.post("/books", json=payload).status_code == 400

    after = [book.id for book in fresh_db.books.list()]
    assert after == before == [kept["id"]]
