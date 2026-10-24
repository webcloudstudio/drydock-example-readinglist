"""Typed application configuration defaults."""

from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class ApplicationConfig:
    """Settings owned by the application boundary."""

    database_path: str = "data/app.db"
    database_url: str | None = None
    secret_key: str | None = None

    @classmethod
    def load(cls) -> "ApplicationConfig":
        return cls(
            database_path=os.environ.get("DATABASE_PATH", "data/app.db"),
            database_url=os.environ.get("DATABASE_URL"),
            secret_key=os.environ.get("SECRET_KEY"),
        )

    def as_flask_config(self) -> dict[str, object]:
        return {
            "DATABASE_PATH": self.database_path,
            "DATABASE_URL": self.database_url,
            "SECRET_KEY": self.secret_key,
            "TESTING": False,
        }
