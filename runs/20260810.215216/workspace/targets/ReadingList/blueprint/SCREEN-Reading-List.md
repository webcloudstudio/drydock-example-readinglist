# SCREEN: Reading List

| Field       | Value |
|-------------|-------|
| Version     | 20260810 V1 |
| Description | Present the reading list and controls for adding and removing books. |
| Depends On  | UI-GENERAL.md, FEATURE-Add-Book.md, FEATURE-List-Books.md, FEATURE-Validate-Book.md, FEATURE-Remove-Book.md |
| Provides    | GET / |
| Consumes    | GET /books, POST /books, POST /books/{id}/remove, book submission validation |
| Route       | / |

## Layout and Interactions

The root screen presents the application name, a book-entry form with title and author fields, an add control, the current books in insertion order, and a remove control for each book. When no books exist, it presents a usable empty-list state. Validation failures are shown as clear user-facing messages.

## Programmatic Acceptance

Requires: python-package=flask; scope=test

### renders-empty-list
The primary entry point is reachable and renders the empty-list state.

Sea Trials: st-007

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

response = client.get("/")
assert response.status_code == 200
assert b"title" in response.data.lower()
assert b"author" in response.data.lower()
```

### renders-added-book
A book added through the user workflow appears on the primary screen.

Sea Trials: st-002, st-003

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

client.post("/books", data={"title": "Book", "author": "Author"})
response = client.get("/")

assert response.status_code == 200
assert b"Book" in response.data
assert b"Author" in response.data
```

### submits-book-form
The screen's add interaction calls the declared creation route.

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

response = client.post("/", data={"title": "Book", "author": "Author"})
assert response.status_code in (200, 201, 302)
assert client.get("/books").get_json()[0]["title"] == "Book"
```

### submits-remove-control
The screen's remove interaction calls the declared removal route.

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

client.post("/books", data={"title": "Book", "author": "Author"})
book = client.get("/books").get_json()[0]

response = client.post(f"/books/{book['id']}/remove")
assert response.status_code in (200, 204, 302)
assert client.get("/books").get_json() == []
```

### renders-validation-error
An invalid screen submission returns to a state containing a user-facing error.

Sea Trials: st-005

```python
from app import create_app

app = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = app.test_client()

response = client.post("/", data={"title": "", "author": "Author"})
assert response.status_code == 400
assert len(response.data) > 0
assert client.get("/books").get_json() == []
```

## User Acceptance

- A reader can add, view, and remove books without instructions.
- The empty-list state clearly indicates how to begin.

## Guardrails

- Books are displayed in insertion order.
- The screen never sends the reading list to a third-party service.
