# Evidence: Block 2 · Foundational (block-2)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 13887
- execution id: 20261023.175049.857Z-ba4d9a18

## Stories built
- Declare the books table and its repository operations. (database) [story]
- Provide the Flask application factory, shared page layout, and web_client test fixture. (app-shell) [story]

## Acceptance tooling authorization
- FEATURE-AppShell.md#appshell-factory: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-AppShell.md#appshell-client: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-AppShell.md#appshell-health: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-AppShell.md#appshell-unknown-route: python-package=flask; scope=test; authorization=existing Target environment

## Reusable compacts
- DATABASE_compact.md

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 895)
- implements: DATABASE.md (SP 2304)
- context: ARCHITECTURE_compact.md (SP 424)
- stack: persistence.md (SP 4315)
- stack: sqlite.md (SP 3027)
- implements: FEATURE-AppShell.md (SP 1076)
- context: DATABASE.md (SP 2304)
- stack: flask.md (SP 691)

## Build directory changes
- app_server/__init__.py
- app_server/config.py
- app_server/routes/__init__.py
- app_server/routes/pages.py
- app_server/templates/base.html
- app_server/testing.py
- tests/conftest.py
- tests/test_app_shell.py
- tests/test_books_persistence.py

## Pre-build acceptance observation
- RED: books-create (DATABASE.md)
  intent: books.create stores a book and returns the declared Output row carrying the supplied title and author.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.
- RED: books-get (DATABASE.md)
  intent: books.get reads back a created book by id with the stored title and author.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.
- RED: books-list (DATABASE.md)
  intent: books.list returns books in the order they were added.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.
- RED: books-delete (DATABASE.md)
  intent: books.delete removes a book so it no longer appears in the next list read, and leaves other books in place.
  error: foundation not built: `persistence` is the package the database foundation (postgres.md, sqlite.md) builds, and the build directory has no `persistence/`. The criterion exercises the built application, so it was not run.
- RED: appshell-factory (FEATURE-AppShell.md)
  intent: create_app returns a Flask application.
  error: foundation not built: `app_server` is the package the web-server foundation (django.md, fastapi.md, flask.md) builds, and the build directory has no `app_server/`. The criterion exercises the built application, so it was not run.
- RED: appshell-client (FEATURE-AppShell.md)
  intent: web_client returns a usable test client for a testing-mode app.
  error: foundation not built: `app_server` is the package the web-server foundation (django.md, fastapi.md, flask.md) builds, and the build directory has no `app_server/`. The criterion exercises the built application, so it was not run.
- RED: appshell-health (FEATURE-AppShell.md)
  intent: GET /health is reachable and answers 200 with a JSON body.
  error: foundation not built: `app_server` is the package the web-server foundation (django.md, fastapi.md, flask.md) builds, and the build directory has no `app_server/`. The criterion exercises the built application, so it was not run.
- RED: appshell-unknown-route (FEATURE-AppShell.md)
  intent: A path no feature declares is absent and answers 404.
  error: foundation not built: `app_server` is the package the web-server foundation (django.md, fastapi.md, flask.md) builds, and the build directory has no `app_server/`. The criterion exercises the built application, so it was not run.

## Post-build programmatic acceptance
- PASS: books-create (DATABASE.md)
  intent: books.create stores a book and returns the declared Output row carrying the supplied title and author.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: books-get (DATABASE.md)
  intent: books.get reads back a created book by id with the stored title and author.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: books-list (DATABASE.md)
  intent: books.list returns books in the order they were added.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: books-delete (DATABASE.md)
  intent: books.delete removes a book so it no longer appears in the next list read, and leaves other books in place.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: appshell-factory (FEATURE-AppShell.md)
  intent: create_app returns a Flask application.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: appshell-client (FEATURE-AppShell.md)
  intent: web_client returns a usable test client for a testing-mode app.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: appshell-health (FEATURE-AppShell.md)
  intent: GET /health is reachable and answers 200 with a JSON body.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: appshell-unknown-route (FEATURE-AppShell.md)
  intent: A path no feature declares is absent and answers 404.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
The DATABASE layer is already generated on disk (`persistence/`, `schema.sql`), so this block's work is the app shell plus callers-free wiring. Let me check the toolchain and existing test run before writing anything.The venv works (Flask 3.1.3, pytest 9.1.1) and the existing 8 foundation tests pass. Plan for this block:

- **database story:** the `persistence/` package and `schema.sql` are Drydock-generated and already on disk, so I write no persistence code. I'll add tests that prove the declared `books` operations through `db_session`.
- **app-shell story:** `app_server` factory, typed `Config`, `/health` blueprint, `base.html`, `testing.web_client()`, and the `conftest.py` fixtures.

Writing the app shell first.Now the fixtures. The existing `conftest.py` must be read before I edit it.I referenced `Iterator` without importing it; fixing that now.Now the tests. Each one acts on the system and reads the result back through a public interface, with no stdout scraping.The `web_client` import in `test_app_shell.py` shares a name with the fixture parameter, which is confusing to read. I'll alias it, then run the suite.All 25 pass (17 new plus the 8 foundation checks). Before I report, I'll confirm the rollback fixture left the store empty of test rows and check the working-tree changes.<reusable-compact filename="DATABASE.md">
Store: SQLite via generated `persistence` (DSN: DATABASE_URL > DATABASE_PATH > data/app.db). Schema applied only at DATABASE step, never at startup.
Table `books`: id INTEGER PK autoincrement (ascending id = order added); title TEXT NOT NULL; author TEXT NOT NULL.
Ops (`db.books.<verb>`):
- create(title, author) -> Book(id, title, author)
- get(id) -> Book | None
- list() -> list[Book], ordered id ASC
- delete(id) -> DeletedBook(id)
Row type: frozen dataclass `persistence.schema.Book`. Fixtures: `persistence.testing.db_session()` (rollback), `committed_session()`.
Guardrails: only `persistence/` touches the store; callers use `db.books.<verb>`; books ordered id ASC only.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- app_server/__init__.py
- app_server/config.py
- app_server/testing.py
- app_server/routes/__init__.py
- app_server/routes/pages.py
- app_server/templates/base.html
- tests/conftest.py
- tests/test_app_shell.py
- tests/test_books_persistence.py

SUMMARY:
- **database story:** No persistence code written. The generated `persistence/` package and `schema.sql` were already on disk from Drydock, and I left them untouched. `tests/test_books_persistence.py` (7 tests) exercises `books.create/get/list/delete` through the rollback `db_session` fixture. It mirrors the four DATABASE.md acceptance assertions and adds boundary cases (distinct ids, `get` returns None after delete, create visible within the transaction).
- **app-shell story:**
  - `create_app()` loads a typed `Config`, opens the store with `open_database`, stores the handle in `app.extensions["db"]`, and registers only the health blueprint. It applies no schema.
  - `app_server/config.py` is the only environment reader; it resolves DATABASE_URL > DATABASE_PATH > `data/app.db`.
  - `GET /health` returns 200 with `{"status": "ok"}` (in `routes/pages.py`).
  - `base.html` has a title block, a content block, minimal CSS, and no JavaScript.
  - `testing.web_client()` returns a testing-mode test client.
  - `tests/test_app_shell.py` (10 tests) covers the four appshell acceptance assertions plus the route-set boundary, template title rendering, and config precedence.
- **Choices I made:**
  - I added a `db_session` fixture to `tests/conftest.py` alongside `web_client`, because ARCHITECTURE.md lists both. The story text only names `web_client`.
  - `Config` lives in `app_server/config.py`, and the health route lives in `routes/pages.py`.
- **Test results:** `.venv/bin/python -m pytest -q` from the application root reports 25 passed (8 foundation, 10 app shell, 7 books). The books tests leave `data/app.db` with 0 rows, so the rollback isolation holds.
- **Not done in this block:** `bin/test.sh` does not exist yet, so `sources/full_test.sh` will exit 1 until a later story creates it. That is outside this block's scope.

BLOCKERS:
- None for this block.
