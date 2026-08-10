# FEATURE: Remove Book

| Field       | Value |
|-------------|-------|
| Version     | 20260810 V1 |
| Description | Remove a selected book from the local reading list. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | POST /books/{id}/remove |
| Consumes    | books persistence interface |

## Workflow

The `POST /books/{id}/remove` route removes the identified book through the persistence interface. A successful removal returns a response indicating success. A subsequent `GET /books` omits the removed book while retaining all other books in insertion order.

## Programmatic Acceptance

Requires: python-package=flask; scope=test

### removes-selected-book
A selected book is absent after removal.

Sea Trials: st-004

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

client.post("/books", data={"title": "Book One", "author": "Author One"})
books = client.get("/books").get_json()
book_id = books[0]["id"]

response = client.post(f"/books/{book_id}/remove")
assert response.status_code in (200, 204, 302)

remaining = client.get("/books").get_json()
assert remaining == []
```

### preserves-other-books
Removing one book does not remove other books.

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

client.post("/books", data={"title": "Book One", "author": "Author One"})
client.post("/books", data={"title": "Book Two", "author": "Author Two"})
books = client.get("/books").get_json()

client.post(f"/books/{books[0]['id']}/remove")
remaining = client.get("/books").get_json()

assert len(remaining) == 1
assert remaining[0]["title"] == "Book Two"
assert remaining[0]["author"] == "Author Two"
```

### unknown-book-removal
Removing an unknown book does not create or alter a book.

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

response = client.post("/books/999999/remove")
assert response.status_code in (404, 204, 302)

assert client.get("/books").get_json() == []
```

## User Acceptance

- A reader can identify and remove a listed book without instructions.

## Guardrails

- Removal operates only on the selected local record.
- Removal does not transmit reader data to a third-party service.
