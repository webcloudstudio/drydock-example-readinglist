# DATABASE: Reading List

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Persistence contract for the reading list: one books table and its access patterns. |
| Depends On  | ARCHITECTURE.md |
| Provides    | books.create, books.list, books.get, books.delete |

## Access Patterns

### FEATURE-BOOKS-001 — Create a book

| Field | Value |
|-------|-------|
| Owner | FEATURE-AddBook.md |
| Access | write |
| Repository operation | `books.create` |
| Compatibility | rebuild |

Input: BookCreate

| Field | Type | Notes |
|-------|------|-------|
| title | TEXT | Non-empty after trimming. |
| author | TEXT | Non-empty after trimming. |

Output: Book

| Field | Type | Notes |
|-------|------|-------|
| id | INTEGER | Assigned on insert. |
| title | TEXT | |
| author | TEXT | |

### FEATURE-BOOKS-002 — List books in insertion order

| Field | Value |
|-------|-------|
| Owner | FEATURE-ListBooks.md |
| Access | read |
| Repository operation | `books.list` |
| Compatibility | rebuild |

Input: BookListRequest

| Field | Type | Notes |
|-------|------|-------|
| (none) | — | The operation takes no input fields. |

Output: Book

| Field | Type | Notes |
|-------|------|-------|
| id | INTEGER | Ordered ascending. |
| title | TEXT | |
| author | TEXT | |

### FEATURE-BOOKS-003 — Retrieve a book by id

| Field | Value |
|-------|-------|
| Owner | FEATURE-RemoveBook.md |
| Access | read |
| Repository operation | `books.get` |
| Compatibility | rebuild |

Input: BookId

| Field | Type | Notes |
|-------|------|-------|
| id | INTEGER | |

Output: Book

| Field | Type | Notes |
|-------|------|-------|
| id | INTEGER | |
| title | TEXT | |
| author | TEXT | |

### FEATURE-BOOKS-004 — Delete a book by id

| Field | Value |
|-------|-------|
| Owner | FEATURE-RemoveBook.md |
| Access | write |
| Repository operation | `books.delete` |
| Compatibility | rebuild |

Input: BookId

| Field | Type | Notes |
|-------|------|-------|
| id | INTEGER | |

Output: BookId

| Field | Type | Notes |
|-------|------|-------|
| id | INTEGER | The id that was removed. |

## Schema

## `books`

| Field | Type | Notes |
|-------|------|-------|
| id | INTEGER PK | Autoincrement; list order is ascending id. |
| title | TEXT NOT NULL | |
| author | TEXT NOT NULL | |

## Programmatic Acceptance

- None. Drydock validates declared SQLite schema construction and connectivity invariants deterministically.
## User Acceptance

- None.

## Guardrails

- The `books` table must not store an empty title or author.
- Callers must not write SQL; they reach storage only through the generated `books.<verb>` operations.
