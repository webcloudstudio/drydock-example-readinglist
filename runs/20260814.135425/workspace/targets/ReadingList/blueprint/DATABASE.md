# DATABASE: ReadingList Persistence

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Defines the SQLite persistence interface and schema for ordered books and read status. |
| Depends On  | ARCHITECTURE.md |
| Provides    | books persistence interface |
| Consumes    | application factory |

## Access Patterns

| Caller | Operation | Store | Interface |
|---|---|---|---|
| Book creation workflow | Create a book | SQLite `books` table | `Database.create_book` |
| Reading-list screen and status workflow | List books | SQLite `books` table | `Database.list_books` |
| Removal workflow | Delete a book | SQLite `books` table | `Database.delete_book` |
| Mark-read workflow | Update status | SQLite `books` table | `Database.mark_book_read` |

## Persistence Interfaces

### `Database`

Location: `app.database`

Allowed callers: application routes and tests.

Public methods:

- `Database(path)`
- `create_book(title, author) -> Book`
- `list_books() -> list[Book]`
- `delete_book(book_id) -> bool`
- `mark_book_read(book_id) -> bool`

`Book` exposes `id`, `title`, `author`, and `is_read`.

The constructor creates the database schema when needed. Each operation manages its own connection and returns state through the typed interface. Callers never receive raw connections or cursors.

## Schema

The `books` table contains:

- `id` — integer primary key; its ascending value defines insertion order.
- `title` — non-empty text.
- `author` — non-empty text.
- `is_read` — boolean-compatible integer, defaulting to unread.

No timestamp is required for ordering.

## Migrations and Initialization

Schema creation is idempotent. A fresh configured SQLite path is sufficient to start the application. Existing rows remain available across application instances using the same path.

## Programmatic Acceptance

Requires: python-package=pytest; scope=test

=== AC database-create-read ===
Intent: A created book is persisted and can be read back through a separate database operation.
from app.database import Database

database_path = "acceptance-create-read.sqlite"
title = "The Left Hand of Darkness"
author = "Ursula K. Le Guin"
database = Database(database_path)

created = database.create_book(title, author)
books = database.list_books()

assert len(books) == 1
book = books[0]
assert book.id == created.id
assert book.title == title
assert book.author == author
assert book.is_read is False
=== END AC database-create-read ===

=== AC database-order ===
Intent: Listing returns books in insertion order.
from app.database import Database

database = Database("acceptance-order.sqlite")
first_title = "First Book"
first_author = "First Author"
second_title = "Second Book"
second_author = "Second Author"

database.create_book(first_title, first_author)
database.create_book(second_title, second_author)
books = database.list_books()

assert [book.title for book in books] == [first_title, second_title]
assert [book.author for book in books] == [first_author, second_author]
=== END AC database-order ===

=== AC database-update-delete ===
Intent: Read-status updates and deletion persist through subsequent reads.
from app.database import Database

database = Database("acceptance-update-delete.sqlite")
title = "A Book"
author = "An Author"
created = database.create_book(title, author)

updated = database.mark_book_read(created.id)
assert updated is True
read_back = database.list_books()
assert read_back[0].is_read is True

deleted = database.delete_book(created.id)
assert deleted is True
assert database.list_books() == []
=== END AC database-update-delete ===

## User Acceptance

- None.

## Guardrails

- All book persistence is encapsulated by `Database`.
- Empty titles and authors must never be stored.
- Listing must always use ascending insertion order.
- Read status must be preserved across reads and application instances.
