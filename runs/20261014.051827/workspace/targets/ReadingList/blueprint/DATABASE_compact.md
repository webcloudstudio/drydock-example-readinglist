<!-- Compacted from DATABASE.md sha256=6e75da4739c7c041d1f9831eaa86fae8c13b9e5e592b277c9d9dd0cf188eb3bb on 2026-10-14 by drydock build agent -->

Table books: id INTEGER PK (autoincrement; list order ascending id), title TEXT NOT NULL, author TEXT NOT NULL.
Operations (persistence.open_database(dsn) -> Database; db.books.<verb>(...)):
- books.create(title, author) -> new id (title/author non-empty after trim, per Blueprint).
- books.list() -> list[Book] in ascending id order.
- books.get(id) -> Book | None.
- books.delete(id) -> rows removed (0 or 1).
Book row: id, title, author. Undeclared verbs (e.g. update) raise UnknownOperation.
Guardrail: no empty title or author stored; callers write no SQL.
