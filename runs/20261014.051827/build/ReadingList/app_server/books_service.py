"""Framework-independent book operations for the reading list."""

from persistence import Database
from persistence.schema import Book

__all__ = ["InvalidBook", "add_book", "list_books", "remove_book"]


class InvalidBook(ValueError):
    """A submitted book was rejected; ``field`` names the empty or missing field."""

    def __init__(self, field: str) -> None:
        super().__init__(f"{field} must not be empty")
        self.field = field


def add_book(database: Database, title: object, author: object) -> Book:
    """Store a book whose title and author are non-empty after trimming, and return it with its id."""
    cleaned_title = _required("title", title)
    cleaned_author = _required("author", author)
    book_id = database.books.create(title=cleaned_title, author=cleaned_author)
    return Book(id=book_id, title=cleaned_title, author=cleaned_author)


def list_books(database: Database) -> list[Book]:
    """Return every stored book in the order it was added, which is ascending id."""
    # Sorted here rather than trusting the engine's row order, since SELECT carries no ORDER BY.
    return sorted(database.books.list(), key=lambda book: book.id)


def remove_book(database: Database, book_id: int) -> bool:
    """Remove the book with ``book_id``. Return False and change nothing when no such book is stored."""
    if database.books.get(id=book_id) is None:
        return False
    database.books.delete(id=book_id)
    return True


def _required(field: str, value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise InvalidBook(field)
    return value.strip()
