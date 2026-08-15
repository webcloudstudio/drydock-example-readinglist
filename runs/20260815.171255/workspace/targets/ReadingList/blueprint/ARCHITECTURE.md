# ARCHITECTURE: ReadingList

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Defines the Flask application structure and module boundaries for the ReadingList web application. |
| Depends On  | — |
| Provides    | application_factory, web_entrypoint |
| Consumes    | — |

## Intent

ReadingList is a small Flask web application for maintaining an ordered personal list of books to read. The application uses one reader-facing workflow: submit a book, review the ordered list, and remove a book.

## Modules and Boundaries

| Module | Responsibility |
|---|---|
| `app/__init__.py` | Application factory and configuration initialization. |
| `app/routes.py` | HTTP route registration and request/response orchestration. |
| `app/persistence.py` | SQLite connection management and the typed book-store boundary. |
| `app/templates/` | Reader-facing HTML templates. |
| `app/static/` | Shared CSS presentation. |
| `tests/` | Automated behavior tests. |
| `bin/test.sh` | POSIX-compatible complete-suite launcher. |

The application factory creates an isolated Flask application, configures the database location, initializes the persistence boundary, and registers routes. Route handlers do not execute raw SQL. Persistence code does not render templates or make HTTP decisions.

## Technical Decisions

- Use a Flask application factory so tests can create isolated application instances.
- Use SQLite for local persistence.
- Preserve insertion order with an integer primary key and an ordered query.
- Keep the initial workflow on one screen at `/`.
- Use redirects after successful form mutations so the list is read again from persistence.

## Technology Stack

| Technology | Use |
|---|---|
| Python | Application and test implementation. |
| Flask | Web application, routing, templates, and test client. |
| SQLite | Local persistent storage for books. |
| pytest | Automated behavior test runner. |
| HTML/CSS | Reader-facing interface and shared presentation. |

## Module Ownership

| Boundary | Owning module | Allowed low-level access |
|---|---|---|
| Application configuration | Application factory | Flask configuration APIs and environment values. |
| Persistence | `app.persistence` | SQLite connections and SQL statements. |
| HTTP | `app.routes` | Flask request, response, redirect, and rendering APIs. |
| Presentation | Templates and static assets | HTML, template variables, and CSS only. |
| Verification | `tests/` and `bin/test.sh` | Test and process execution APIs. |

## Programmatic Acceptance

=== AC architecture-factory ===
Intent: The application factory creates a runnable Flask application with an HTTP test client.

from app import create_app

application = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = application.test_client()
response = client.get("/")
assert response.status_code == 200
=== END AC architecture-factory ===

=== AC architecture-isolation ===
Intent: Separate application instances can be created independently for isolated execution.

from app import create_app

first = create_app({"TESTING": True, "DATABASE": ":memory:"})
second = create_app({"TESTING": True, "DATABASE": ":memory:"})
assert first is not second
assert first.test_client().get("/").status_code == 200
assert second.test_client().get("/").status_code == 200
=== END AC architecture-isolation ===

=== AC architecture-entrypoint ===
Intent: The web entrypoint exposes the application factory without requiring a development server to start during import.

import importlib

module = importlib.import_module("app")
assert callable(module.create_app)
=== END AC architecture-entrypoint ===

## User Acceptance

- None.

## Guardrails

- Route handlers must not access SQLite directly.
- Persistence code must not reorder books.
- The application must remain runnable as a web application.
