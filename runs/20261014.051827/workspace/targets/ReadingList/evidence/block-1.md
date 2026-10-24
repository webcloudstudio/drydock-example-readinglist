# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 10146
- execution id: 20261014.052142.874Z-07926177

## Stories built
- Stand up the Python project tree, environment, test runner, and Flask application factory. (architecture-foundation) [story]
- Declare the reading-list store and generate the persistence package from DATABASE.md. (persistence-foundation) [story]

## Reusable compacts
- ARCHITECTURE_compact.md
- DATABASE_compact.md

## Stacked context
- compass: COMPASS.md (SP 833)
- implements: ARCHITECTURE.md (SP 1043)
- stack: python.md (SP 600)
- stack: flask.md (SP 678)
- implements: DATABASE.md (SP 1025)
- stack: persistence.md (SP 3535)
- stack: sqlite.md (SP 2194)

## Build directory changes
- .gitignore
- app_server/__init__.py
- app_server/testing.py
- pyproject.toml
- tests/conftest.py
- tests/test_app_factory.py
- tests/test_persistence.py
- tests/test_web_client.py
- uv.lock

## Pre-build acceptance observation
- RED: architecture-create-app (ARCHITECTURE.md)
  intent: create_app returns a Flask application instance.
  error: foundation not built: `app_server` is the package the web-server foundation (django.md, fastapi.md, flask.md) builds, and the build directory has no `app_server/`. The criterion exercises the built application, so it was not run.
- RED: architecture-web-client-testing (ARCHITECTURE.md)
  intent: web_client returns a test client whose application has TESTING enabled.
  error: foundation not built: `app_server` is the package the web-server foundation (django.md, fastapi.md, flask.md) builds, and the build directory has no `app_server/`. The criterion exercises the built application, so it was not run.
- RED: architecture-web-client-unregistered (ARCHITECTURE.md)
  intent: web_client answers a path no story registers with 404.
  error: foundation not built: `app_server` is the package the web-server foundation (django.md, fastapi.md, flask.md) builds, and the build directory has no `app_server/`. The criterion exercises the built application, so it was not run.

## Post-build programmatic acceptance
- PASS: architecture-create-app (ARCHITECTURE.md)
  intent: create_app returns a Flask application instance.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: architecture-web-client-testing (ARCHITECTURE.md)
  intent: web_client returns a test client whose application has TESTING enabled.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: architecture-web-client-unregistered (ARCHITECTURE.md)
  intent: web_client answers a path no story registers with 404.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
The persistence package and `schema.sql` are already on disk and committed, so this step only needs the project tree, the Flask factory, and tests. I'll set up the environment first, then verify the package names through `uv` resolution.Dependencies resolved through `uv` from PyPI. Before writing tests against the persistence layer, I need the rest of `Database.run` so the assertions match its real return values.I have what I need. Writing the application factory, the test client helper, and the tests. The `.gitignore` keeps `.venv/` out of Git per the Python stack rules.One test I just wrote locks in the wrong behavior: it asserts an empty title is accepted, which contradicts the COMPASS guardrail. I'm removing it, and moving the inline import to the top of the file.Now running the suite through the project environment, plus the three declared acceptance assertions exactly as written in ARCHITECTURE.md.All 16 tests pass and the three declared assertions pass. Checking the working tree for stray residue and confirming the new files are the only changes.<reusable-compact filename="ARCHITECTURE.md">
Project: pyproject.toml + committed uv.lock; env .venv via `uv venv`; python >=3.11.
Package app_server:
- create_app() -> Flask. Registers no feature routes; feature stories add blueprints/error handlers.
- app_server.testing.web_client() -> FlaskClient for a fresh app with TESTING=True.
- Unregistered paths answer 404.
Stack: Python (python.md), Flask (flask.md), SQLite via generated `persistence` (sqlite.md), pytest.
Guardrails: no feature routes registered in the factory; no module outside `persistence` imports sqlite3.
</reusable-compact>

<reusable-compact filename="DATABASE.md">
Table books: id INTEGER PK (autoincrement; list order ascending id), title TEXT NOT NULL, author TEXT NOT NULL.
Operations (persistence.open_database(dsn) -> Database; db.books.<verb>(...)):
- books.create(title, author) -> new id (title/author non-empty after trim, per Blueprint).
- books.list() -> list[Book] in ascending id order.
- books.get(id) -> Book | None.
- books.delete(id) -> rows removed (0 or 1).
Book row: id, title, author. Undeclared verbs (e.g. update) raise UnknownOperation.
Guardrail: no empty title or author stored; callers write no SQL.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- .gitignore
- pyproject.toml
- uv.lock
- app_server/__init__.py
- app_server/testing.py
- tests/conftest.py
- tests/test_app_factory.py
- tests/test_web_client.py
- tests/test_persistence.py

SUMMARY:
- **Project tree and environment:** `pyproject.toml` declares Python >=3.11, `flask` as a runtime dependency and `pytest` as a dev dependency. Both were added with `uv add`, which resolved them from PyPI, and `uv.lock` is committed-ready. The environment is `.venv`, created with `uv venv` and ignored by `.gitignore`.
- **Application factory:** `app_server/__init__.py` exposes `create_app() -> Flask` and registers no feature routes.
- **Test client:** `app_server/testing.py` exposes `web_client()` exactly as the Foundation Contract shows.
- **Persistence:** the `persistence/` package and `schema.sql` were already on disk and committed. I did not modify them. The persistence tests exercise the declared `books` operations through `db_session()`.
- **Test runner:** `pytest` is configured in `pyproject.toml` with `pythonpath = ["."]`. `tests/conftest.py` provides the `web_client` fixture, which delegates to the helper, and the `db_session` fixture, which uses a fresh temporary store per test.
- **Verification:** `uv run pytest` gives 16 passed, exit 0. The three declared ARCHITECTURE.md acceptance assertions (`architecture-create-app`, `architecture-web-client-testing`, `architecture-web-client-unregistered`) each pass when run as written.
- **Judgment calls:**
  - I added `.gitignore` for `.venv/`, `__pycache__/`, and `data/` so the environment and runtime database stay out of Git.
  - I did not write `bin/test.sh`. ARCHITECTURE.md assigns it to the terminal story, not this block.
  - I did not run `sources/full_test.sh`. None of this block's acceptance criteria invoke it.
  - I left the existing `data/app.db` untouched.
- **Test coverage:** the tests cover the factory's return type, instance isolation, the single static route, and the TESTING default. They also cover the test client's TESTING flag and 404 path, plus the store's create, get, list ordering, delete, absent-id, undeclared-verb, and per-session isolation behavior.
