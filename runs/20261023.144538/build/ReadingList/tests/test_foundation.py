"""Foundation tests: project root, application factory, and test client helper."""

from pathlib import Path

from flask import Flask

from app_server import create_app
from app_server.testing import web_client

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def test_create_app_returns_flask_application():
    app = create_app()

    assert isinstance(app, Flask)


def test_create_app_returns_a_new_application_each_call():
    first = create_app()
    second = create_app()

    assert first is not second


def test_web_client_answers_unregistered_path_with_404():
    client = web_client()

    response = client.get("/arch-no-such-route")

    assert response.status_code == 404


def test_web_client_enables_testing_mode():
    client = web_client()

    assert client.application.config["TESTING"] is True


def test_web_client_fixture_answers_unregistered_path_with_404(web_client):
    response = web_client.get("/arch-no-such-route")

    assert response.status_code == 404


def test_project_root_carries_dependency_manifest_lockfile_and_conftest():
    for name in ("pyproject.toml", "uv.lock", "tests/conftest.py"):
        assert (PROJECT_ROOT / name).is_file(), name


def test_project_declares_flask_runtime_dependency():
    import tomllib

    manifest = tomllib.loads((PROJECT_ROOT / "pyproject.toml").read_text())

    assert any(dep.startswith("flask") for dep in manifest["project"]["dependencies"])
