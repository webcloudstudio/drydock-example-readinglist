"""Runtime settings for the reading list, read when the application is created."""

import os
from pathlib import Path

__all__ = ["DATABASE_ENV", "DATABASE_EXTENSION", "PROJECT_ROOT", "database_dsn"]

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_ENV = "READINGLIST_DATABASE"
DATABASE_EXTENSION = "readinglist.database"


def database_dsn() -> str:
    """Return the store named by READINGLIST_DATABASE, or the development store under data/."""
    configured = os.environ.get(DATABASE_ENV)
    if configured:
        return configured
    return f"sqlite://{PROJECT_ROOT / 'data' / 'app.db'}"
