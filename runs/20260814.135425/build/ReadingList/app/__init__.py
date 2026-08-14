"""Application factory for ReadingList."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from flask import Flask

from app.database import Database
from app.routes import main_blueprint


def create_app(test_config: dict[str, Any] | None = None) -> Flask:
    """Create an isolated Flask application instance."""
    app = Flask(__name__, template_folder="templates", static_folder="static")
    default_database = Path(app.instance_path) / "reading_list.sqlite3"
    app.config.from_mapping(
        TESTING=False,
        SECRET_KEY="reading-list-development-key",
        READING_LIST_DATABASE=str(default_database),
    )
    if test_config is not None:
        app.config.update(test_config)
        if "DATABASE" in test_config and "READING_LIST_DATABASE" not in test_config:
            app.config["READING_LIST_DATABASE"] = test_config["DATABASE"]

    database = Database(app.config["READING_LIST_DATABASE"])
    database.initialize()
    app.extensions["reading_list_database"] = database

    app.register_blueprint(main_blueprint)
    return app
