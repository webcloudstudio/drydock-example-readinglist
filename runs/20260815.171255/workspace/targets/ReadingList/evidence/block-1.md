# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 11649
- execution id: 20260815.171742.357Z-0c435543

## Stories built
- Establish the Flask application architecture and module boundaries. (architecture) [story]

## Reusable compacts
- ARCHITECTURE_compact.md

## Stacked context
- compass: COMPASS.md (SP 724)
- implements: ARCHITECTURE.md (SP 970)
- stack: python.md (SP 3892)
- stack: flask.md (SP 4232)
- stack: sqlite.md (SP 1763)

## Build directory changes
- .env.example
- .gitignore
- app/__init__.py
- app/persistence.py
- app/routes.py
- app/static/css/style.css
- app/templates/base.html
- app/templates/index.html
- bin/test.sh
- config.py
- pyproject.toml
- pytest.ini
- run.py
- tests/conftest.py
- tests/test_architecture.py
- tests/test_routes.py
- uv.lock

## Pre-build acceptance observation
- RED: architecture-factory (ARCHITECTURE.md)
  intent: The application factory creates a runnable Flask application with an HTTP test client.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-factory.py", line 1, in <module>
        from app import create_app
    ModuleNotFoundError: No module named 'app'
- RED: architecture-isolation (ARCHITECTURE.md)
  intent: Separate application instances can be created independently for isolated execution.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-isolation.py", line 1, in <module>
        from app import create_app
    ModuleNotFoundError: No module named 'app'
- RED: architecture-entrypoint (ARCHITECTURE.md)
  intent: The web entrypoint exposes the application factory without requiring a development server to start during import.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-entrypoint.py", line 3, in <module>
        module = importlib.import_module("app")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/importlib/__init__.py", line 90, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
      File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
      File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
    ModuleNotFoundError: No module named 'app'

## Post-build programmatic acceptance
- PASS: architecture-factory (ARCHITECTURE.md)
  intent: The application factory creates a runnable Flask application with an HTTP test client.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: architecture-isolation (ARCHITECTURE.md)
  intent: Separate application instances can be created independently for isolated execution.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: architecture-entrypoint (ARCHITECTURE.md)
  intent: The web entrypoint exposes the application factory without requiring a development server to start during import.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
Flask app factory: `from app import create_app`; supports isolated overrides including `TESTING` and `DATABASE`. HTTP routes live in `app.routes`; SQLite access is confined to typed `app.persistence`; templates/static assets live under `app/`; tests use pytest; `bin/test.sh` runs the complete suite. Root `/` must return 200, and independent app instances must not share state.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- .env.example
- .gitignore
- app/__init__.py
- app/persistence.py
- app/routes.py
- app/templates/base.html
- app/templates/index.html
- app/static/css/style.css
- bin/test.sh
- config.py
- pyproject.toml
- pytest.ini
- run.py
- tests/conftest.py
- tests/test_architecture.py
- tests/test_routes.py
- uv.lock

SUMMARY:
Implemented the Flask application factory, isolated SQLite persistence boundary, route registration, templates, configuration, tests, and POSIX test launcher. `sh bin/test.sh` passes all 5 tests; Ruff also passes.

BLOCKERS:
- None
