# FEATURE: Add Book

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Defines the workflow for creating and displaying a valid book. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | POST /books |
| Consumes     | books persistence interface |

## Purpose

A reader submits a title and author through the reading-list form. The application validates the submission before persistence, creates the book through `Database.create_book`, and returns a response that makes the new book available to the reading-list view.

## Route

`POST /books`

Input fields:

- `title`
- `author`

A valid submission is persisted and returns HTTP `303`, redirecting to `/`.

## Reads and Writes

- Reads submitted title and author.
- Writes one row through the books persistence interface.
- Does not reorder existing books.
- Does not alter the read status of existing books.

## Programmatic Acceptance

Requires: python-package=flask; scope=runtime

=== AC add-route-reachable ===
Intent: The book creation route accepts a valid submission.
from app import create_app

app = create_app({"TESTING": True, "READING_LIST_DATABASE": ":memory:"})
client = app.test_client()
title = "A Valid Book"
author = "A Valid Author"

response = client.post("/books", data={"title": title, "author": author})
assert response.status_code == 303
=== END AC add-route-reachable ===

=== AC add-persists-book ===
Intent: A valid route submission is stored and readable through the persistence interface.
from app import create_app
from app.database import Database

database_path = "acceptance-add.sqlite"
app = create_app({"TESTING": True, "READING_LIST_DATABASE": database_path})
client = app.test_client()
title = "Stored Title"
author = "Stored Author"

response = client.post("/books", data={"title": title, "author": author})
assert response.status_code == 303

books = Database(database_path).list_books()
assert len(books) == 1
assert books[0].title == title
assert books[0].author == author
assert books[0].is_read is False
=== END AC add-persists-book ===

=== AC add-preserves-existing-order ===
Intent: Adding a book leaves existing books first and appends the new book.
from app import create_app
from app.database import Database

database_path = "acceptance-add-order.sqlite"
database = Database(database_path)
first_title = "Existing Title"
first_author = "Existing Author"
second_title = "Added Title"
second_author = "Added Author"
database.create_book(first_title, first_author)

app = create_app({"TESTING": True, "READING_LIST_DATABASE": database_path})
response = app.test_client().post(
    "/books", data={"title": second_title, "author": second_author}
)
assert response.status_code == 303

books = Database(database_path).list_books()
assert [book.title for book in books] == [first_title, second_title]
assert [book.author for book in books] == [first_author, second_author]
=== END AC add-preserves-existing-order ===

## User Acceptance

- A reader can submit a title and author and see the new book in the reading list.

## Guardrails

- Only valid submissions reach `Database.create_book`.
- A successful addition does not reorder existing books.
- Newly added books are unread.
