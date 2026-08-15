"""Flask application factory for ReadingList."""

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from flask import Flask

from config import Config


def create_app(overrides: Mapping[str, Any] | Config | None = None) -> Flask:
    """Create an isolated ReadingList application instance."""
    settings = Config.load()
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

    database_path = Path(app.config["DATABASE"])
    if str(database_path) != ":memory:":
        database_path.parent.mkdir(parents=True, exist_ok=True)

    from app.persistence import initialize
    from app.routes import bp

    initialize(app.config["DATABASE"])
    app.register_blueprint(bp)
    return app
