"""In-process test client for acceptance checks and the pytest web_client fixture."""

from __future__ import annotations

from flask.testing import FlaskClient

from app_server import create_app


def web_client() -> FlaskClient:
    """Return a test client for an application created in testing mode."""
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
