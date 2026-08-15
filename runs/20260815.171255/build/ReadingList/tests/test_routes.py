import pytest


def test_root_renders_empty_list(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"ReadingList" in response.data


def test_reading_list_has_labeled_book_form_and_empty_state(client):
    response = client.get("/")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert '<form action="/books" method="post">' in body
    assert 'for="title"' in body
    assert 'name="title"' in body
    assert 'for="author"' in body
    assert 'name="author"' in body
    assert "empty" in body.lower()


def test_added_book_is_rendered_with_named_removal_control(client):
    created = client.post(
        "/books", data={"title": "Listed Book", "author": "Listed Author"}
    )

    assert created.status_code in (302, 303)
    body = client.get("/").get_data(as_text=True)
    assert "Listed Book" in body
    assert "Listed Author" in body
    assert "Remove" in body
    assert 'aria-label="Remove Listed Book"' in body


def test_added_book_is_rendered_as_unread_with_mark_read_control(client):
    client.post("/books", data={"title": "Unread Book", "author": "Author"})

    body = client.get("/").get_data(as_text=True)

    assert "Unread" in body
    assert 'action="/books/1/read"' in body
    assert 'aria-label="Mark Unread Book as read"' in body


def test_mark_read_route_persists_and_renders_read_state(client):
    client.post("/books", data={"title": "Finished Book", "author": "Author"})

    response = client.post("/books/1/read")
    body = client.get("/").get_data(as_text=True)

    assert response.status_code in (200, 302, 303)
    assert "Read" in body
    assert 'action="/books/1/read"' not in body
    with client.application.app_context():
        from app.persistence import get_book_store

        assert get_book_store().list_ordered()[0].is_read is True


def test_mark_read_route_with_unknown_id_keeps_all_books(client):
    client.post("/books", data={"title": "Still Unread", "author": "Author"})

    response = client.post("/books/999999/read")

    assert response.status_code in (200, 302, 303)
    assert "Still Unread" in client.get("/").get_data(as_text=True)


def test_book_creation_redirects_to_the_list(client):
    response = client.post(
        "/books", data={"title": "Middlemarch", "author": "George Eliot"}
    )

    assert response.status_code in (302, 303)
    assert response.headers["Location"].endswith("/")


def test_book_creation_preserves_existing_insertion_order(client):
    client.post("/books", data={"title": "First", "author": "Author One"})
    client.post("/books", data={"title": "Second", "author": "Author Two"})

    body = client.get("/").get_data(as_text=True)

    assert body.index("First") < body.index("Second")


def test_invalid_submission_keeps_reader_on_page_with_error(client):
    response = client.post("/books", data={"title": "", "author": "Known Author"})

    assert response.status_code == 400
    body = response.get_data(as_text=True)
    assert 'role="alert"' in body
    assert "title" in body.lower()
    assert "Known Author" in body


def test_invalid_submission_with_missing_author_returns_client_error(client):
    response = client.post("/books", data={"title": "Known Title", "author": ""})

    assert response.status_code == 400
    assert 'role="alert"' in response.get_data(as_text=True)


def test_submission_with_both_required_fields_missing_returns_client_error(client):
    response = client.post("/books", data={"title": "", "author": ""})

    assert response.status_code == 400
    assert 'role="alert"' in response.get_data(as_text=True)


@pytest.mark.parametrize(
    "title,author",
    [("Rejected Title", ""), ("", "Rejected Author"), ("", "")],
)
def test_invalid_submission_is_not_persisted(client, title, author):
    response = client.post("/books", data={"title": title, "author": author})

    assert response.status_code == 400
    with client.application.app_context():
        from app.persistence import get_book_store

        assert get_book_store().list_ordered() == []


def test_valid_submission_remains_supported_after_validation(client):
    response = client.post(
        "/books", data={"title": "Valid Title", "author": "Valid Author"}
    )

    assert response.status_code in (200, 302, 303)
    with client.application.app_context():
        from app.persistence import get_book_store

        books = get_book_store().list_ordered()

    assert [(book.title, book.author) for book in books] == [
        ("Valid Title", "Valid Author")
    ]


def test_removal_control_removes_only_target_book(client):
    client.post("/books", data={"title": "Keep", "author": "Author A"})
    client.post("/books", data={"title": "Remove", "author": "Author B"})
    with client.application.app_context():
        from app.persistence import get_book_store

        books = get_book_store().list_ordered()
        target_id = books[1].id

    response = client.post(f"/books/{target_id}/remove")
    body = client.get("/").get_data(as_text=True)

    assert response.status_code in (302, 303)
    assert "Keep" in body
    assert "<strong>Remove</strong>" not in body
    assert "<span>by Author B</span>" not in body


def test_removal_route_preserves_relative_order_of_remaining_books(client):
    client.post("/books", data={"title": "First Remaining", "author": "Author A"})
    client.post("/books", data={"title": "Middle Removed", "author": "Author B"})
    client.post("/books", data={"title": "Last Remaining", "author": "Author C"})

    with client.application.app_context():
        from app.persistence import get_book_store

        target_id = get_book_store().list_ordered()[1].id

    response = client.post(f"/books/{target_id}/remove")
    body = client.get("/").get_data(as_text=True)

    assert response.status_code in (200, 302, 303)
    assert body.index("First Remaining") < body.index("Last Remaining")
    assert "Middle Removed" not in body


def test_removal_route_with_unknown_id_keeps_all_books(client):
    client.post("/books", data={"title": "Still Here", "author": "Author"})

    response = client.post("/books/999999/remove")
    body = client.get("/").get_data(as_text=True)

    assert response.status_code in (200, 302, 303)
    assert "Still Here" in body
    assert "Author" in body


def test_health_reports_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
