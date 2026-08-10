from pathlib import Path

import pytest
from app import create_app


@pytest.fixture
def app(tmp_path: Path):
    return create_app({"TESTING": True, "DATABASE": str(tmp_path / "books.sqlite3")})


@pytest.fixture
def client(app):
    return app.test_client()
