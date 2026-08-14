from app import create_app


def test_factory_returns_testing_app_and_client():
    app = create_app({"TESTING": True, "READING_LIST_DATABASE": ":memory:"})

    assert app is not None
    assert app.config["TESTING"] is True
    assert app.test_client() is not None


def test_factory_calls_are_isolated_and_configurable():
    first = create_app({"TESTING": True, "READING_LIST_DATABASE": ":memory:"})
    second = create_app({"TESTING": False, "READING_LIST_DATABASE": ":memory:"})

    assert first is not second
    assert first.config["TESTING"] is True
    assert second.config["TESTING"] is False


def test_factory_registers_root_entry_point():
    app = create_app({"TESTING": True, "READING_LIST_DATABASE": ":memory:"})

    routes = {rule.rule for rule in app.url_map.iter_rules()}

    assert "/" in routes


def test_root_entry_point_renders_reading_list(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.content_type.startswith("text/html")
