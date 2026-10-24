"""Shared pytest fixtures for the ReadingList test suite."""

from collections.abc import Iterator

import pytest
from flask.testing import FlaskClient


@pytest.fixture
def web_client() -> FlaskClient:
    """Provide a Flask test client for the application factory."""
    from app_server.testing import web_client as make_client

    return make_client()


@pytest.fixture
def db_session() -> Iterator[object]:
    """Provide a rolled-back database session from the generated persistence package.

    The persistence package is generated from DATABASE.md at the DATABASE build step,
    so the import is deferred until a test requests this fixture.
    """
    from persistence.testing import db_session as open_session

    with open_session() as db:
        yield db
