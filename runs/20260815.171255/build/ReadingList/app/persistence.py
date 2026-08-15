"""Typed SQLite persistence boundary for the reading list."""

import sqlite3
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from flask import current_app, g


@dataclass(frozen=True)
class Book:
    """A book record returned by the persistence interface."""

    id: int
    title: str
    author: str
    created_at: str | None = None
    is_read: bool = False


class BookStore:
    """Store books in SQLite while keeping SQL private to this module."""

    def __init__(
        self,
        database_path: str,
        connect: Callable[[], sqlite3.Connection] | None = None,
    ) -> None:
        self.database_path = database_path
        self._connect_provider = connect

    def _connect(self) -> sqlite3.Connection:
        if self._connect_provider is not None:
            return self._connect_provider()
        if self.database_path != ":memory:":
            Path(self.database_path).parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA journal_mode = WAL")
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def initialize(self) -> None:
        """Create or migrate the books table without changing existing rows."""
        connection = self._connect()
        try:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    is_read INTEGER NOT NULL DEFAULT 0
                )
                """
            )
            columns = {
                row["name"]
                for row in connection.execute("PRAGMA table_info(books)").fetchall()
            }
            if "is_read" not in columns:
                connection.execute(
                    "ALTER TABLE books ADD COLUMN is_read INTEGER NOT NULL DEFAULT 0"
                )
            connection.commit()
        finally:
            if self._connect_provider is None:
                connection.close()

    def add(self, title: str, author: str) -> Book:
        """Persist and return one book, rejecting incomplete submissions."""
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title is required")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("author is required")

        connection = self._connect()
        try:
            cursor = connection.execute(
                "INSERT INTO books (title, author) VALUES (?, ?)",
                (title, author),
            )
            connection.commit()
            row = connection.execute(
                "SELECT id, title, author, created_at, is_read FROM books WHERE id = ?",
                (cursor.lastrowid,),
            ).fetchone()
            assert row is not None
            return _book_from_row(row)
        finally:
            if self._connect_provider is None:
                connection.close()

    def list_ordered(self) -> list[Book]:
        """Return books in their SQLite-assigned insertion order."""
        connection = self._connect()
        try:
            rows = connection.execute(
                "SELECT id, title, author, created_at, is_read FROM books ORDER BY id"
            ).fetchall()
            return [_book_from_row(row) for row in rows]
        finally:
            if self._connect_provider is None:
                connection.close()

    def mark_read(self, book_id: int) -> bool:
        """Mark one book as read and report whether it exists."""
        connection = self._connect()
        try:
            cursor = connection.execute(
                "UPDATE books SET is_read = 1 WHERE id = ?", (book_id,)
            )
            connection.commit()
            return cursor.rowcount == 1
        finally:
            if self._connect_provider is None:
                connection.close()

    def remove(self, book_id: int) -> bool:
        """Delete a book and report whether a row was removed."""
        connection = self._connect()
        try:
            cursor = connection.execute("DELETE FROM books WHERE id = ?", (book_id,))
            connection.commit()
            return cursor.rowcount == 1
        finally:
            if self._connect_provider is None:
                connection.close()


def _book_from_row(row: sqlite3.Row) -> Book:
    return Book(
        id=row["id"],
        title=row["title"],
        author=row["author"],
        created_at=row["created_at"],
        is_read=bool(row["is_read"]),
    )


def _context_connection() -> sqlite3.Connection:
    connection = g.get("reading_list_db")
    if connection is None:
        database_path = current_app.config["DATABASE"]
        if database_path != ":memory:":
            Path(database_path).parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(database_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA journal_mode = WAL")
        connection.execute("PRAGMA foreign_keys = ON")
        g.reading_list_db = connection
    return connection


def get_book_store() -> BookStore:
    """Return the store bound to the current Flask application context."""
    store = g.get("reading_list_store")
    if store is None:
        store = BookStore(current_app.config["DATABASE"], _context_connection)
        g.reading_list_store = store
    return store


def close_connection(_: object | None = None) -> None:
    """Close the current request/workflow connection, if one was opened."""
    connection = g.pop("reading_list_db", None)
    if connection is not None:
        connection.close()


def initialize(database_path: str) -> None:
    """Initialize the schema without exposing SQLite to application code."""
    BookStore(database_path).initialize()
