"""Flask application factory for the ReadingList web application."""

from pathlib import Path

from flask import Flask

from persistence import open_database

from .books import bp as books_bp
from .settings import Settings

TEMPLATE_FOLDER = Path(__file__).resolve().parent / "templates"


def create_app() -> Flask:
    """Build and return the ReadingList Flask application.

    Opening the store does not connect to it; connections are made on first use, per thread.
    """
    settings = Settings.from_environment()
    app = Flask(__name__, template_folder=str(TEMPLATE_FOLDER))
    app.extensions["database"] = open_database(settings.database_url)
    app.register_blueprint(books_bp)
    return app
