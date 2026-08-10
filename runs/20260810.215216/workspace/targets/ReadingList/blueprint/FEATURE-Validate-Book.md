# FEATURE: Validate Book

| Field       | Value |
|-------------|-------|
| Version     | 20260810 V1 |
| Description | Reject book submissions that omit a title or author before persistence. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, FEATURE-Add-Book.md |
| Provides    | book submission validation |
| Consumes    | POST /books |

## Workflow

The `POST /books` workflow validates the submitted title and author before invoking persistence. A title or author containing only whitespace is invalid. Invalid submissions return HTTP 400, provide a clear user-facing reason, and do not create a book.

## Programmatic Acceptance

Requires: python-package=flask; scope=test

### rejects-empty-title
An empty title is rejected before persistence.

Sea Trials: st-005

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

response = client.post("/books", data={"title": "", "author": "Author"})
assert response.status_code == 400

books = client.get("/books").get_json()
assert books == []
```

### rejects-empty-author
An empty author is rejected before persistence.

Sea Trials: st-005

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

response = client.post("/books", data={"title": "Book", "author": "   "})
assert response.status_code == 400

books = client.get("/books").get_json()
assert books == []
```

### accepts-complete-submission
A submission with a non-empty title and author is not rejected by validation.

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

response = client.post("/books", data={"title": "Book", "author": "Author"})
assert response.status_code in (200, 201, 302)
```

## User Acceptance

- A reader receives a clear error when either required field is empty.

## Guardrails

- Validation occurs before any persistence write.
- Validation does not transmit submitted data to a third-party service.
