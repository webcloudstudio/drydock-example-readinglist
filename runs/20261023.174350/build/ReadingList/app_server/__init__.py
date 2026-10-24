"""Flask application factory for ReadingList."""

from __future__ import annotations

from flask import Flask

from persistence import open_database

from .config import Config
from .routes.books import books
from .routes.pages import pages


def create_app(config: Config | None = None) -> Flask:
    """Build the application. Routes come only from registered blueprints; no schema is applied here."""
    config = config or Config.load()
    app = Flask(__name__)
    app.extensions["db"] = open_database(config.database_dsn)
    app.register_blueprint(pages)
    app.register_blueprint(books)
    return app
