# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 4028
- execution id: 20261023.174856.568Z-ce58b2b0

## Stories built
- Stand up the Python project tree, environment, dependency manifest, and pytest runner. (architecture) [story]

## Acceptance tooling authorization
- ARCHITECTURE.md#architecture-manifest: executable=python3; scope=test; authorization=existing Target environment
- ARCHITECTURE.md#architecture-pytest: python-package=pytest; scope=test; authorization=existing Target environment

## Reusable compacts
- ARCHITECTURE_compact.md

## Stacked context
- implements: python.md (SP 1166)
- compass: COMPASS.md (SP 895)
- implements: ARCHITECTURE.md (SP 1812)

## Build directory changes
- .gitignore
- pyproject.toml
- tests/conftest.py
- tests/test_project_foundation.py
- uv.lock

## Pre-build acceptance observation
- UNVERIFIED: architecture-manifest (ARCHITECTURE.md)
  intent: pyproject.toml parses and declares Flask and pytest as dependencies.
  return code: 1
  error: unverified acceptance: the assertion raised FileNotFoundError ([Errno 2] No such file or directory: 'pyproject.toml') in its own frame, before reaching the code under test. This is a fault in the acceptance kit or its environment, not a defect in the build.
  stderr:
    Traceback (most recent call last):
      File "architecture-manifest.py", line 4, in <module>
        with open(Path("pyproject.toml"), "rb") as handle:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'pyproject.toml'
- RED: architecture-tree (ARCHITECTURE.md)
  intent: The lockfile, tests directory, and conftest exist at the application root.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-tree.py", line 3, in <module>
        assert Path("uv.lock").is_file()
               ^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): architecture-pytest (ARCHITECTURE.md)
  intent: The pytest runner is installed and starts from the application root.
  return code: 0
  stdout:
    pytest 9.0.3

## Post-build programmatic acceptance
- PASS: architecture-manifest (ARCHITECTURE.md)
  intent: pyproject.toml parses and declares Flask and pytest as dependencies.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: uv sync --locked succeeded
  return code: 0
- PASS: architecture-tree (ARCHITECTURE.md)
  intent: The lockfile, tests directory, and conftest exist at the application root.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: uv sync --locked succeeded
  return code: 0
- PASS: architecture-pytest (ARCHITECTURE.md)
  intent: The pytest runner is installed and starts from the application root.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: uv sync --locked succeeded
  return code: 0
  stdout:
    pytest 9.1.1

## Build summary
The suite passes, but the Flask check uses a deprecated `__version__` attribute and `importorskip` could silently skip. I'll tighten that test.<reusable-compact filename="ARCHITECTURE.md">
Project: ReadingList (Flask, SQLite via generated `persistence`, pytest). Python >=3.11.
Layout: `pyproject.toml` + `uv.lock` (deps: flask>=3.1,<4; dev group: pytest>=9,<10); `.venv` via `uv venv`; `app_server/__init__.py` exposes `create_app() -> Flask`; `app_server/testing.py` exposes `web_client()`; `app_server/routes/{books.py,pages.py}`; `app_server/services/books.py` exposes `add_book`, `list_books`, `remove_book`, `validate_book_input`; `app_server/templates/`; `persistence/` generated from `DATABASE.md`; `tests/conftest.py` exposes `web_client` and `db_session` fixtures; `bin/test.sh` POSIX runner.
Rules: routes call services only; services call `db.<table>.<verb>(...)`; only `persistence` touches SQLite; books ordered by id ascending; rejected input -> 400; unknown book removal -> 404; server-rendered HTML forms, no client JS.
Config: `DATABASE_URL` > `DATABASE_PATH` > `data/app.db`.
Test command: `pytest -q` from application root.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- .gitignore
- pyproject.toml
- uv.lock
- tests/conftest.py
- tests/test_project_foundation.py

SUMMARY:
Stood up the Python foundation in the build directory:
- `pyproject.toml`: `requires-python >=3.11`; runtime dependency `flask>=3.1,<4`; dev group `pytest>=9,<10`; `[tool.uv] package = false`; `[tool.pytest.ini_options]` with `testpaths = ["tests"]` and `pythonpath = ["."]` so `pytest -q` runs from the application root.
- Package names verified on PyPI before adding (flask 3.1.3, pytest 9.1.1).
- `uv.lock` generated with `uv lock`; `.venv` created with `uv venv --python 3.12` and populated with `uv sync`. `.venv` is git-ignored.
- `tests/conftest.py`: session fixture `project_root`. The `web_client` and `db_session` fixtures are left for the app and persistence stories.
- `tests/test_project_foundation.py`: 8 tests that read the manifest, lockfile, and tests layout back from disk, check the Flask import and version, and check the interpreter version.
- `.gitignore`: `.venv/`, `__pycache__/`, `.pytest_cache/`, `.env`, `data/`.

Verification:
- `.venv/bin/python -m pytest -q`: 8 passed, exit 0.
- `.venv/bin/python -m pytest --version`: pytest 9.1.1, exit 0.
- The three `architecture-*` acceptance checks, run in-process: all pass.
- Choice: I did not create `app_server/`, `bin/test.sh`, or `.env.example`. Those belong to later stories. Because of that, `sources/full_test.sh` will report failure until `bin/test.sh` exists. That is expected for this block.
- `sources/` was not touched. Nothing was committed.

BLOCKERS:
- None for this block.
