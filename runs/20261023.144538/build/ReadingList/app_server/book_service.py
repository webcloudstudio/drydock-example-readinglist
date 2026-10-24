"""Book behavior for the ReadingList web application, free of any Flask dependency."""

from __future__ import annotations

from persistence import Database
from persistence.schema import BookRow


class BookRejected(ValueError):
    """A submission the application refuses to store; ``reason`` says why and ``field`` names the input."""

    def __init__(self, reason: str, field: str) -> None:
        super().__init__(reason)
        self.reason = reason
        self.field = field


class BookNotFound(LookupError):
    """A removal named an id that no stored book carries; ``book_id`` is that id."""

    def __init__(self, book_id: int) -> None:
        super().__init__(book_id)
        self.book_id = book_id


def add_book(database: Database, title: str, author: str) -> BookRow:
    """Store a book appended after every existing book and return the stored row.

    Values are expected already trimmed by the caller. An empty title or author is refused
    without touching the store, so a stored book always has both.
    """
    if not title:
        raise BookRejected("rejected: title is empty", field="title")
    if not author:
        raise BookRejected("rejected: author is empty", field="author")
    return database.books.create(title=title, author=author)


def list_books(database: Database) -> list[BookRow]:
    """Return every stored book in the order added, oldest first.

    The order is enforced here, by ascending id, rather than trusted to the store's select, which
    the generated persistence layer issues without an ORDER BY clause.
    """
    return sorted(database.books.list(), key=lambda row: row.id)


def remove_book(database: Database, book_id: int) -> None:
    """Delete the stored book with ``book_id``; the remaining books keep their order.

    An id that no stored book carries is refused with ``BookNotFound`` before any write, so an
    unknown id never changes stored data.
    """
    if database.books.get(id=book_id) is None:
        raise BookNotFound(book_id)
    database.books.delete(id=book_id)
