# DATABASE: Books

| Field       | Value |
|-------------|-------|
| Version     | 20260810 V1 |
| Description | Defines the local SQLite store and persistence interface for books. |
| Depends On  | ARCHITECTURE.md |
| Provides    | books persistence interface |
| Consumes    | — |

## Access Patterns

| Caller | Operation | Store | Interface |
|---|---|---|---|
| Add-book workflow | Insert | `books` | `BookStore.add(title, author)` |
| List-books workflow | Read ordered collection | `books` | `BookStore.list()` |
| Remove-book workflow | Delete | `books` | `BookStore.remove(book_id)` |

## Persistence Interfaces

The `BookStore` interface owns all book storage operations. Application workflows call `add`, `list`, and `remove`; no route accesses SQLite directly.

The SQLite database is stored at `instance-reading-list.sqlite3` by default. Tests may provide an isolated database path through application configuration.

## Schema

The `books` table contains:

| Column | Type | Constraints |
|---|---|---|
| `id` | INTEGER | Primary key |
| `title` | TEXT | Required |
| `author` | TEXT | Required |

Book retrieval orders rows by ascending `id`, preserving insertion order.

## Migrations

Application startup creates the `books` table when it does not exist. Existing rows remain available across application instances using the same database path.

## Programmatic Acceptance

### persistence-interface
The persistence boundary stores and reads a book through its public interface.

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    app = create_app({"TESTING": True, "DATABASE": str(Path(directory) / "books.sqlite3")})
    store = app.extensions["book_store"]
    created = store.add("Dune", "Frank Herbert")
    books = store.list()
    assert any(book["id"] == created["id"] and book["title"] == "Dune" and book["author"] == "Frank Herbert" for book in books)
```

### insertion-order
The persistence interface returns books in insertion order.

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    app = create_app({"TESTING": True, "DATABASE": str(Path(directory) / "books.sqlite3")})
    store = app.extensions["book_store"]
    store.add("First", "Author A")
    store.add("Second", "Author B")
    books = store.list()
    assert [book["title"] for book in books] == ["First", "Second"]
```

### removal
Removing a stored book makes it absent from a subsequent read.

```python
import tempfile
from pathlib import Path
from app import create_app

with tempfile.TemporaryDirectory() as directory:
    app = create_app({"TESTING": True, "DATABASE": str(Path(directory) / "books.sqlite3")})
    store = app.extensions["book_store"]
    created = store.add("Remove me", "Author")
    store.remove(created["id"])
    assert all(book["id"] != created["id"] for book in store.list())
```

## User Acceptance

- The application keeps reader data in local SQLite storage.

## Guardrails

- SQLite is the only persistence backend.
- The store never calls a third-party service.
- All reads preserve insertion order.
