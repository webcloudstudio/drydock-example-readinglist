# DATABASE: ReadingList

| Field       | Value |
|-------------|-------|
| Version     | 20261023 V1 |
| Description | Persistence stores and typed interfaces for ReadingList. |
| Depends On  | ARCHITECTURE.md |
| Provides    | persistence.books |
| Build Order | 1 |

## Persistence Boundary

| Boundary | Rule |
|----------|------|
| Raw storage access | Only the generated `persistence/` package reaches the store. |
| Caller dependency | Features depend on declared access patterns and their DTOs, not on schemas. |
| Implementation | Generated from this file at the DATABASE build step; never written by hand. |

## Access Patterns

### FEATURE-READING-LIST-001 — List books

| Field | Value |
|-------|-------|
| Owner | FEATURE-READING-LIST.md |
| Access | read |
| Repository operation | `books.list` |
| Compatibility | unchanged |

Input: `BookListInput`

| Field | Type | Required |
|-------|------|----------|
| — | — | — |

Output: `BookRow[]`

| Field | Type |
|-------|------|
| id | INTEGER |
| title | TEXT |
| author | TEXT |
| insertion_order | INTEGER |

### FEATURE-ADD-BOOK-001 — Create a book

| Field | Value |
|-------|-------|
| Owner | FEATURE-ADD-BOOK.md |
| Access | write |
| Repository operation | `books.create` |
| Compatibility | unchanged |

Input: `BookCreateInput`

| Field | Type | Required |
|-------|------|----------|
| title | TEXT | yes |
| author | TEXT | yes |
| insertion_order | INTEGER | yes |

Output: `BookRow`

| Field | Type |
|-------|------|
| id | INTEGER |
| title | TEXT |
| author | TEXT |
| insertion_order | INTEGER |

### FEATURE-REMOVE-BOOK-001 — Delete a book

| Field | Value |
|-------|-------|
| Owner | FEATURE-REMOVE-BOOK.md |
| Access | write |
| Repository operation | `books.delete` |
| Compatibility | unchanged |

Input: `BookDeleteInput`

| Field | Type | Required |
|-------|------|----------|
| id | INTEGER | yes |

Output: `DeletedBook`

| Field | Type |
|-------|------|
| id | INTEGER |

## Schemas

## `books`

| Field | Type | Notes |
|-------|------|-------|
| id | INTEGER PK | Stable book identifier. |
| title | TEXT NOT NULL | Book title. |
| author | TEXT NOT NULL | Book author. |
| insertion_order | INTEGER NOT NULL UNIQUE | Monotonic order assigned when the book is added. |

## Migrations

| Access Pattern | Revision | State |
|----------------|----------|-------|
| FEATURE-READING-LIST-001 | MIGRATION-FEATURE-READING-LIST-001 | planned |
| FEATURE-ADD-BOOK-001 | MIGRATION-FEATURE-ADD-BOOK-001 | planned |
| FEATURE-REMOVE-BOOK-001 | MIGRATION-FEATURE-REMOVE-BOOK-001 | planned |

## Config (.env)

| Key | Type | Required | Notes |
|-----|------|----------|-------|
| DATABASE_URL | string | no | Optional database DSN; overrides `DATABASE_PATH`. |
| DATABASE_PATH | string | no | Optional local database path; defaults to `data/app.db`. |

## File Stores

| Store | Root dir | Notes |
|-------|----------|-------|
| — | — | No file store. |

## External Services

| Service | Wrapper | Notes |
|---------|---------|-------|
| — | — | No external services. |

## External Libraries

| Library | Ownership | Distribution | Consumer Contract |
|---------|-----------|--------------|-------------------|
| — | — | — | No external persistence libraries. |

## Programmatic Acceptance

=== AC database-books-create ===
Intent: The books create operation returns the declared book row with the supplied values.

from persistence.testing import db_session

title = "The Left Hand of Darkness"
author = "Ursula K. Le Guin"
insertion_order = 1

with db_session() as db:
    row = db.books.create(
        title=title,
        author=author,
        insertion_order=insertion_order,
    )
    assert row.title == title
    assert row.author == author
    assert row.insertion_order == insertion_order
=== END AC database-books-create ===

=== AC database-books-list ===
Intent: The books list operation returns books in insertion order.

from persistence.testing import db_session

first_title = "Dune"
first_author = "Frank Herbert"
second_title = "Kindred"
second_author = "Octavia E. Butler"

with db_session() as db:
    db.books.create(
        title=first_title,
        author=first_author,
        insertion_order=1,
    )
    db.books.create(
        title=second_title,
        author=second_author,
        insertion_order=2,
    )
    rows = db.books.list()

    assert [row.title for row in rows] == [first_title, second_title]
    assert [row.author for row in rows] == [first_author, second_author]
=== END AC database-books-list ===

=== AC database-books-delete ===
Intent: The books delete operation returns the selected identifier and removes that book from subsequent reads.

from persistence.testing import db_session

title = "A Wizard of Earthsea"
author = "Ursula K. Le Guin"

with db_session() as db:
    created = db.books.create(
        title=title,
        author=author,
        insertion_order=1,
    )
    deleted = db.books.delete(id=created.id)
    assert deleted.id == created.id

    remaining = db.books.list()
    assert all(row.id != created.id for row in remaining)
=== END AC database-books-delete ===

## User Acceptance

- None.

## Guardrails

- Empty titles and authors are rejected by the feature validation boundary before persistence.
- Books retain insertion order and are never silently reordered.
- Raw storage access remains encapsulated by the generated persistence package.
