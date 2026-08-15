"""Application configuration loaded from the environment."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    """Typed settings shared by every application entry point."""

    secret_key: str
    database_path: str = "data/reading_list.db"

    @classmethod
    def load(cls, *, require_secret: bool = True) -> "Config":
        secret_key = os.environ.get("SECRET_KEY")
        if secret_key is None and require_secret:
            raise RuntimeError("Missing required env var: 'SECRET_KEY'")
        if secret_key is None:
            secret_key = "testing-only"
        return cls(
            secret_key=secret_key,
            database_path=os.environ.get("DATABASE_PATH", "data/reading_list.db"),
        )
