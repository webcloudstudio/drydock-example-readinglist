# Evidence: Block 2 · Foundational (block-2)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 6682
- execution id: 20260815.172122.438Z-4ffea838

## Stories built
- Establish SQLite persistence for ordered books. (database) [story]

## Reusable compacts
- DATABASE_compact.md

## Stacked context
- compass: COMPASS.md (SP 724)
- implements: DATABASE.md (SP 1129)
- stack: persistence.md (SP 2353)
- stack: sqlite_compact.md (SP 876)
- stack: python_compact.md (SP 1534)

## Build directory changes
- app/__init__.py
- app/persistence.py
- app/routes.py
- tests/test_persistence.py

## Pre-build acceptance observation
- RED: database-add-readback (DATABASE.md)
  intent: A book added through the persistence interface can be read back with the submitted fields.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "database-add-readback.py", line 2, in <module>
        from app.persistence import get_book_store
    ImportError: cannot import name 'get_book_store' from 'app.persistence' (/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/app/persistence.py)
- RED: database-order (DATABASE.md)
  intent: Ordered reads preserve the order in which books were added.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "database-order.py", line 2, in <module>
        from app.persistence import get_book_store
    ImportError: cannot import name 'get_book_store' from 'app.persistence' (/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/app/persistence.py)
- RED: database-remove (DATABASE.md)
  intent: Removing an existing book makes it absent from a subsequent persistence read.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "database-remove.py", line 2, in <module>
        from app.persistence import get_book_store
    ImportError: cannot import name 'get_book_store' from 'app.persistence' (/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/app/persistence.py)
- RED: database-empty (DATABASE.md)
  intent: A new database returns an empty ordered collection.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "database-empty.py", line 2, in <module>
        from app.persistence import get_book_store
    ImportError: cannot import name 'get_book_store' from 'app.persistence' (/mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/app/persistence.py)

## Post-build programmatic acceptance
- PASS: database-add-readback (DATABASE.md)
  intent: A book added through the persistence interface can be read back with the submitted fields.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: database-order (DATABASE.md)
  intent: Ordered reads preserve the order in which books were added.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: database-remove (DATABASE.md)
  intent: Removing an existing book makes it absent from a subsequent persistence read.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: database-empty (DATABASE.md)
  intent: A new database returns an empty ordered collection.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
<reusable-compact filename="DATABASE.md">
SQLite `books` persistence via `app.persistence.get_book_store()`:
- `BookStore.add(title, author) -> Book`
- `BookStore.list_ordered() -> list[Book]`
- `BookStore.remove(book_id) -> bool`
- Schema: `id`, required `title`, required `author`, `created_at`; insertion order follows ascending SQLite primary key.
- Initialization is idempotent and preserves rows.
- SQLite access remains encapsulated; connections are scoped to Flask application contexts.
- Empty titles/authors are rejected and never stored.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- app/__init__.py
- app/persistence.py
- app/routes.py
- tests/test_persistence.py

SUMMARY:
Implemented SQLite book persistence with add, ordered listing, removal, validation, idempotent initialization, and context-scoped connections. Added coverage for all acceptance criteria and edge cases. `sh bin/test.sh`: 14 passed. Ruff checks passed.

BLOCKERS:
- None
