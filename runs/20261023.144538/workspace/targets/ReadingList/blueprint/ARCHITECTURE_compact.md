<!-- Compacted from ARCHITECTURE.md sha256=64951a517fa03e92d5fbc2753f072d3a1dbea94a3337305d0f5655584717a101 on 2026-10-23 by drydock build agent -->

Package app_server: create_app() -> Flask (no routes yet). app_server.testing.web_client() -> FlaskClient with TESTING=True, fresh app per call.
Project root: pyproject.toml, uv.lock, tests/conftest.py (fixtures web_client, db_session). Runner: pytest -q from root. Launcher: bin/run.sh.
Routes per ARCHITECTURE: GET / ; GET /books ; POST /books ; POST /books/{id}/delete. Success form posts 303 to /; rejection 400; unknown id 404.
Persistence: generated persistence package only; open_database(dsn), db.books.{create,list,get,delete}; db_session() context manager for acceptance.
