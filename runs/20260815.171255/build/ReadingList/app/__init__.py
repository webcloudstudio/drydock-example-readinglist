"""Flask application factory for ReadingList."""

import tempfile
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from flask import Flask

from config import Config


def create_app(overrides: Mapping[str, Any] | Config | None = None) -> Flask:
    """Create an isolated ReadingList application instance."""
    settings = Config.load(require_secret=overrides is None)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=settings.secret_key,
        DATABASE=settings.database_path,
    )
    if isinstance(overrides, Config):
        app.config.update(
            SECRET_KEY=overrides.secret_key,
            DATABASE=overrides.database_path,
        )
    elif overrides is not None:
        app.config.update(overrides)

    if (
        isinstance(overrides, Mapping)
        and overrides.get("TESTING") is True
        and "DATABASE" not in overrides
    ):
        app.config["DATABASE"] = ":memory:"

    if app.config["DATABASE"] == ":memory:":
        temporary_database = tempfile.NamedTemporaryFile(
            prefix="reading-list-", suffix=".db", delete=False
        )
        temporary_database.close()
        app.config["DATABASE"] = temporary_database.name
    else:
        database_path = Path(app.config["DATABASE"])
        database_path.parent.mkdir(parents=True, exist_ok=True)

    from app.persistence import close_connection, initialize
    from app.routes import bp

    initialize(app.config["DATABASE"])
    app.teardown_appcontext(close_connection)
    app.register_blueprint(bp)
    return app
