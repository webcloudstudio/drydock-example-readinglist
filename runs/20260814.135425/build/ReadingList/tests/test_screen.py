from __future__ import annotations

from app.books import list_books


def test_screen_renders_a_useful_empty_state(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.content_type.startswith("text/html")
    body = response.get_data(as_text=True)
    assert "Reading list" in body
    assert "Your reading list is empty" in body
    assert 'action="/books"' in body


def test_screen_renders_books_in_addition_order_with_status_and_controls(client):
    client.post("/books", data={"title": "First", "author": "Author One"})
    client.post("/books", data={"title": "Second", "author": "Author Two"})
    books = list_books(client.application)
    client.post(f"/books/{books[0]['id']}/read")

    response = client.get("/")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert body.index("First") < body.index("Second")
    assert 'data-status="read"' in body
    assert 'data-status="unread"' in body
    assert f'action="/books/{books[1]["id"]}/read"' in body
    assert f'action="/books/{books[0]["id"]}/delete"' in body


def test_screen_declares_loading_feedback_for_every_mutating_form(client):
    response = client.get("/")
    body = response.get_data(as_text=True)

    assert 'data-loading-state aria-live="polite"' in body
    assert 'src="/static/app.js"' in body
    assert 'data-loading-form' in body
