"""Typed runtime settings. This module is the only reader of the process environment."""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass

DEFAULT_DATABASE_PATH = "data/app.db"


@dataclass(frozen=True)
class Config:
    """Settings resolved once at startup. DATABASE_URL overrides DATABASE_PATH."""

    database_dsn: str

    @classmethod
    def load(cls, environ: Mapping[str, str] | None = None) -> "Config":
        env = os.environ if environ is None else environ
        dsn = env.get("DATABASE_URL") or env.get("DATABASE_PATH") or DEFAULT_DATABASE_PATH
        return cls(database_dsn=dsn)
