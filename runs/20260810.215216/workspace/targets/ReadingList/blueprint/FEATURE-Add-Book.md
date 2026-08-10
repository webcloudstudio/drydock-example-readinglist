# FEATURE: Add Book

| Field       | Value |
|-------------|-------|
| Version     | 20260810 V1 |
| Description | Stores a submitted book with its title and author. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | POST /books |
| Consumes    | books persistence interface |

## Workflow

A reader submits a title and author to `POST /books`. The workflow validates that both values are non-empty, stores the book through `BookStore.add`, and returns a response from which the stored book can be read.

## Input

The request carries `title` and `author` form fields. Values containing non-whitespace characters are accepted.

## Output

A successful submission returns an HTTP redirect to the reading-list view. The subsequent `GET /books` response includes the stored book.

## Programmatic Acceptance

### add-route
The add route accepts a valid title and author.

Requires: python-package=flask; scope=test

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    app = create_app({"TESTING": True, "DATABASE": str(Path(directory) / "books.sqlite3")})
    client = app.test_client()
    response = client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})
    assert response.status_code in (302, 303)
```

### add-round-trip
A successful add is visible through the public list route.

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    app = create_app({"TESTING": True, "DATABASE": str(Path(directory) / "books.sqlite3")})
    client = app.test_client()
    client.post("/books", data={"title": "Dune", "author": "Frank Herbert"})
    response = client.get("/books")
    assert response.status_code == 200
    books = response.get_json()
    assert books[-1]["title"] == "Dune"
    assert books[-1]["author"] == "Frank Herbert"
```

### add-requires-both-fields
A valid add creates a record containing both required fields.

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    app = create_app({"TESTING": True, "DATABASE": str(Path(directory) / "books.sqlite3")})
    client = app.test_client()
    client.post("/books", data={"title": "Book", "author": "Author"})
    books = client.get("/books").get_json()
    assert books[0].keys() >= {"id", "title", "author"}
    assert books[0]["title"] == "Book"
    assert books[0]["author"] == "Author"
```

## User Acceptance

- A reader can add a book using the title and author fields.

## Guardrails

- A successful submission stores no fields other than the book record data defined by the persistence contract.
- The add workflow uses the local persistence boundary.
