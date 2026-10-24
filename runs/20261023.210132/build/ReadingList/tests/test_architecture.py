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
    routes = {
        (rule.rule, tuple(sorted(rule.methods - {"HEAD", "OPTIONS"})))
        for rule in app.url_map.iter_rules()
    }

    assert ("/", ("GET",)) in routes
    assert ("/books", ("POST",)) in routes
    assert ("/books/<int:book_id>/delete", ("POST",)) in routes


def test_primary_page_has_accessible_form_and_empty_state():
    app = create_app()
    app.config.update(TESTING=True)
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Books to read" in response.data
    assert b'for="title"' in response.data
    assert b'for="author"' in response.data
    assert b"Your reading list" in response.data


def test_add_book_preserves_values_and_insertion_order():
    app = create_app()
    app.config.update(TESTING=True)
    client = app.test_client()
    try:
        first = client.post("/books", data={"title": "Project First Book", "author": "A. One"})
        second = client.post("/books", data={"title": "Project Second Book", "author": "B. Two"})
        page = client.get("/")
        assert first.status_code == 302
        assert second.status_code == 302
        assert page.data.index(b"Project First Book") < page.data.index(b"Project Second Book")
    finally:
        _delete_titles("Project First Book", "Project Second Book")


def test_invalid_book_submission_preserves_values_and_reports_fields():
    app = create_app()
    app.config.update(TESTING=True)
    response = app.test_client().post("/books", data={"title": "  ", "author": "Reader"})
    assert response.status_code == 400
    assert b'value="  "' in response.data
    assert b"Title is required." in response.data


def test_invalid_author_submission_reports_author_field():
    app = create_app()
    app.config.update(TESTING=True)
    response = app.test_client().post(
        "/books", data={"title": "Validation Title", "author": "  "}
    )
    assert response.status_code == 400
    assert b'value="Validation Title"' in response.data
    assert b"Author is required." in response.data


def test_invalid_submission_can_be_corrected():
    app = create_app()
    app.config.update(TESTING=True)
    client = app.test_client()
    invalid = client.post("/books", data={"title": "", "author": "Correctable Author"})
    valid = client.post(
        "/books", data={"title": "Project Corrected Title", "author": "Corrected Author"}
    )
    assert invalid.status_code == 400
    assert valid.status_code == 302
    assert b"Project Corrected Title" in client.get("/").data
    _delete_titles("Project Corrected Title")


def test_remove_book_hides_it_from_next_read():
    app = create_app()
    app.config.update(TESTING=True)
    client = app.test_client()
    client.post("/books", data={"title": "Project Temporary Book", "author": "Reader"})
    from persistence import open_database
    database = open_database("data/app.db")
    try:
        book_id = next(
            book.id for book in database.books.list() if book.title == "Project Temporary Book"
        )
    finally:
        database.close()
    removed = client.post(f"/books/{book_id}/delete")
    page = client.get("/")
    assert removed.status_code == 302
    assert b"Project Temporary Book" not in page.data


def _delete_titles(*titles):
    from persistence import open_database

    database = open_database("data/app.db")
    try:
        for book in database.books.list():
            if book.title in titles:
                database.books.delete(id=book.id)
    finally:
        database.close()
