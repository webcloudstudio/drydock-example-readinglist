from __future__ import annotations

import sqlite3
import threading
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Book:
    id: int
    title: str
    author: str
    is_read: bool

    def as_dict(self) -> dict[str, int | str | bool]:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "is_read": self.is_read,
        }


class BookStore:
    """Typed persistence boundary for locally stored books."""

    def __init__(self, database_path: str) -> None:
        self._database_path = database_path
        self._local = threading.local()

    def _connect(self) -> sqlite3.Connection:
        connection = getattr(self._local, "connection", None)
        if connection is None:
            if self._database_path != ":memory:":
                Path(self._database_path).parent.mkdir(parents=True, exist_ok=True)
            connection = sqlite3.connect(self._database_path)
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA journal_mode=WAL")
            connection.execute("PRAGMA foreign_keys=ON")
            self._local.connection = connection
        return connection

    def initialize(self) -> None:
        self._connect().execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                is_read INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        columns = {
            row["name"]
            for row in self._connect().execute("PRAGMA table_info(books)").fetchall()
        }
        if "is_read" not in columns:
            self._connect().execute(
                "ALTER TABLE books ADD COLUMN is_read INTEGER NOT NULL DEFAULT 0"
            )
        self._connect().commit()

    def add(self, title: str, author: str) -> dict[str, int | str | bool]:
        connection = self._connect()
        cursor = connection.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)", (title, author)
        )
        connection.commit()
        return Book(int(cursor.lastrowid), title, author, False).as_dict()

    def list(self) -> list[dict[str, int | str | bool]]:
        rows = (
            self
            ._connect()
            .execute("SELECT id, title, author, is_read FROM books ORDER BY id ASC")
            .fetchall()
        )
        return [
            Book(int(row["id"]), row["title"], row["author"], bool(row["is_read"])).as_dict()
            for row in rows
        ]

    def mark_read(self, book_id: int) -> bool:
        connection = self._connect()
        cursor = connection.execute(
            "UPDATE books SET is_read = 1 WHERE id = ?", (book_id,)
        )
        connection.commit()
        return cursor.rowcount == 1

    def remove(self, book_id: int) -> bool:
        connection = self._connect()
        cursor = connection.execute("DELETE FROM books WHERE id = ?", (book_id,))
        connection.commit()
        return cursor.rowcount == 1
