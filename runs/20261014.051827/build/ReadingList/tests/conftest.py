"""Shared pytest fixtures. Each test receives its own client and its own temporary store."""

import pytest

from app_server import testing
from app_server.settings import DATABASE_ENV
from persistence.testing import db_session as open_session


@pytest.fixture(autouse=True)
def isolated_store(tmp_path, monkeypatch):
    monkeypatch.setenv(DATABASE_ENV, str(tmp_path / "app.db"))


@pytest.fixture
def web_client():
    return testing.web_client()


@pytest.fixture
def db_session():
    with open_session() as db:
        yield db
