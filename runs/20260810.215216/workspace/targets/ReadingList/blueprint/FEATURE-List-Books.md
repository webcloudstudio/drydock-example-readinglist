# FEATURE: List Books

| Field       | Value |
|-------------|-------|
| Version     | 20260810 V1 |
| Description | Retrieves the complete reading list in insertion order. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | GET /books |
| Consumes    | books persistence interface |

## Workflow

A reader requests `GET /books`. The workflow reads the complete collection through `BookStore.list` and returns the books in insertion order.

## Output

The route returns HTTP 200 and a JSON array of book records. An empty store returns an empty array.

## Programmatic Acceptance

### list-route
The list route is reachable and returns an empty collection for a new store.

Requires: python-package=flask; scope=test

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    app = create_app({"TESTING": True, "DATABASE": str(Path(directory) / "books.sqlite3")})
    response = app.test_client().get("/books")
    assert response.status_code == 200
    assert response.get_json() == []
```

### list-round-trip
The list route returns books persisted through the add workflow.

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    app = create_app({"TESTING": True, "DATABASE": str(Path(directory) / "books.sqlite3")})
    client = app.test_client()
    client.post("/books", data={"title": "One", "author": "A"})
    client.post("/books", data={"title": "Two", "author": "B"})
    books = client.get("/books").get_json()
    assert [book["title"] for book in books] == ["One", "Two"]
```

### list-preserves-order
The route preserves insertion order independently of request order.

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    app = create_app({"TESTING": True, "DATABASE": str(Path(directory) / "books.sqlite3")})
    store = app.extensions["book_store"]
    store.add("Alpha", "A")
    store.add("Beta", "B")
    response = app.test_client().get("/books")
    assert [book["title"] for book in response.get_json()] == ["Alpha", "Beta"]
```

## User Acceptance

- A reader can view the complete list without instructions.
- An empty list is presented as a usable state.

## Guardrails

- The response contains books in insertion order.
- Listing does not transmit data to a third-party service.
