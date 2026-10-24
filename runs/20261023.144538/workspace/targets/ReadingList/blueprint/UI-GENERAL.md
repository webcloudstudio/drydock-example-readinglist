# UI-GENERAL: ReadingList

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | Shared page layout and error region used by every ReadingList page. |
| Depends On | ARCHITECTURE.md, DATABASE.md |
| Provides | base layout template |

## Layout

All pages extend `app_server/templates/base.html`.

| Element | Template name | Behavior |
|---------|---------------|----------|
| Page title | `block title` | Defaults to `Reading List` |
| Main content | `block content` | Filled by each page |
| Error region | variable `error` | When `error` is set and non-empty, an element with `role="alert"` shows the text; otherwise nothing is rendered |

## Wiring

`create_app()` configures the Jinja template folder `app_server/templates` and initializes persistence through `open_database(...)` using the configured store. No book routes are registered by this story.

## Programmatic Acceptance

=== AC ui-base-template-loads ===
Intent: The base layout template is available to the application.
Suite: scoped

from app_server import create_app

app = create_app()
template = app.jinja_env.get_template("base.html")
assert template is not None
=== END AC ui-base-template-loads ===

=== AC ui-base-shows-error ===
Intent: The base layout renders the supplied error text in its error region.
Suite: scoped

from flask import render_template
from app_server import create_app

app = create_app()
message = "bound error reason"
with app.test_request_context("/"):
    html = render_template("base.html", error=message)
assert message in html
=== END AC ui-base-shows-error ===

=== AC ui-base-without-error ===
Intent: The base layout renders without an error and does not show an alert region.
Suite: scoped

from flask import render_template
from app_server import create_app

app = create_app()
with app.test_request_context("/"):
    html = render_template("base.html")
assert 'role="alert"' not in html
=== END AC ui-base-without-error ===

## User Acceptance

- The page looks clean and readable in a browser.

## Guardrails

- The layout never hides a supplied error message.
