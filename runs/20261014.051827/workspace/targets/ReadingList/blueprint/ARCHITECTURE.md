# ARCHITECTURE: Reading List

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Application factory, test client, and project layout for the reading list web application. |
| Depends On  | COMPASS.md |
| Provides    | create_app, app_server.testing.web_client |
| Consumes    | |

## Project Layout

- `pyproject.toml` with committed `uv.lock`; the environment is `.venv`, created by `uv venv`.
- `app_server/__init__.py` exposes `create_app() -> Flask`.
- `app_server/testing.py` exposes `web_client()`, which returns a Flask test client with `TESTING` enabled.
- `bin/test.sh` at the application root, written by the terminal story.

## Technology Stack

- Python: implementation language, governed by `python.md`.
- Flask: web framework, governed by `flask.md`.
- SQLite: local persistence through the generated `persistence` package, governed by `sqlite.md`.
- pytest: test runner for the automated suite.
- HTML/CSS: browser interface, styling unspecified.

## Module Ownership

| Boundary | Owner | Notes |
|----------|-------|-------|
| Application factory | `app_server` | Registers blueprints and error handlers added by later stories. |
| Persistence | `persistence` | Generated from `DATABASE.md`; callers reach it only through services. |
| Routes | `app_server` feature modules | Call `db.books.<verb>(...)` and never open a connection. |

## Foundation Contract

- package: app_server
- entry: create_app() -> Flask
- fixture: web_client
- fixture_source: app_server/testing.py

`create_app()` registers no routes of its own. It wires only the blueprints and error handlers that feature stories contribute.

## Programmatic Acceptance

=== AC architecture-create-app ===
Intent: create_app returns a Flask application instance.

from flask import Flask
from app_server import create_app

app = create_app()
assert isinstance(app, Flask)
=== END AC architecture-create-app ===

=== AC architecture-web-client-testing ===
Intent: web_client returns a test client whose application has TESTING enabled.

from app_server.testing import web_client

client = web_client()
assert client.application.config["TESTING"] is True
=== END AC architecture-web-client-testing ===

=== AC architecture-web-client-unregistered ===
Intent: web_client answers a path no story registers with 404.

from app_server.testing import web_client

client = web_client()
response = client.get("/unregistered-probe-path")
assert response.status_code == 404
=== END AC architecture-web-client-unregistered ===

## User Acceptance

- None.

## Guardrails

- The application factory must not register routes that no feature story declares.
- No module outside `persistence` may import `sqlite3`.
