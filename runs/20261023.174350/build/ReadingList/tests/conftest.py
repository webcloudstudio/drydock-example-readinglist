"""Shared pytest configuration for the ReadingList test suite.

Exposes the project root, the in-process web client, and the rollback database session.
"""

from collections.abc import Iterator
from pathlib import Path

import pytest
from flask import Flask
from flask.testing import FlaskClient

from app_server import create_app
from app_server import testing as app_testing
from app_server.config import Config
from persistence import testing as persistence_testing
from persistence.db import Database

PROJECT_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Return the application root directory."""
    return PROJECT_ROOT


@pytest.fixture
def web_client() -> FlaskClient:
    """Return a test client for a testing-mode application."""
    return app_testing.web_client()


@pytest.fixture
def store_path(tmp_path: Path) -> Path:
    """Return the path of a store private to this test; the configured application store is never touched."""
    return tmp_path / "books.db"


@pytest.fixture
def fresh_app(store_path: Path, project_root: Path) -> Flask:
    """Return a testing-mode application over an empty store with the generated schema applied."""
    app = create_app(Config(database_dsn=str(store_path)))
    app.config["TESTING"] = True
    app.extensions["db"].execute_script((project_root / "schema.sql").read_text(encoding="utf-8"))
    return app


@pytest.fixture
def fresh_client(fresh_app: Flask) -> FlaskClient:
    """Return a test client bound to the empty per-test store."""
    return fresh_app.test_client()


@pytest.fixture
def fresh_db(fresh_app: Flask) -> Database:
    """Return the database handle of the empty per-test store."""
    return fresh_app.extensions["db"]


@pytest.fixture
def db_session() -> Iterator[Database]:
    """Yield the configured store's database inside a transaction that always rolls back."""
    with persistence_testing.db_session() as db:
        yield db
