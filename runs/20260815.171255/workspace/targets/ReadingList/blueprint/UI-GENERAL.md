# UI-GENERAL: Reading List Presentation

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Defines shared accessible presentation patterns for the single-screen reading-list interface. |
| Depends On  | ARCHITECTURE.md |
| Provides    | reading_list_ui_patterns |
| Consumes    | application_factory |

## Presentation Patterns

The reading-list screen uses a simple responsive page with:

- A clear page heading identifying the reading list.
- A book-submission form containing required title and author inputs.
- A submit control with an understandable action label.
- An ordered list of books, showing each title with its author.
- A removal control associated with each listed book.
- A clear empty-list message when no books exist.
- A visible validation-error region when a submission is rejected.

Controls must have labels, inputs must have stable names, and each removal control must identify its target book without relying on position alone. Error presentation must identify the missing required field or fields.

## CSS Patterns

Styles should provide readable typography, visible focus states, sufficient contrast, and usable spacing on narrow and wide screens. Styling must not change the order of books or hide validation errors.

## Programmatic Acceptance

=== AC ui-patterns-form ===
Intent: The shared presentation includes labeled title and author controls and a submission control.

from app import create_app

application = create_app({"TESTING": True, "DATABASE": ":memory:"})
response = application.test_client().get("/")
body = response.get_data(as_text=True)

assert response.status_code == 200
assert 'name="title"' in body
assert 'name="author"' in body
assert "<form" in body
=== END AC ui-patterns-form ===

=== AC ui-patterns-empty-state ===
Intent: The shared presentation provides a reader-visible empty-list state.

from app import create_app

application = create_app({"TESTING": True, "DATABASE": ":memory:"})
body = application.test_client().get("/").get_data(as_text=True)

assert body
assert "reading" in body.lower()
assert "empty" in body.lower() or "no books" in body.lower()
=== END AC ui-patterns-empty-state ===

=== AC ui-patterns-removal-control ===
Intent: The shared presentation provides a removal control for a listed book.

from app import create_app

title = "Listed Book"
author = "Listed Author"
application = create_app({"TESTING": True, "DATABASE": ":memory:"})
client = application.test_client()
response = client.post("/books", data={"title": title, "author": author})
assert response.status_code in (302, 303)
body = client.get("/").get_data(as_text=True)

assert title in body
assert author in body
assert "remove" in body.lower() or "delete" in body.lower()
=== END AC ui-patterns-removal-control ===

## User Acceptance

- None.

## Guardrails

- The interface must provide a direct path to submit both required book fields.
- The list must remain in insertion order.
- Validation errors must remain visible and understandable.
