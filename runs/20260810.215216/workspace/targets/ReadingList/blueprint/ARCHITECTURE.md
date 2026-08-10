# ARCHITECTURE: ReadingList

| Field       | Value |
|-------------|-------|
| Version     | 20260810 V1 |
| Description | Defines the Flask application boundary and module ownership for ReadingList. |
| Depends On  | — |
| Provides    | Flask application factory, GET /, GET /books, POST /books, POST /books/{id}/remove |
| Consumes    | — |

## Application Boundary

ReadingList is a local Flask web application. The application factory creates an isolated application instance and configures the local SQLite persistence location.

The application exposes the reading-list screen and book workflows through Flask routes. Reader data remains inside the application and is never transmitted to third-party services.

## Module Ownership

| Concern | Owner | Boundary |
|---|---|---|
| Application creation and configuration | `app.py` | Flask application factory |
| HTTP route dispatch | `routes.py` | Flask route handlers |
| Persistence | `persistence.py` | SQLite access through the book persistence interface |
| Validation | `validation.py` | Submission validation before persistence |
| Rendering | `templates/` | HTML presentation |
| Automated tests | `tests/` | pytest suite launched by `bin/test.sh` |

Application routes do not access SQLite directly. Persistence operations pass through the documented database interface.

## Technology Stack

| Technology | Use |
|---|---|
| Python | Application and test implementation |
| Flask | Local web application and HTTP routing |
| SQLite | Local book persistence |
| pytest | Automated test execution |
| HTML/CSS | Browser interface |

## Programmatic Acceptance

### application-factory
The application factory creates a testable Flask application.

Requires: python-package=flask; scope=test

```python
from app import create_app

app = create_app({"TESTING": True})
assert app is not None
assert app.test_client() is not None
```

### root-route
The application boundary exposes the reading-list entry route.

```python
from app import create_app

client = create_app({"TESTING": True}).test_client()
response = client.get("/")
assert response.status_code == 200
```

### local-boundary
The application can be configured with a local database path.

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    database = Path(directory) / "reading-list.sqlite3"
    app = create_app({"TESTING": True, "DATABASE": str(database)})
    response = app.test_client().get("/")
    assert response.status_code == 200
```

## User Acceptance

- A reader can use the application locally without an external service.

## Guardrails

- Reader lists never leave the application.
- Route handlers do not access SQLite outside the persistence boundary.
