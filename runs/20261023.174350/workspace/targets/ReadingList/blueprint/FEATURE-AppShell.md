# FEATURE: App Shell

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Flask application factory, shared page layout, test client fixture, and health route. |
| Depends On | ARCHITECTURE.md, DATABASE.md |
| Provides | create_app, app_server.testing.web_client, GET /health |
| Consumes | None |

## Purpose

Provide the runnable Flask application that later features register routes on, plus the shared base template and the in-process test client used by acceptance and pytest.

## Trigger

A WSGI server or test harness calls `create_app()`.

## Sequence

1. `create_app()` builds a Flask app and resolves the database DSN (`DATABASE_URL`, then `DATABASE_PATH`, then `data/app.db`).
2. It opens the database with `open_database(dsn)` and keeps the handle for services.
3. It registers the book blueprints supplied by later stories; it invents no other routes.
4. `app_server.testing.web_client()` creates the app with `TESTING = True` and returns its test client.

## Routes

| Route | Behavior |
|-------|----------|
| `GET /health` | Returns 200 with a small JSON body `{"status": ...}`. |

## Layout

`app_server/templates/base.html` is the shared layout: page title block, content block, minimal inline or static CSS, no JavaScript.

## Reads

None.

## Writes

None.

## Database Interface

- None — persistence is owned by DATABASE.md.

## Programmatic Acceptance

=== AC appshell-factory ===
Intent: create_app returns a Flask application.
Requires: python-package=flask; scope=test

from flask import Flask
from app_server import create_app

app = create_app()
assert isinstance(app, Flask)
=== END AC appshell-factory ===

=== AC appshell-client ===
Intent: web_client returns a usable test client for a testing-mode app.
Requires: python-package=flask; scope=test

from app_server.testing import web_client

client = web_client()
assert client.application.config["TESTING"] is True
=== END AC appshell-client ===

=== AC appshell-health ===
Intent: GET /health is reachable and answers 200 with a JSON body.
Requires: python-package=flask; scope=test

from app_server.testing import web_client

client = web_client()
response = client.get("/health")
assert response.status_code == 200
assert isinstance(response.get_json(), dict)
=== END AC appshell-health ===

=== AC appshell-unknown-route ===
Intent: A path no feature declares is absent and answers 404.
Requires: python-package=flask; scope=test

from app_server.testing import web_client

client = web_client()
response = client.get("/route-nobody-declared")
assert response.status_code == 404
=== END AC appshell-unknown-route ===

## User Acceptance

- None.

## Guardrails

- The factory registers only routes declared by Blueprint features.
- The factory reaches the store only through `open_database`.
