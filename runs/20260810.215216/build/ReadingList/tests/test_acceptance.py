from pathlib import Path

from app import create_app


def test_application_factory_is_testable():
    app = create_app({"TESTING": True, "DATABASE": ":memory:"})
    assert app is not None
    assert app.test_client() is not None


def test_root_route(client):
    response = client.get("/")
    assert response.status_code == 200


def test_list_route_starts_empty(tmp_path: Path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "books.sqlite3")})
    response = app.test_client().get("/books")
    assert response.status_code == 200
    assert response.get_json() == []


def test_add_route_redirects_for_valid_book(tmp_path: Path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "books.sqlite3")})
    response = app.test_client().post(
        "/books", data={"title": "Dune", "author": "Frank Herbert"}
    )
    assert response.status_code in (302, 303)


def test_add_round_trip_returns_both_fields(tmp_path: Path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "books.sqlite3")})
    client = app.test_client()
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})
    books = client.get("/books").get_json()
    assert books[-1]["title"] == "Dune"
    assert books[-1]["author"] == "Frank Herbert"
    assert books[0].keys() >= {"id", "title", "author"}


def test_list_round_trip_preserves_insertion_order(tmp_path: Path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "books.sqlite3")})
    client = app.test_client()
    client.post("/books", data={"title": "One", "author": "A"})
    client.post("/books", data={"title": "Two", "author": "B"})
    books = client.get("/books").get_json()
    assert [book["title"] for book in books] == ["One", "Two"]


def test_remove_selected_book_and_preserve_other_books(tmp_path: Path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "books.sqlite3")})
    client = app.test_client()
    client.post("/books", data={"title": "Book One", "author": "Author One"})
    client.post("/books", data={"title": "Book Two", "author": "Author Two"})
    books = client.get("/books").get_json()
    response = client.post(f"/books/{books[0]['id']}/remove")
    assert response.status_code in (200, 204, 302)
    assert client.get("/books").get_json() == [books[1]]


def test_unknown_book_removal_does_not_change_list(client):
    response = client.post("/books/999999/remove")
    assert response.status_code in (404, 204, 302)
    assert client.get("/books").get_json() == []


def test_local_database_configuration(tmp_path: Path):
    database = tmp_path / "reading-list.sqlite3"
    app = create_app({"TESTING": True, "DATABASE": str(database)})
    assert app.test_client().get("/").status_code == 200
    assert database.exists()


def test_store_round_trip_and_insertion_order(tmp_path: Path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "books.sqlite3")})
    store = app.extensions["book_store"]
    first = store.add("Dune", "Frank Herbert")
    store.add("Second", "Author B")
    books = store.list()
    assert any(
        book["id"] == first["id"] and book["title"] == "Dune" and book["author"] == "Frank Herbert"
        for book in books
    )
    assert [book["title"] for book in books] == ["Dune", "Second"]


def test_store_remove(tmp_path: Path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "books.sqlite3")})
    store = app.extensions["book_store"]
    created = store.add("Remove me", "Author")
    store.remove(created["id"])
    assert all(book["id"] != created["id"] for book in store.list())


def test_store_adds_books_as_unread_and_marks_them_read(tmp_path: Path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "books.sqlite3")})
    store = app.extensions["book_store"]
    created = store.add("Read later", "Author")

    assert store.list()[0]["is_read"] is False
    assert store.mark_read(created["id"]) is True
    assert store.list()[0]["is_read"] is True


def test_store_migrates_existing_books_as_unread(tmp_path: Path):
    database = tmp_path / "legacy.sqlite3"
    import sqlite3

    connection = sqlite3.connect(database)
    connection.execute(
        "CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL)"
    )
    connection.execute("INSERT INTO books (title, author) VALUES ('Legacy', 'Author')")
    connection.commit()
    connection.close()

    app = create_app({"TESTING": True, "DATABASE": str(database)})
    assert app.extensions["book_store"].list()[0]["is_read"] is False


def test_mark_read_route_persists_selected_book_state(client):
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})
    book = client.get("/books").get_json()[0]

    response = client.post(f"/books/{book['id']}/read")

    assert response.status_code == 302
    assert client.get("/books").get_json() == [{**book, "is_read": True}]


def test_mark_read_route_rejects_unknown_book(client):
    response = client.post("/books/999999/read")

    assert response.status_code == 404


def test_add_and_remove_workflow(client):
    added = client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})
    assert added.status_code == 302
    page = client.get("/")
    assert page.status_code == 200
    removed = client.post("/books/1/remove")
    assert removed.status_code == 302


def test_empty_fields_are_rejected_and_values_remain(client):
    response = client.post("/books", data={"title": " ", "author": ""})
    assert response.status_code == 400
    assert client.get("/books").get_json() == []


def test_empty_title_is_rejected_before_persistence(client):
    response = client.post("/books", data={"title": "", "author": "Author"})
    assert response.status_code == 400
    assert client.get("/books").get_json() == []


def test_empty_author_is_rejected_before_persistence(client):
    response = client.post("/books", data={"title": "Book", "author": "   "})
    assert response.status_code == 400
    assert client.get("/books").get_json() == []


def test_empty_state_is_rendered(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"empty" in response.data.lower()


def test_reading_list_screen_renders_title_and_author_inputs(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"title" in response.data.lower()
    assert b"author" in response.data.lower()


def test_reading_list_screen_renders_added_book_in_order(client):
    client.post("/books", data={"title": "Book", "author": "Author"})

    response = client.get("/")

    assert response.status_code == 200
    assert b"Book" in response.data
    assert b"Author" in response.data


def test_reading_list_screen_renders_unread_state_and_mark_read_control(client):
    client.post("/books", data={"title": "Book", "author": "Author"})

    response = client.get("/")

    assert b"Unread" in response.data
    assert b"Mark as read" in response.data


def test_reading_list_screen_renders_read_state_without_mark_read_control(client):
    client.post("/books", data={"title": "Book", "author": "Author"})
    book = client.get("/books").get_json()[0]
    client.post(f"/books/{book['id']}/read")

    response = client.get("/")

    assert b"Read" in response.data
    assert b"Mark as read" not in response.data


def test_reading_list_screen_form_submits_to_creation_workflow(client):
    response = client.post("/", data={"title": "Book", "author": "Author"})

    assert response.status_code in (200, 201, 302)
    assert client.get("/books").get_json()[0]["title"] == "Book"


def test_reading_list_screen_remove_control_removes_selected_book(client):
    client.post("/books", data={"title": "Book", "author": "Author"})
    book = client.get("/books").get_json()[0]

    response = client.post(f"/books/{book['id']}/remove")

    assert response.status_code in (200, 204, 302)
    assert client.get("/books").get_json() == []


def test_reading_list_screen_shows_validation_failure_without_persisting(client):
    response = client.post("/", data={"title": "", "author": "Author"})

    assert response.status_code == 400
    assert len(response.data) > 0
    assert client.get("/books").get_json() == []
