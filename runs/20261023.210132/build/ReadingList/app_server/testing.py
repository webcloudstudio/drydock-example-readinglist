"""Testing entry points for the application."""

from __future__ import annotations

from flask.testing import FlaskClient

from app_server import create_app


def web_client() -> FlaskClient:
    """Return a Flask test client backed by a fresh application instance."""

    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
