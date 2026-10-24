<!-- Compacted from ARCHITECTURE.md sha256=6ffc16486a0aad1b27190c96896304f063205378eac5ea9b8ddf3ff1b7ae4b38 on 2026-10-14 by drydock build agent -->

Project: pyproject.toml + committed uv.lock; env .venv via `uv venv`; python >=3.11.
Package app_server:
- create_app() -> Flask. Registers no feature routes; feature stories add blueprints/error handlers.
- app_server.testing.web_client() -> FlaskClient for a fresh app with TESTING=True.
- Unregistered paths answer 404.
Stack: Python (python.md), Flask (flask.md), SQLite via generated `persistence` (sqlite.md), pytest.
Guardrails: no feature routes registered in the factory; no module outside `persistence` imports sqlite3.
