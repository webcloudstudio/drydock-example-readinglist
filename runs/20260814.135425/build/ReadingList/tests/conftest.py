from __future__ import annotations

import pytest

from app import create_app


@pytest.fixture
def app():
    return create_app({"TESTING": True, "READING_LIST_DATABASE": ":memory:"})


@pytest.fixture
def client(app):
    return app.test_client()
