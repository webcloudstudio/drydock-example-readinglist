# FEATURE: Reading List

| Field       | Value |
|-------------|-------|
| Version     | 20261023 V1 |
| Description | Serves the ordered reading-list workflow for persisted books. |
| Depends On  | ARCHITECTURE.md, DATABASE.md |
| Provides    | GET `/` |
| Consumes    | `app_server.create_app`, `persistence.books.list` |

## Purpose

The primary reading-list page retrieves persisted books through `persistence.books.list` and presents them in insertion order. It renders a clear empty state when no books are available.

## Database Interface

- `FEATURE-READING-LIST-001` — read: list books - supplies: — - returns: `id`, `title`, `author`, `insertion_order`

## Workflow

1. A reader requests `GET /`.
2. The feature reads books through `books.list`.
3. The page renders the returned books without reordering them.
4. An empty result renders the empty-list state.

## Programmatic Acceptance

=== AC reading-list-reachable ===
Intent: The primary reading-list route is reachable and returns a successful page response.

from app_server.testing import web_client

client = web_client()
response = client.get("/")
assert response.status_code == 200
=== END AC reading-list-reachable ===

=== AC reading-list-order ===
Intent: The reading-list route presents persisted books in insertion order.

from persistence.testing import committed_session
from app_server.testing import web_client

first_title = "Reading List First"
first_author = "Reading List Author One"
second_title = "Reading List Second"
second_author = "Reading List Author Two"

with committed_session() as db:
    first = db.books.create(
        title=first_title,
        author=first_author,
        insertion_order=900001,
    )
    second = db.books.create(
        title=second_title,
        author=second_author,
        insertion_order=900002,
    )

try:
    client = web_client()
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    first_position = body.index(first_title)
    second_position = body.index(second_title)
    assert first_position < second_position
finally:
    with committed_session() as db:
        db.books.delete(id=first.id)
        db.books.delete(id=second.id)
=== END AC reading-list-order ===

=== AC reading-list-empty ===
Intent: The reading-list route successfully renders when no matching books are present.

from app_server.testing import web_client

title = "No Matching Reading List Fixture"
client = web_client()
response = client.get("/")
assert response.status_code == 200
assert response.request.path == "/"
=== END AC reading-list-empty ===

## User Acceptance

- A reader can open the primary page and understand whether books are present.
- Books appear in the order they were added.

## Guardrails

- The route never silently reorders books.
- Removed books are absent on the next read.
- Empty titles and authors are never displayed.
