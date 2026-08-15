# FEATURE: Book Removal

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Removes a selected book and preserves the relative order of remaining books. |
| Depends On  | DATABASE.md, FEATURE-Ordered-List.md |
| Provides    | POST /books/{id}/remove, book_removal |
| Consumes    | book_store.remove, ordered_book_listing |

## Purpose

Allow a reader to remove a selected book from the reading list.

## Trigger and Sequence

1. The reader submits the removal control for a listed book.
2. The application removes that book through the persistence boundary.
3. The application redirects or returns the reader to the ordered list.
4. The removed book is absent and remaining books retain their relative order.

## Reads and Writes

- Reads the selected book identifier from the removal request.
- Writes deletion through `book_store.remove`.
- Reads the resulting list through `ordered_book_listing`.

## Operational Behavior

The removal route is `POST /books/<int:book_id>/remove`. Unknown identifiers do not remove any other book.

## Programmatic Acceptance

=== AC removal-route-reachable ===
Intent: The removal route accepts a valid removal request.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
title = "Book to Remove"
author = "Removal Author"
created = client.post("/books", data={"title": title, "author": author})
assert created.status_code in (200, 302, 303)
listed = client.get("/")
assert listed.status_code == 200
removed = client.post("/books/1/remove")
assert removed.status_code in (200, 302, 303)
=== END AC removal-route-reachable ===

=== AC removal-persists ===
Intent: Removing a book makes it absent on the next public list read.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
title = "Temporary Book"
author = "Temporary Author"
client.post("/books", data={"title": title, "author": author})
before = client.get("/")
assert before.status_code == 200
removed = client.post("/books/1/remove")
assert removed.status_code in (200, 302, 303)
after = client.get("/")
assert after.status_code == 200
assert title.encode() not in after.data
assert author.encode() not in after.data
=== END AC removal-persists ===

=== AC removal-preserves-remaining-order ===
Intent: Removing one book leaves the other books in their original relative order.
from app import create_app

app = create_app({"TESTING": True})
client = app.test_client()
first_title = "First Remaining"
first_author = "First Author"
removed_title = "Middle Removed"
removed_author = "Middle Author"
last_title = "Last Remaining"
last_author = "Last Author"
client.post("/books", data={"title": first_title, "author": first_author})
client.post("/books", data={"title": removed_title, "author": removed_author})
client.post("/books", data={"title": last_title, "author": last_author})
client.post("/books/2/remove")
response = client.get("/")
assert response.status_code == 200
first_position = response.data.index(first_title.encode())
last_position = response.data.index(last_title.encode())
assert first_position < last_position
assert removed_title.encode() not in response.data
=== END AC removal-preserves-remaining-order ===

## User Acceptance

- A reader can remove a listed book and see the updated list.

## Guardrails

- Removal must go through the persistence boundary.
- Removing one book must never reorder the remaining books.
