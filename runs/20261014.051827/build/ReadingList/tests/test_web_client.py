from flask import Flask

from app_server import testing


def test_web_client_returns_client_for_testing_application():
    client = testing.web_client()
    assert isinstance(client.application, Flask)
    assert client.application.config["TESTING"] is True


def test_web_client_answers_unregistered_path_with_404():
    client = testing.web_client()
    response = client.get("/unregistered-probe-path")
    assert response.status_code == 404


def test_web_client_fixture_delegates_to_helper(web_client):
    assert web_client.application.config["TESTING"] is True
    assert web_client.get("/unregistered-probe-path").status_code == 404
