# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-08-10
- resulting state: closed/verified
- story points (combined assembled cost): 15215
- execution id: 20260810.215639.267Z-d006af83

## Stories built
- Define the Flask application boundary and module ownership. (architecture) [story]
- Define local SQLite persistence for books. (database) [story]
- Define shared interaction patterns for the reading-list interface. (ui-general) [story]

## Acceptance tooling authorization
- ARCHITECTURE.md#application-factory: python-package=flask; scope=test; authorization=Commander technology stack

## Reusable compacts
- ARCHITECTURE_compact.md
- DATABASE_compact.md
- UI-GENERAL_compact.md

## Stacked context
- compass: COMPASS.md (SP 685)
- implements: ARCHITECTURE.md (SP 695)
- context: TECHNOLOGY_STACK.md (SP 247)
- stack: python.md (SP 3892)
- stack: flask.md (SP 4232)
- implements: DATABASE.md (SP 798)
- stack: persistence.md (SP 2353)
- stack: sqlite.md (SP 1763)
- implements: UI-GENERAL.md (SP 378)

## Build directory changes
- app.py
- bin/test.sh
- persistence.py
- pyproject.toml
- routes.py
- run.py
- runs/20260810.215216/build/ReadingList/requirements.txt
- templates/base.html
- templates/books.html
- tests/conftest.py
- tests/test_acceptance.py
- validation.py

## Pre-build acceptance observation
- RED: application-factory (ARCHITECTURE.md)
  intent: The application factory creates a testable Flask application.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: root-route (ARCHITECTURE.md)
  intent: The application boundary exposes the reading-list entry route.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: local-boundary (ARCHITECTURE.md)
  intent: The application can be configured with a local database path.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: persistence-interface (DATABASE.md)
  intent: The persistence boundary stores and reads a book through its public interface.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: insertion-order (DATABASE.md)
  intent: The persistence interface returns books in insertion order.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: removal (DATABASE.md)
  intent: Removing a stored book makes it absent from a subsequent read.
  error: baseline unavailable: authorized Target tooling is not provisioned

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
Flask factory via `app.create_app(config)`. Routes: `GET /`, `GET /books`, `POST /books`, `POST /books/{id}/remove`. Persistence belongs in `persistence.py`; validation in `validation.py`; rendering in `templates/`; tests in `tests/`. Local-only execution; no third-party transmission.
</reusable-compact>

<reusable-compact filename="DATABASE.md">
`BookStore` exposes `add(title, author)`, `list()`, and `remove(book_id)`. SQLite database defaults to `instance-reading-list.sqlite3`, with configurable test paths. `books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL)`. Listing orders by ascending `id`; startup creates the table.
</reusable-compact>

<reusable-compact filename="UI-GENERAL.md">
Reading-list page includes heading, labeled title/author form, submit control, ordered book list, per-book remove controls, and an empty-state message. Validation errors appear near the form and submitted values are retained.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- app.py
- persistence.py
- validation.py
- routes.py
- templates/base.html
- templates/books.html
- tests/conftest.py
- tests/test_acceptance.py
- bin/test.sh
- run.py
- pyproject.toml
- pytest.ini

SUMMARY:
Implemented the Flask application factory, local SQLite `BookStore`, validated add/list/remove workflows, shared reading-list UI, and automated acceptance tests. `sh bin/test.sh` passes all 8 tests; Ruff checks and formatting pass.

BLOCKERS:
- None
