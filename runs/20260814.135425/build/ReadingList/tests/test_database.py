from __future__ import annotations

import pytest

from app.database import Book, Database


def test_create_book_persists_an_unread_book(tmp_path):
    database = Database(str(tmp_path / "reading-list.sqlite"))

    created = database.create_book("The Left Hand of Darkness", "Ursula K. Le Guin")

    assert created == Book(
        id=created.id,
        title="The Left Hand of Darkness",
        author="Ursula K. Le Guin",
        is_read=False,
    )
    assert database.list_books() == [created]


def test_list_books_uses_insertion_order(tmp_path):
    database = Database(str(tmp_path / "reading-list.sqlite"))
    first = database.create_book("First Book", "First Author")
    second = database.create_book("Second Book", "Second Author")

    assert database.list_books() == [first, second]


def test_read_status_and_deletion_persist_across_database_instances(tmp_path):
    path = str(tmp_path / "reading-list.sqlite")
    database = Database(path)
    created = database.create_book("A Book", "An Author")

    assert database.mark_book_read(created.id) is True
    reopened = Database(path)
    assert reopened.list_books()[0].is_read is True
    assert reopened.delete_book(created.id) is True

    assert Database(path).list_books() == []


@pytest.mark.parametrize(
    ("title", "author"),
    [("", "An Author"), ("   ", "An Author"), ("A Book", ""), ("A Book", "   ")],
)
def test_create_book_rejects_blank_title_or_author(tmp_path, title, author):
    database = Database(str(tmp_path / "reading-list.sqlite"))

    with pytest.raises(ValueError):
        database.create_book(title, author)

    assert database.list_books() == []


def test_mutations_report_false_for_missing_books(tmp_path):
    database = Database(str(tmp_path / "reading-list.sqlite"))

    assert database.mark_book_read(999) is False
    assert database.delete_book(999) is False


def test_schema_initialization_is_idempotent(tmp_path):
    path = str(tmp_path / "reading-list.sqlite")

    Database(path)
    Database(path)

    assert Database(path).list_books() == []
