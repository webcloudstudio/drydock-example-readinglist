import importlib

from app import create_app


def test_factory_creates_runnable_application():
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})
    response = application.test_client().get("/")
    assert response.status_code == 200


def test_factory_isolates_application_instances():
    first = create_app({"TESTING": True, "DATABASE": ":memory:"})
    second = create_app({"TESTING": True, "DATABASE": ":memory:"})
    assert first is not second
    assert first.test_client().get("/").status_code == 200
    assert second.test_client().get("/").status_code == 200


def test_testing_factory_uses_isolated_database_by_default():
    first = create_app({"TESTING": True})
    second = create_app({"TESTING": True})

    first.test_client().post(
        "/books", data={"title": "Only First", "author": "Author"}
    )

    assert b"Only First" in first.test_client().get("/").data
    assert b"Only First" not in second.test_client().get("/").data


def test_app_module_exposes_factory_without_starting_server():
    module = importlib.import_module("app")
    assert callable(module.create_app)
