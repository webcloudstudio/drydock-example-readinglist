from __future__ import annotations

from pathlib import Path
from typing import Any

from flask import Flask
from persistence import BookStore
from routes import register_routes


def create_app(config: dict[str, Any] | None = None) -> Flask:
    """Create an isolated ReadingList application instance."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="reading-list-local-development",
        DATABASE=str(Path.cwd() / "instance-reading-list.sqlite3"),
        TESTING=False,
    )
    if config:
        app.config.update(config)

    store = BookStore(str(app.config["DATABASE"]))
    store.initialize()
    app.extensions["book_store"] = store
    register_routes(app)
    return app
