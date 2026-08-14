from __future__ import annotations

from app.books import list_books

def test_post_books_redirects_after_adding_valid_book(client):
    response = client.post(
        "/books", data={"title": "A Valid Book", "author": "A Valid Author"}
    )

    assert response.status_code == 303
    assert response.headers["Location"].endswith("/")


def test_post_books_makes_new_book_visible_in_reading_list(client):
    client.post("/books", data={"title": "Visible Title", "author": "Visible Author"})

    response = client.get("/")

    assert response.status_code == 200
    assert b"Visible Title by Visible Author" in response.data


def test_post_books_appends_after_existing_books(client):
    client.post("/books", data={"title": "First Title", "author": "First Author"})
    client.post("/books", data={"title": "Second Title", "author": "Second Author"})

    body = client.get("/").get_data(as_text=True)

    assert body.index("First Title by First Author") < body.index(
        "Second Title by Second Author"
    )


def test_new_book_is_displayed_as_unread(client):
    client.post("/books", data={"title": "Unread Title", "author": "Unread Author"})

    body = client.get("/").get_data(as_text=True)

    assert "Unread Title by Unread Author" in body
    assert 'data-status="unread"' in body
    assert "Unread" in body


def test_read_status_is_displayed_after_persistence(client, app):
    client.post("/books", data={"title": "Read Title", "author": "Read Author"})
    book = app.extensions["reading_list_database"].list_books()[0]
    assert app.extensions["reading_list_database"].mark_book_read(book.id) is True

    body = client.get("/").get_data(as_text=True)

    assert "Read Title by Read Author" in body
    assert 'data-status="read"' in body
    assert "Read" in body


def test_mark_read_route_accepts_an_existing_book(client, app):
    client.post("/books", data={"title": "Readable Book", "author": "Readable Author"})
    book = list_books(app)[0]

    response = client.post(f"/books/{book['id']}/read")

    assert response.status_code in (200, 302, 303)


def test_mark_read_changes_status_on_the_next_list_view(client, app):
    client.post("/books", data={"title": "Finished Book", "author": "Finished Author"})
    book = list_books(app)[0]

    before = client.get("/")
    assert before.status_code == 200
    assert "Unread" in before.get_data(as_text=True)

    update_response = client.post(f"/books/{book['id']}/read")
    after = client.get("/")

    assert update_response.status_code in (200, 302, 303)
    assert after.status_code == 200
    after_body = after.get_data(as_text=True)
    assert "Read" in after_body
    assert "Finished Book" in after_body


def test_mark_read_persists_across_separate_list_requests(client, app):
    client.post(
        "/books", data={"title": "Persisted Read Book", "author": "Persisted Read Author"}
    )
    book = list_books(app)[0]
    client.post(f"/books/{book['id']}/read")

    first = client.get("/")
    second = client.get("/")

    assert first.status_code == 200
    assert second.status_code == 200
    assert "Read" in first.get_data(as_text=True)
    assert "Read" in second.get_data(as_text=True)


def test_mark_read_changes_only_the_selected_book(client, app):
    client.post("/books", data={"title": "First Book", "author": "First Author"})
    client.post("/books", data={"title": "Second Book", "author": "Second Author"})
    books = list_books(app)

    client.post(f"/books/{books[0]['id']}/read")

    assert [book["is_read"] for book in list_books(app)] == [True, False]


def test_mark_read_is_idempotent_for_an_already_read_book(client, app):
    client.post("/books", data={"title": "Already Read", "author": "An Author"})
    book = list_books(app)[0]

    first = client.post(f"/books/{book['id']}/read")
    second = client.post(f"/books/{book['id']}/read")

    assert first.status_code == 303
    assert second.status_code == 303
    assert list_books(app)[0]["is_read"] is True


def test_post_books_rejects_blank_title_without_persisting(client):
    response = client.post(
        "/books", data={"title": "   ", "author": "An Author"}
    )

    assert response.status_code == 400
    assert response.request.path == "/books"
    assert client.get("/").get_data(as_text=True).count("An Author") == 0


def test_post_books_rejects_blank_author_without_persisting(client):
    response = client.post(
        "/books", data={"title": "A Book", "author": ""}
    )

    assert response.status_code == 400
    assert response.request.path == "/books"
    assert client.get("/").get_data(as_text=True).count("A Book by") == 0


def test_delete_route_redirects_after_removing_selected_book(client, app):
    client.post("/books", data={"title": "Removable Book", "author": "Removable Author"})
    book = list_books(app)[0]

    response = client.post(f"/books/{book['id']}/delete")

    assert response.status_code == 303
    assert response.headers["Location"].endswith("/")


def test_delete_route_removes_selected_book_and_preserves_remaining_order(client, app):
    client.post("/books", data={"title": "Removed Book", "author": "Removed Author"})
    client.post("/books", data={"title": "Remaining Book", "author": "Remaining Author"})
    removed = list_books(app)[0]

    response = client.post(f"/books/{removed['id']}/delete")

    assert response.status_code == 303
    books = list_books(app)
    assert [book["title"] for book in books] == ["Remaining Book"]
    body = client.get("/").get_data(as_text=True)
    assert "Removed Book" not in body
    assert "Remaining Book by Remaining Author" in body


def test_delete_route_is_idempotent_for_missing_book(client):
    response = client.post("/books/999999/delete")

    assert response.status_code == 303
