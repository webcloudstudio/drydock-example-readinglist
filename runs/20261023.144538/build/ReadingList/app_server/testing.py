"""Test helpers for the ReadingList web application."""

from flask.testing import FlaskClient

from app_server import create_app


def web_client() -> FlaskClient:
    """Return a Flask test client for a fresh application with TESTING enabled."""
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
