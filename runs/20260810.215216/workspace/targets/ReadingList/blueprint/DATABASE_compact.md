<!-- Compacted from DATABASE.md sha256=0d716a675aaa06fbc34d296dd5998a8014e445e3771c8db2765c9cd7b366308a on 2026-08-10 by drydock build agent -->

`BookStore` exposes `add(title, author)`, `list()`, and `remove(book_id)`. SQLite database defaults to `instance-reading-list.sqlite3`, with configurable test paths. `books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL)`. Listing orders by ascending `id`; startup creates the table.
