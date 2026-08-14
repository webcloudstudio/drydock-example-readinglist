# ARCHITECTURE: ReadingList

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Defines the Flask application structure, boundaries, and runtime entry point for ReadingList. |
| Depends On  | — |
| Provides    | application factory |
| Consumes    | — |

## Purpose

ReadingList is a small Flask web application for maintaining an ordered list of books and tracking read status.

## Application Structure

- `app/__init__.py` owns the application factory.
- `app/routes.py` owns HTTP route registration and request handling.
- `app/database.py` owns the persistence boundary.
- `templates/` owns server-rendered HTML.
- `static/` owns browser styling and assets.
- `tests/` owns automated behavior coverage.
- `bin/test.sh` is the root-level test command.

The application factory must accept optional test configuration and return an isolated Flask application instance. Runtime configuration must identify the SQLite database location. Route code may use the persistence interface but must not access SQLite connections or SQL statements directly.

## Route Ownership

Feature specifications own the following workflows:

- `POST /books` — create a valid book.
- `POST /books/{id}/read` — mark one book as read.
- `POST /books/{id}/delete` — remove one book.

The reading-list screen owns `GET /` and renders the current collection.

## Technology Stack

- Python provides the implementation language and test tooling.
- Flask provides the web application and test client.
- SQLite provides local persistence.
- pytest provides automated tests.
- HTML/CSS provides the browser interface.

## Module Ownership

| Boundary | Owner | Allowed low-level access |
|---|---|---|
| Application configuration | `app` | Flask configuration APIs |
| HTTP routing | `app.routes` | Flask request/response APIs and persistence interfaces |
| Persistence | `app.database` | SQLite APIs |
| Presentation | templates and static assets | HTML/CSS only |
| Verification | `tests` | Public application and persistence interfaces |

## Programmatic Acceptance

Requires: python-package=flask; scope=runtime

=== AC architecture-factory ===
Intent: The application exposes an isolated Flask application factory and a usable test client.
from app import create_app

app = create_app({"TESTING": True})
assert app is not None
client = app.test_client()
assert client is not None
assert app.config["TESTING"] is True
=== END AC architecture-factory ===

=== AC architecture-isolation ===
Intent: Separate factory calls produce independently configurable application instances.
from app import create_app

first = create_app({"TESTING": True, "READING_LIST_DATABASE": ":memory:"})
second = create_app({"TESTING": False, "READING_LIST_DATABASE": ":memory:"})

assert first is not second
assert first.config["TESTING"] is True
assert second.config["TESTING"] is False
=== END AC architecture-isolation ===

=== AC architecture-entry-point ===
Intent: The factory-created application has a registered root entry point.
from app import create_app

app = create_app({"TESTING": True})
routes = {rule.rule for rule in app.url_map.iter_rules()}
assert "/" in routes
=== END AC architecture-entry-point ===

## User Acceptance

- None.

## Guardrails

- Route handlers must not access raw SQLite details.
- The application must be runnable from the project root.
- Application instances must not depend on mutable global runtime state.
