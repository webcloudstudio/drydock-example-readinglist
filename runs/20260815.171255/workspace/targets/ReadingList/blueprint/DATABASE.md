# DATABASE: Book Persistence

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Defines the SQLite persistence contract for ordered reading-list books. |
| Depends On  | ARCHITECTURE.md |
| Provides    | book_store.add, book_store.list_ordered, book_store.remove, books_table |
| Consumes    | application_factory |

## Access Patterns

| Caller | Operation | Store | Interface |
|---|---|---|---|
| Book creation workflow | Add a submitted title and author | `books` | `BookStore.add(title, author)` |
| Ordered-list workflow | Read all books | `books` | `BookStore.list_ordered()` |
| Book-removal workflow | Delete a selected book | `books` | `BookStore.remove(book_id)` |

## Persistence Interfaces

| Store | Public interface | Module | Allowed callers | Notes |
|---|---|---|---|---|
| SQLite `books` table | `BookStore.add(title, author) -> Book` | `app.persistence` | Application workflows | Persists one book. |
| SQLite `books` table | `BookStore.list_ordered() -> list[Book]` | `app.persistence` | Application workflows | Returns rows in insertion order. |
| SQLite `books` table | `BookStore.remove(book_id) -> bool` | `app.persistence` | Application workflows | Removes the selected row and reports whether it existed. |

## Schema

The `books` table contains:

- `id`: integer primary key.
- `title`: required text.
- `author`: required text.
- `created_at`: persisted timestamp or equivalent insertion marker.

The primary key is monotonically assigned by SQLite and is used to preserve insertion order. The database must reject null title or author values. Application validation additionally rejects empty submitted values.

## Configuration

The application factory supplies the database location through Flask configuration. Tests may provide an isolated temporary path or an in-memory database. Connections are scoped to the application context and closed after use.

## Migrations and Initialization

Application startup creates the `books` table when it does not exist. Initialization is idempotent and must not delete existing rows.

## Programmatic Acceptance

=== AC database-add-readback ===
Intent: A book added through the persistence interface can be read back with the submitted fields.

from app import create_app
from app.persistence import get_book_store

title = "The Dispossessed"
author = "Ursula K. Le Guin"
application = create_app({"TESTING": True, "DATABASE": ":memory:"})

with application.app_context():
    store = get_book_store()
    created = store.add(title, author)
    books = store.list_ordered()

assert len(books) == 1
assert books[0].id == created.id
assert books[0].title == title
assert books[0].author == author
=== END AC database-add-readback ===

=== AC database-order ===
Intent: Ordered reads preserve the order in which books were added.

from app import create_app
from app.persistence import get_book_store

first_title = "A"
first_author = "Author A"
second_title = "B"
second_author = "Author B"
application = create_app({"TESTING": True, "DATABASE": ":memory:"})

with application.app_context():
    store = get_book_store()
    store.add(first_title, first_author)
    store.add(second_title, second_author)
    books = store.list_ordered()

assert [book.title for book in books] == [first_title, second_title]
assert [book.author for book in books] == [first_author, second_author]
=== END AC database-order ===

=== AC database-remove ===
Intent: Removing an existing book makes it absent from a subsequent persistence read.

from app import create_app
from app.persistence import get_book_store

title = "To Remove"
author = "Author"
application = create_app({"TESTING": True, "DATABASE": ":memory:"})

with application.app_context():
    store = get_book_store()
    created = store.add(title, author)
    removed = store.remove(created.id)
    books = store.list_ordered()

assert removed is True
assert books == []
=== END AC database-remove ===

=== AC database-empty ===
Intent: A new database returns an empty ordered collection.

from app import create_app
from app.persistence import get_book_store

application = create_app({"TESTING": True, "DATABASE": ":memory:"})

with application.app_context():
    books = get_book_store().list_ordered()

assert books == []
=== END AC database-empty ===

## User Acceptance

- None.

## Guardrails

- All SQLite access is encapsulated by `app.persistence`.
- Empty titles and authors must never be stored.
- Ordered reads must preserve addition order.
