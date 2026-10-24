"""Validation: an empty or whitespace-only title or author is refused with 400, a reason, and nothing stored."""

import os
from pathlib import Path

import pytest

from persistence import open_database

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_ACCEPT = {"Accept": "application/json"}
SEED = {"title": "Dune", "author": "Frank Herbert"}

REJECTED_SUBMISSIONS = [
    pytest.param("title", {"title": "", "author": "Frank Herbert"}, id="empty-title"),
    pytest.param("title", {"title": "   ", "author": "Frank Herbert"}, id="spaces-title"),
    pytest.param("title", {"title": " \t\n ", "author": "Frank Herbert"}, id="tab-newline-title"),
    pytest.param("title", {"author": "Frank Herbert"}, id="title-absent"),
    pytest.param("author", {"title": "Dune", "author": ""}, id="empty-author"),
    pytest.param("author", {"title": "Dune", "author": "   "}, id="spaces-author"),
    pytest.param("author", {"title": "Dune", "author": " \t\n "}, id="tab-newline-author"),
    pytest.param("author", {"title": "Dune"}, id="author-absent"),
]


@pytest.fixture(autouse=True)
def isolated_store(monkeypatch, tmp_path):
    """Give each test its own store, provisioned from schema.sql, so no test touches data/app.db.

    The ``web_client`` fixture reads DATABASE_URL when it builds the application, so it
    follows this store.
    """
    url = f"sqlite:///{tmp_path / 'validation.db'}"
    monkeypatch.setenv("DATABASE_URL", url)
    monkeypatch.delenv("DATABASE_PATH", raising=False)
    database = open_database(url)
    try:
        database.execute_script((PROJECT_ROOT / "schema.sql").read_text())
    finally:
        database.close()
    return url


@pytest.mark.parametrize(("field", "form"), REJECTED_SUBMISSIONS)
def test_json_rejection_answers_400(web_client, field, form):
    response = web_client.post("/books", data=form, headers=JSON_ACCEPT)

    assert response.status_code == 400


@pytest.mark.parametrize(("field", "form"), REJECTED_SUBMISSIONS)
def test_json_rejection_body_has_non_empty_reason(web_client, field, form):
    response = web_client.post("/books", data=form, headers=JSON_ACCEPT)

    body = response.get_json()
    assert isinstance(body["error"], str)
    assert body["error"].strip()


@pytest.mark.parametrize(("field", "form"), REJECTED_SUBMISSIONS)
def test_json_rejection_names_offending_field(web_client, field, form):
    response = web_client.post("/books", data=form, headers=JSON_ACCEPT)

    assert response.get_json()["field"] == field


@pytest.mark.parametrize(("field", "form"), REJECTED_SUBMISSIONS)
def test_rejected_submission_leaves_stored_list_unchanged(web_client, field, form):
    web_client.post("/books", data=SEED)
    before = web_client.get("/books").get_json()

    web_client.post("/books", data=form, headers=JSON_ACCEPT)

    assert web_client.get("/books").get_json() == before
    assert len(before) == 1


@pytest.mark.parametrize(("field", "form"), REJECTED_SUBMISSIONS)
def test_rejected_submission_on_empty_list_stores_nothing(web_client, field, form):
    web_client.post("/books", data=form, headers=JSON_ACCEPT)

    assert web_client.get("/books").get_json() == []


@pytest.mark.parametrize(("field", "form"), REJECTED_SUBMISSIONS)
def test_browser_rejection_answers_400_with_non_empty_page(web_client, field, form):
    response = web_client.post("/books", data=form)

    assert response.status_code == 400
    assert len(response.get_data()) > 0
