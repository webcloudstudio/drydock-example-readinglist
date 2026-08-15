# FEATURE: Ordered List

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Defines the ordered reading-list read workflow and its empty-list behavior. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, FEATURE-Book-Creation.md |
| Provides    | GET /, ordered_book_listing |
| Consumes    | book_store.list_ordered, books_table |

## Purpose

Show every stored book in the same order in which it was added.

## Trigger

The reader requests `GET /`.

## Workflow

1. Read books through `BookStore.list_ordered`.
2. Render the resulting collection on the reading-list screen.
3. When the collection is empty, render an understandable empty-list state.

## Operational Behavior

The list response is successful for both an empty and a populated store. Each displayed book includes its title and author. The persistence ordering is the authoritative display ordering.

## Programmatic Acceptance

=== AC ordered-list-route ===
Intent: The reading-list route is reachable and returns a successful response for an empty store.

from app import create_app

application = create_app({"TESTING": True, "DATABASE": ":memory:"})
response = application.test_client().get("/")

assert response.status_code == 200
=== END AC ordered-list-route ===

=== AC ordered-list-empty-state ===
Intent: An empty store produces a reader-understandable empty-list state.

from app import create_app

application = create_app({"TESTING": True, "DATABASE": ":memory:"})
body = application.test_client().get("/").get_data(as_text=True)

assert body
assert "empty" in body.lower() or "no books" in body.lower()
=== END AC ordered-list-empty-state ===

=== AC ordered-list-order ===
Intent: The list renders multiple books in their insertion order.

from app import create_app

first_title = "First Added"
first_author = "First Author"
second_title = "Second Added"
second_author = "Second Author"
application = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = application.test_client()

assert client.post("/books", data={"title": first_title, "author": first_author}).status_code in (302, 303)
assert client.post("/books", data={"title": second_title, "author": second_author}).status_code in (302, 303)
response = client.get("/")
body = response.get_data(as_text=True)

assert response.status_code == 200
assert body.index(first_title) < body.index(second_title)
assert first_author in body
assert second_author in body
=== END AC ordered-list-order ===

## User Acceptance

- None.

## Guardrails

- Books must always be displayed in insertion order.
- The empty-list state must be clear.
- The route must read persisted state rather than relying on submission response data.
