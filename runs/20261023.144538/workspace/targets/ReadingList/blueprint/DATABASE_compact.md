<!-- Compacted from DATABASE.md sha256=0c992bebfe25d4b01148234e73a2399496f30823a0bd5058073fc5f205515438 on 2026-10-23 by drydock build agent -->

DATABASE.md (20261023 V1). Provides: books.create, books.list, books.get, books.delete.
Table books: id INTEGER PK (autoincrement; defines insertion order), title TEXT NOT NULL, author TEXT NOT NULL.
- FEATURE-BOOKS-001 books.create(title, author) -> BookRow(id, title, author). Write.
- FEATURE-BOOKS-002 books.list() -> BookRow[] ascending id. Read. Generated select has no ORDER BY; callers needing order must sort by id.
- FEATURE-BOOKS-003 books.get(id) -> BookRow. Read.
- FEATURE-BOOKS-004 books.delete(id) -> BookDeleteResult(id). Write.
Access only via persistence.open_database(dsn) and db.books.<op>. Criteria use persistence.testing.committed_session / db_session.
Guardrails: books listed in ascending id order; no caller reaches the store except through the persistence package.
