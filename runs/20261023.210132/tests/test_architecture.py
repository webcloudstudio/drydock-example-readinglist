from flask import Flask

from app_server import create_app
from app_server.testing import web_client


def test_factory_exposes_flask_application_and_testing_client():
    app = create_app()

    assert isinstance(app, Flask)
    assert web_client() is not None


def test_factory_creates_independent_applications():
    first = create_app()
    second = create_app()

    assert first is not second
    assert first.name == second.name


def test_factory_registers_declared_route_boundaries():
    app = create_app()
    routes = {(rule.rule, tuple(sorted(rule.methods - {"HEAD", "OPTIONS"}))) for rule in app.url_map.iter_rules()}

    assert ("/", ("GET",)) in routes
    assert ("/books", ("POST",)) in routes
    assert ("/books/<int:book_id>/delete", ("POST",)) in routes
