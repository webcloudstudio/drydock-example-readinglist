"""Application factory wiring: template folder, persistence store, and no book routes."""

import sqlite3
from pathlib import Path

from persistence import Database
from app_server import create_app
from app_server.settings import DEFAULT_DATABASE_PATH, Settings

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def test_create_app_template_folder_is_app_server_templates():
    app = create_app()

    assert Path(app.jinja_loader.searchpath[0]).resolve() == (
        PROJECT_ROOT / "app_server" / "templates"
    ).resolve()


def test_create_app_exposes_database_opened_from_configured_store(monkeypatch, tmp_path):
    store = tmp_path / "wired.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{store}")
    monkeypatch.delenv("DATABASE_PATH", raising=False)

    app = create_app()

    assert isinstance(app.extensions["database"], Database)


def test_create_app_does_not_create_store_file_at_startup(monkeypatch, tmp_path):
    store = tmp_path / "lazy.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{store}")

    create_app()

    assert not store.exists()


def test_create_app_database_round_trips_through_configured_store(monkeypatch, tmp_path):
    store = tmp_path / "roundtrip.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{store}")
    app = create_app()
    db = app.extensions["database"]
    db.execute_script((PROJECT_ROOT / "schema.sql").read_text())

    created = db.books.create(title="Dune", author="Frank Herbert")
    fetched = db.books.get(id=created.id)

    assert fetched == created
    assert store.is_file()
    with sqlite3.connect(store) as connection:
        assert connection.execute('SELECT title, author FROM "books"').fetchall() == [
            ("Dune", "Frank Herbert")
        ]


def test_create_app_registers_only_book_routes_beside_static():
    app = create_app()

    endpoints = {rule.endpoint for rule in app.url_map.iter_rules()}

    assert endpoints == {
        "static",
        "books.index",
        "books.create_book",
        "books.get_books",
        "books.delete_book",
    }


def test_settings_default_store_path_when_no_environment_override(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("DATABASE_PATH", raising=False)

    assert Settings.from_environment().database_url == DEFAULT_DATABASE_PATH


def test_settings_prefer_database_url_over_database_path(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///from-url.db")
    monkeypatch.setenv("DATABASE_PATH", "from-path.db")

    assert Settings.from_environment().database_url == "sqlite:///from-url.db"


def test_settings_fall_back_to_database_path_when_url_absent(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setenv("DATABASE_PATH", "from-path.db")

    assert Settings.from_environment().database_url == "from-path.db"


def test_settings_treat_empty_database_url_as_absent(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "")
    monkeypatch.delenv("DATABASE_PATH", raising=False)

    assert Settings.from_environment().database_url == DEFAULT_DATABASE_PATH
