"""App shell: application factory, configuration, test client, health route, and shared layout."""

from html.parser import HTMLParser

from flask import Flask
from flask.testing import FlaskClient

from app_server import create_app
from app_server.config import DEFAULT_DATABASE_PATH, Config
from app_server.testing import web_client as make_web_client
from persistence import Database


class _TitleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title = ""

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


def test_create_app_returns_flask_application() -> None:
    assert isinstance(create_app(), Flask)


def test_create_app_opens_database_handle_for_services() -> None:
    app = create_app(Config(database_dsn="data/app.db"))

    assert isinstance(app.extensions["db"], Database)


def test_web_client_returns_test_client_in_testing_mode() -> None:
    client = make_web_client()

    assert isinstance(client, FlaskClient)
    assert client.application.config["TESTING"] is True


def test_health_returns_200_with_status_body(web_client: FlaskClient) -> None:
    response = web_client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_unknown_route_returns_404(web_client: FlaskClient) -> None:
    response = web_client.get("/route-nobody-declared")

    assert response.status_code == 404


def test_factory_registers_only_the_declared_routes() -> None:
    app = create_app()

    rules = {rule.rule for rule in app.url_map.iter_rules() if rule.endpoint != "static"}

    assert rules == {
        "/",
        "/health",
        "/add",
        "/remove/<int:book_id>",
        "/books",
        "/books/<int:book_id>",
    }


def test_base_layout_renders_title_block() -> None:
    app = create_app()
    template = app.jinja_env.from_string(
        '{% extends "base.html" %}{% block title %}Shelf{% endblock %}'
        "{% block content %}<p>body</p>{% endblock %}"
    )

    parser = _TitleParser()
    parser.feed(template.render())

    assert parser.title == "Shelf"


def test_config_defaults_to_data_app_db() -> None:
    assert Config.load(environ={}).database_dsn == DEFAULT_DATABASE_PATH


def test_config_prefers_database_url_over_database_path() -> None:
    config = Config.load(environ={"DATABASE_URL": "sqlite:///tmp/a.db", "DATABASE_PATH": "b.db"})

    assert config.database_dsn == "sqlite:///tmp/a.db"


def test_config_uses_database_path_when_url_absent() -> None:
    config = Config.load(environ={"DATABASE_PATH": "b.db"})

    assert config.database_dsn == "b.db"
