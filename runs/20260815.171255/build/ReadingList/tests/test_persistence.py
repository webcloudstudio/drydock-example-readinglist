import sqlite3

import pytest

from app import create_app
from app.persistence import get_book_store


def test_add_reads_back_submitted_book():
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})

    with application.app_context():
        store = get_book_store()
        created = store.add("The Dispossessed", "Ursula K. Le Guin")
        books = store.list_ordered()

    assert len(books) == 1
    assert books[0].id == created.id
    assert books[0].title == "The Dispossessed"
    assert books[0].author == "Ursula K. Le Guin"
    assert books[0].is_read is False


def test_initialize_migrates_existing_rows_to_unread(tmp_path):
    database_path = str(tmp_path / "legacy-books.db")
    connection = sqlite3.connect(database_path)
    connection.execute(
        """
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    connection.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        ("Legacy Book", "Legacy Author"),
    )
    connection.commit()
    connection.close()

    application = create_app({"TESTING": True, "DATABASE": database_path})
    with application.app_context():
        books = get_book_store().list_ordered()

    assert [(book.title, book.is_read) for book in books] == [("Legacy Book", False)]


def test_mark_read_persists_and_is_idempotent():
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})

    with application.app_context():
        store = get_book_store()
        created = store.add("A Book", "An Author")

        assert store.mark_read(created.id) is True
        assert store.list_ordered()[0].is_read is True
        assert store.mark_read(created.id) is True
        assert store.list_ordered()[0].is_read is True


def test_mark_read_reports_missing_book():
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})

    with application.app_context():
        assert get_book_store().mark_read(999999) is False


def test_list_ordered_preserves_addition_order():
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})

    with application.app_context():
        store = get_book_store()
        store.add("A", "Author A")
        store.add("B", "Author B")
        books = store.list_ordered()

    assert [book.title for book in books] == ["A", "B"]
    assert [book.author for book in books] == ["Author A", "Author B"]


def test_remove_existing_book_removes_it():
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})

    with application.app_context():
        store = get_book_store()
        created = store.add("To Remove", "Author")
        removed = store.remove(created.id)

        assert removed is True
        assert store.list_ordered() == []


def test_new_database_lists_no_books():
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})

    with application.app_context():
        assert get_book_store().list_ordered() == []


@pytest.mark.parametrize("title, author", [("", "Author"), ("Title", "")])
def test_add_rejects_empty_fields(title, author):
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})

    with application.app_context():
        store = get_book_store()
        with pytest.raises(ValueError):
            store.add(title, author)
        assert store.list_ordered() == []


def test_remove_missing_book_reports_false():
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})

    with application.app_context():
        assert get_book_store().remove(999999) is False


def test_initialization_is_idempotent_and_keeps_rows(tmp_path):
    database_path = str(tmp_path / "books.db")
    application = create_app({"TESTING": True, "DATABASE": database_path})

    with application.app_context():
        store = get_book_store()
        store.add("Persisted", "Author")

    from app.persistence import initialize

    initialize(database_path)
    second = create_app({"TESTING": True, "DATABASE": database_path})
    with second.app_context():
        assert [book.title for book in get_book_store().list_ordered()] == ["Persisted"]


def test_database_rejects_null_book_fields(tmp_path):
    database_path = str(tmp_path / "books.db")
    application = create_app({"TESTING": True, "DATABASE": database_path})

    with application.app_context():
        connection = get_book_store()._connect()
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO books (title, author) VALUES (?, ?)",
                (None, "Author"),
            )
