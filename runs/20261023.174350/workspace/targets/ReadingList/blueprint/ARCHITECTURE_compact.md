<!-- Compacted from ARCHITECTURE.md sha256=513564d05020d87c4d59bcbd40b693fe2aae86fabff2f44b9c436731980f5168 on 2026-10-23 by drydock build agent -->

Project: ReadingList (Flask, SQLite via generated `persistence`, pytest). Python >=3.11.
Layout: `pyproject.toml` + `uv.lock` (deps: flask>=3.1,<4; dev group: pytest>=9,<10); `.venv` via `uv venv`; `app_server/__init__.py` exposes `create_app() -> Flask`; `app_server/testing.py` exposes `web_client()`; `app_server/routes/{books.py,pages.py}`; `app_server/services/books.py` exposes `add_book`, `list_books`, `remove_book`, `validate_book_input`; `app_server/templates/`; `persistence/` generated from `DATABASE.md`; `tests/conftest.py` exposes `web_client` and `db_session` fixtures; `bin/test.sh` POSIX runner.
Rules: routes call services only; services call `db.<table>.<verb>(...)`; only `persistence` touches SQLite; books ordered by id ascending; rejected input -> 400; unknown book removal -> 404; server-rendered HTML forms, no client JS.
Config: `DATABASE_URL` > `DATABASE_PATH` > `data/app.db`.
Test command: `pytest -q` from application root.
