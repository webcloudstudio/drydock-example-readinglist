<!-- Compacted from DATABASE.md sha256=0bab0628f6130ff0e1c840409170226b73ac94f3a474ecee669f2d01577bbbd7 on 2026-10-23 by drydock build agent -->

Persistence provides `persistence.books` with:

- `list()` → ordered `BookRow[]`
- `create(title, author, insertion_order)` → `BookRow`
- `delete(id)` → `DeletedBook`

Books require non-empty title/author, retain insertion order, and use generated persistence only. Schema: `books(id, title, author, insertion_order UNIQUE)`.
