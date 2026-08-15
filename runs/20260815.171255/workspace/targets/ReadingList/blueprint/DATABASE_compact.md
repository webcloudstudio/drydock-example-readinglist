<!-- Compacted from DATABASE.md sha256=78e782f3b44cbf8f06bf8af3062dfbc659139e71f0edda468bbe62514cb03467 on 2026-08-15 by drydock build agent -->

SQLite `books` persistence via `app.persistence.get_book_store()`:
- `BookStore.add(title, author) -> Book`
- `BookStore.list_ordered() -> list[Book]`
- `BookStore.remove(book_id) -> bool`
- Schema: `id`, required `title`, required `author`, `created_at`; insertion order follows ascending SQLite primary key.
- Initialization is idempotent and preserves rows.
- SQLite access remains encapsulated; connections are scoped to Flask application contexts.
- Empty titles/authors are rejected and never stored.
