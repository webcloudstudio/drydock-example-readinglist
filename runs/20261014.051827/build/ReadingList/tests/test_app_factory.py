from flask import Flask

from app_server import create_app


def test_create_app_returns_flask_instance():
    assert isinstance(create_app(), Flask)


def test_create_app_returns_a_new_application_each_call():
    assert create_app() is not create_app()


def test_create_app_registers_only_the_page_and_book_routes_besides_static():
    app = create_app()
    rules = {rule.rule for rule in app.url_map.iter_rules()}
    assert rules == {"/", "/static/<path:filename>", "/books", "/books/<int:book_id>"}


def test_create_app_leaves_testing_disabled_by_default():
    assert create_app().config["TESTING"] is False
