"""Acceptance coverage for the reader-facing reading-list screen."""


def test_screen_loads_at_root(client):
    response = client.get("/")

    assert response.status_code == 200


def test_screen_accepts_book_submission(client):
    title = "Screen Book"
    author = "Screen Author"

    response = client.post("/books", data={"title": title, "author": author})

    assert response.status_code in (200, 302, 303)
    listed = client.get("/")
    assert listed.status_code == 200
    assert title in listed.get_data(as_text=True)
    assert author in listed.get_data(as_text=True)


def test_screen_removes_book_using_its_identity(client):
    client.post(
        "/books", data={"title": "Screen Removal", "author": "Screen Removal Author"}
    )

    response = client.post("/books/1/remove")

    assert response.status_code in (200, 302, 303)
    listed = client.get("/")
    assert listed.status_code == 200
    assert "Screen Removal" not in listed.get_data(as_text=True)


def test_screen_supports_an_empty_list(client):
    response = client.get("/")

    assert response.status_code == 200
