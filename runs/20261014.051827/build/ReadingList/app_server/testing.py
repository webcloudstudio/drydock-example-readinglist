"""Test client helper shared by programmatic acceptance and the pytest fixture."""

from flask.testing import FlaskClient

from app_server import create_app


def web_client() -> FlaskClient:
    """Return a test client for a fresh application with TESTING enabled."""
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
