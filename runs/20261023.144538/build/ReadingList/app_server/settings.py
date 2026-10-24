"""Typed runtime settings for the ReadingList web application."""

from __future__ import annotations

import os
from dataclasses import dataclass

DEFAULT_DATABASE_PATH = "data/app.db"


@dataclass(frozen=True)
class Settings:
    """Runtime settings read from the environment."""

    database_url: str

    @classmethod
    def from_environment(cls) -> Settings:
        """Read DATABASE_URL, then DATABASE_PATH, then fall back to the default store path."""
        configured = (
            os.environ.get("DATABASE_URL") or os.environ.get("DATABASE_PATH") or DEFAULT_DATABASE_PATH
        )
        return cls(database_url=configured)
