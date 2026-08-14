# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-08-14
- resulting state: closed/verified
- story points (combined assembled cost): 11551
- execution id: 20260814.140029.546Z-0bfa5e02

## Stories built
- Establish the ReadingList application architecture and web entry point. (architecture) [story]

## Reusable compacts
- ARCHITECTURE_compact.md

## Stacked context
- compass: COMPASS.md (SP 729)
- implements: ARCHITECTURE.md (SP 865)
- stack: python.md (SP 3892)
- stack: flask.md (SP 4232)
- stack: sqlite.md (SP 1763)

## Build directory changes
- app/__init__.py
- app/database.py
- app/routes.py
- app/static/style.css
- app/templates/reading_list.html
- bin/test.sh
- instance/reading_list.sqlite3
- pyproject.toml
- run.py
- tests/conftest.py
- tests/test_architecture.py

## Pre-build acceptance observation
- RED: architecture-factory (ARCHITECTURE.md)
  intent: The application exposes an isolated Flask application factory and a usable test client.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-factory.py", line 1, in <module>
        from app import create_app
    ModuleNotFoundError: No module named 'app'
- RED: architecture-isolation (ARCHITECTURE.md)
  intent: Separate factory calls produce independently configurable application instances.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-isolation.py", line 1, in <module>
        from app import create_app
    ModuleNotFoundError: No module named 'app'
- RED: architecture-entry-point (ARCHITECTURE.md)
  intent: The factory-created application has a registered root entry point.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-entry-point.py", line 1, in <module>
        from app import create_app
    ModuleNotFoundError: No module named 'app'

## Post-build programmatic acceptance
- UNVERIFIED: architecture-factory (ARCHITECTURE.md)
  intent: The application exposes an isolated Flask application factory and a usable test client.
  provisioning: not required
  error: unverified acceptance: acceptance environment unavailable: Target Python project has no .venv
- UNVERIFIED: architecture-isolation (ARCHITECTURE.md)
  intent: Separate factory calls produce independently configurable application instances.
  provisioning: not required
  error: unverified acceptance: acceptance environment unavailable: Target Python project has no .venv
- UNVERIFIED: architecture-entry-point (ARCHITECTURE.md)
  intent: The factory-created application has a registered root entry point.
  provisioning: not required
  error: unverified acceptance: acceptance environment unavailable: Target Python project has no .venv

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
- `create_app(test_config: dict[str, Any] | None) -> Flask` returns an isolated Flask app; optional config must support `TESTING` and `READING_LIST_DATABASE`.
- `app.routes` owns HTTP routes; `app.database` owns SQLite access. Routes must not access SQLite directly.
- Root route: `GET /`, rendering the current reading-list collection.
- Persistence uses SQLite; application is runnable from the project root via `run.py`.
- `bin/test.sh` runs the complete pytest suite.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- app/__init__.py
- app/database.py
- app/routes.py
- app/templates/reading_list.html
- app/static/style.css
- tests/conftest.py
- tests/test_architecture.py
- bin/test.sh
- run.py
- pyproject.toml

SUMMARY:
Implemented the isolated Flask application factory, SQLite persistence boundary, root web entry point, template, test suite, and POSIX test command. All 4 tests and declared acceptance assertions pass.

BLOCKERS:
- None
