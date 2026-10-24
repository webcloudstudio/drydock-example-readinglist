# ARCHITECTURE: ReadingList

| Field       | Value |
|-------------|-------|
| Version     | 20261023 V1 |
| Description | Application structure and module boundaries for the ReadingList web application. |
| Depends On  | — |
| Provides    | `app_server.create_app`, `app_server.testing.web_client` |
| Consumes    | — |

## Application Structure

The application uses a Flask factory in `app_server.create_app`. Web routes are registered by the application factory. Feature modules handle request workflows and call the generated `persistence` package for storage.

## Module Ownership

| Boundary | Owner | Rule |
|----------|-------|------|
| Application factory | `app_server` | Creates and configures the Flask application. |
| Web routes | Feature modules | Translate HTTP requests into feature operations. |
| Persistence | Generated `persistence` package | Owns database connections, schema operations, and repository calls. |
| Configuration | `app_server` | Resolves application settings and database configuration. |
| Templates and styling | Interface layer | Renders the server-rendered reading-list screen. |
| External services | None | No external services are required. |

## Routes

| Method | Route | Owner |
|--------|-------|-------|
| GET | `/` | `FEATURE-READING-LIST.md` |
| POST | `/books` | `FEATURE-ADD-BOOK.md` and `FEATURE-VALIDATE-BOOK.md` |
| POST | `/books/<book_id>/delete` | `FEATURE-REMOVE-BOOK.md` |

## Technology Stack

| Technology | Use |
|------------|-----|
| Python | Application implementation and tests. |
| Flask | Web application factory, routing, and test client. |
| SQLite | Local relational persistence. |
| pytest | Automated test suite. |
| HTML/CSS | Server-rendered browser interface. |

## Technical Decisions

- The primary page is served at `/`.
- Book creation uses `POST /books`.
- Book removal uses `POST /books/<book_id>/delete`.
- Features access persistence only through generated repository operations.

## Programmatic Acceptance

=== AC architecture-factory ===
Intent: The application exposes the selected Flask factory and testing client contracts.

from flask import Flask
from app_server import create_app
from app_server.testing import web_client

app = create_app()
assert isinstance(app, Flask)
client = web_client()
assert client is not None
=== END AC architecture-factory ===

=== AC architecture-testing ===
Intent: The application factory can be created repeatedly for isolated automated tests.

from app_server import create_app

first = create_app()
second = create_app()
assert first is not second
assert first.name == second.name
=== END AC architecture-testing ===

## User Acceptance

- None.

## Guardrails

- Raw database access remains outside feature route modules.
- The application uses the declared Flask factory and testing-client contracts.
- The primary workflow remains reachable from `/`.
