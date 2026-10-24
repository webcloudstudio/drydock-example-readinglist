<!-- Compacted from DATABASE.md sha256=ba3f2fb135480b34230597f018171e86cdb4992a5e13d7aed20ccb12d8eb8581 on 2026-10-23 by drydock build agent -->

Store: SQLite via generated `persistence` (DSN: DATABASE_URL > DATABASE_PATH > data/app.db). Schema applied only at DATABASE step, never at startup.
Table `books`: id INTEGER PK autoincrement (ascending id = order added); title TEXT NOT NULL; author TEXT NOT NULL.
Ops (`db.books.<verb>`):
- create(title, author) -> Book(id, title, author)
- get(id) -> Book | None
- list() -> list[Book], ordered id ASC
- delete(id) -> DeletedBook(id)
Row type: frozen dataclass `persistence.schema.Book`. Fixtures: `persistence.testing.db_session()` (rollback), `committed_session()`.
Guardrails: only `persistence/` touches the store; callers use `db.books.<verb>`; books ordered id ASC only.
