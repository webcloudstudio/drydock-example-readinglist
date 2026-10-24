# FEATURE: Remove Book

| Field       | Value |
|-------------|-------|
| Version     | 20261023 V1 |
| Description | Removes a selected persisted book from the reading list. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | POST `/books/<book_id>/delete` |
| Consumes    | `app_server.create_app`, `persistence.books.delete` |

## Purpose

A reader submits the removal action for a selected book. The feature deletes only that persisted identifier through `books.delete`, then returns to the list workflow.

## Database Interface

- `FEATURE-REMOVE-BOOK-001` — write: delete a book - supplies: `id` - returns: `id`

## Workflow

1. A book identifier is submitted to `POST /books/<book_id>/delete`.
2. The selected book is deleted through the persistence contract.
3. The reader returns to the reading-list page.
4. The next read omits the removed book.

## Programmatic Acceptance

=== AC remove-book-route ===
Intent: The removal route deletes the selected book and returns to the reading-list workflow.

from persistence.testing import committed_session
from app_server.testing import web_client

title = "Remove Book Acceptance Title"
author = "Remove Book Acceptance Author"

with committed_session() as db:
    created = db.books.create(
        title=title,
        author=author,
        insertion_order=900003,
    )

try:
    client = web_client()
    response = client.post(f"/books/{created.id}/delete")
    assert response.status_code == 302

    follow_up = client.get("/")
    assert follow_up.status_code == 200
    body = follow_up.get_data(as_text=True)
    assert title not in body
finally:
    with committed_session() as db:
        db.books.delete(id=created.id)
=== END AC remove-book-route ===

=== AC remove-book-readback ===
Intent: Removing a book changes subsequent persisted reads so the selected identifier is absent.

from persistence.testing import committed_session

title = "Remove Book Readback Title"
author = "Remove Book Readback Author"

with committed_session() as db:
    created = db.books.create(
        title=title,
        author=author,
        insertion_order=900004,
    )
    deleted = db.books.delete(id=created.id)
    assert deleted.id == created.id

    remaining = db.books.list()
    assert all(row.id != created.id for row in remaining)

    db.books.delete(id=created.id)
=== END AC remove-book-readback ===

## User Acceptance

- A reader can remove a selected book and no longer sees it on the next list read.

## Guardrails

- Removal affects only the selected persisted book.
- A removed book is not shown on the next reading-list request.
- The feature does not silently reorder remaining books.
