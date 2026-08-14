"""SQLite persistence boundary for ReadingList."""

from __future__ import annotations

import sqlite3
import threading
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Book:
    """A book persisted in the reading list."""

    id: int
    title: str
    author: str
    is_read: bool


class Database:
    """Owns SQLite setup and persistence operations."""

    def __init__(self, path: str) -> None:
        self.path = path
        self._connections = threading.local()
        self.initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = getattr(self._connections, "connection", None)
        if connection is not None:
            return connection
        if self.path != ":memory:":
            Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA journal_mode = WAL")
        self._connections.connection = connection
        return connection

    def initialize(self) -> None:
        """Create the schema if it does not already exist."""
        connection = self._connect()
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                is_read INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        connection.commit()

    def list_books(self) -> list[Book]:
        """Return books in insertion order."""
        connection = self._connect()
        rows = connection.execute(
            "SELECT id, title, author, is_read FROM books ORDER BY id"
        ).fetchall()
        return [
            Book(
                id=row["id"],
                title=row["title"],
                author=row["author"],
                is_read=bool(row["is_read"]),
            )
            for row in rows
        ]

    def create_book(self, title: str, author: str) -> Book:
        """Persist and return an unread book."""
        self._validate_book_fields(title, author)
        connection = self._connect()
        cursor = connection.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)", (title, author)
        )
        connection.commit()
        return Book(id=cursor.lastrowid, title=title, author=author, is_read=False)

    def delete_book(self, book_id: int) -> bool:
        """Delete a book and report whether a row was removed."""
        connection = self._connect()
        cursor = connection.execute("DELETE FROM books WHERE id = ?", (book_id,))
        connection.commit()
        return cursor.rowcount == 1

    def mark_book_read(self, book_id: int) -> bool:
        """Mark a book as read and report whether a row was updated."""
        connection = self._connect()
        cursor = connection.execute(
            "UPDATE books SET is_read = 1 WHERE id = ?", (book_id,)
        )
        connection.commit()
        return cursor.rowcount == 1

    @staticmethod
    def _validate_book_fields(title: str, author: str) -> None:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Book title must not be empty.")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Book author must not be empty.")
