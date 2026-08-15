# FEATURE: Book Creation

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Defines the workflow for adding a titled and authored book to the reading list. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | POST /books, book_creation |
| Consumes    | book_store.add, books_table |

## Purpose

Allow a reader to submit a non-empty title and author and have the book stored in the reading list.

## Trigger

The reader submits the book form with `POST /books`.

## Workflow

1. Read the title and author form fields.
2. Pass the submitted values to the book-store boundary.
3. Redirect to `/` after persistence succeeds.
4. The subsequent list read displays the newly stored book.

Validation of empty fields is owned by `FEATURE-Incomplete-Submission.md`.

## Operational Behavior

- Successful creation uses a redirect response to return the reader to the list.
- The submitted title and author are preserved.
- Existing books retain their relative order.
- Persistence is performed only through `BookStore.add`.

## Programmatic Acceptance

=== AC book-creation-route ===
Intent: The book-creation route accepts a submitted title and author and returns a redirect response.

from app import create_app

title = "Middlemarch"
author = "George Eliot"
application = create_app({"TESTING": True, "DATABASE": ":memory:"})
response = application.test_client().post(
    "/books",
    data={"title": title, "author": author},
)

assert response.status_code in (302, 303)
=== END AC book-creation-route ===

=== AC book-creation-readback ===
Intent: A successfully submitted book is visible when the list is read again.

from app import create_app

title = "Kindred"
author = "Octavia Butler"
application = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = application.test_client()

created = client.post("/books", data={"title": title, "author": author})
assert created.status_code in (302, 303)
response = client.get("/")
body = response.get_data(as_text=True)

assert response.status_code == 200
assert title in body
assert author in body
=== END AC book-creation-readback ===

=== AC book-creation-preserves-existing-order ===
Intent: Adding a new book preserves the relative order of books already present.

from app import create_app

first_title = "First"
first_author = "Author One"
second_title = "Second"
second_author = "Author Two"
application = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = application.test_client()

assert client.post("/books", data={"title": first_title, "author": first_author}).status_code in (302, 303)
assert client.post("/books", data={"title": second_title, "author": second_author}).status_code in (302, 303)
body = client.get("/").get_data(as_text=True)

assert body.index(first_title) < body.index(second_title)
=== END AC book-creation-preserves-existing-order ===

## User Acceptance

- None.

## Guardrails

- A book is stored only when both title and author are non-empty.
- Successful submission must make the book visible on the next list read.
- Existing books must not be reordered.
