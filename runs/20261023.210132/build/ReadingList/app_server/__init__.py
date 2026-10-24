"""Application factory for the ReadingList web application."""

from __future__ import annotations

from flask import Flask

from app_server.config import ApplicationConfig
from app_server.features.reading_list import reading_list


def create_app() -> Flask:
    """Create a configured, independently usable Flask application."""

    app = Flask(__name__, instance_relative_config=True)
    settings = ApplicationConfig.load()
    app.config.from_mapping(settings.as_flask_config())

    app.register_blueprint(reading_list)
    return app
