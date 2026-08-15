"""Acceptance coverage for the ordered reading-list workflow."""


def test_root_is_successful_for_an_empty_store(client):
    response = client.get("/")

    assert response.status_code == 200


def test_empty_store_has_an_understandable_empty_state(client):
    body = client.get("/").get_data(as_text=True)

    assert body
    assert "empty" in body.lower() or "no books" in body.lower()


def test_root_renders_books_in_insertion_order(client):
    first_title = "First Added"
    first_author = "First Author"
    second_title = "Second Added"
    second_author = "Second Author"

    first_response = client.post(
        "/books", data={"title": first_title, "author": first_author}
    )
    second_response = client.post(
        "/books", data={"title": second_title, "author": second_author}
    )

    assert first_response.status_code in (302, 303)
    assert second_response.status_code in (302, 303)

    response = client.get("/")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert body.index(first_title) < body.index(second_title)
    assert first_author in body
    assert second_author in body
