"""Book behavior: validate submissions, then store, list, and remove books through ``db.books``."""

from __future__ import annotations

from persistence import Database
from persistence.schema import Book

__all__ = ["add_book", "list_books", "remove_book", "validate_book_input"]


def validate_book_input(title: str | None, author: str | None) -> None:
    """Raise ValueError naming each field that is missing, not text, or blank after stripping."""
    blank = [
        name
        for name, value in (("title", title), ("author", author))
        if not isinstance(value, str) or not value.strip()
    ]
    if blank:
        raise ValueError(f"{' and '.join(blank)} must be non-empty text")


def add_book(db: Database, title: str | None, author: str | None) -> Book:
    """Validate the submission, then store exactly the title and author supplied."""
    validate_book_input(title, author)
    return db.books.create(title=title, author=author)


def list_books(db: Database) -> list[Book]:
    """Return every stored book in the order it was added."""
    return db.books.list()


def remove_book(db: Database, book_id: int) -> bool:
    """Delete the book and return True; return False and change nothing for an unknown id."""
    if db.books.get(id=book_id) is None:
        return False
    db.books.delete(id=book_id)
    return True
