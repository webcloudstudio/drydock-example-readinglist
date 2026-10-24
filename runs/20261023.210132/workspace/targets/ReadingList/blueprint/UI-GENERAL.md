# UI-GENERAL: Reading List Interface

| Field       | Value |
|-------------|-------|
| Version     | 20261023 V1 |
| Description | Shared server-rendered interface patterns for the ReadingList application. |
| Depends On  | ARCHITECTURE.md |
| Provides    | shared reading-list layout and feedback patterns |
| Consumes    | `app_server.create_app` |

## Interface Patterns

The page uses a consistent server-rendered layout with a clear page title, an add-book form, accessible labels for title and author, a list region, and action controls.

The list displays books in the order supplied by the reading-list feature. When no books exist, the page presents a clear empty-list state. Validation failures preserve the form workflow and expose field-specific feedback without discarding the submitted values.

Controls use ordinary HTML form submission and remain usable without undocumented client-side behavior.

## Programmatic Acceptance

=== AC ui-general-client ===
Intent: The shared interface is available through the application's published testing client.

from app_server.testing import web_client

client = web_client()
response = client.get("/")
assert response.status_code == 200
assert response.request.path == "/"
=== END AC ui-general-client ===

=== AC ui-general-form ===
Intent: The primary interface accepts the declared book form fields.

from app_server.testing import web_client

title = "Interface Acceptance Title"
author = "Interface Acceptance Author"

client = web_client()
response = client.post(
    "/books",
    data={"title": title, "author": author},
)
assert response.status_code in (200, 302, 303)
=== END AC ui-general-form ===

## User Acceptance

- The page is understandable to a reader without instructions outside the page.
- Empty-list and validation states are visually clear.

## Guardrails

- The interface never displays a book with an empty title or author.
- Validation feedback leaves the reader able to correct and resubmit.
- Books are displayed in stored insertion order.
