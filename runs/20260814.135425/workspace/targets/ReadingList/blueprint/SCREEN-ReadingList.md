# SCREEN: Reading List

| Field       | Value |
|-------------|-------|
| Version     | 20260814 V1 |
| Description | Defines the browser screen for viewing and managing the ordered reading list. |
| Depends On  | ARCHITECTURE.md, DATABASE.md, FEATURE-AddBook.md, FEATURE-ValidateBook.md, FEATURE-OrderAndStatus.md, FEATURE-RemoveBook.md, FEATURE-MarkRead.md |
| Provides    | GET / |
| Consumes     | GET /, POST /books, POST /books/{id}/read, POST /books/{id}/delete |
| Route       | / |
| Parent      | — |
| Main Menu   | Reading List (1) |
| Sub Menu    | — |
| Tab Order   | 1 |

## Layout and Interactions

The screen contains:

- a page heading identifying the reading list;
- an add-book form with title and author fields;
- the current books in insertion order;
- each book's title, author, and unread/read state;
- a mark-read control for unread books;
- a remove control for each book;
- a useful empty state when no books exist.

The screen submits the form to `POST /books`, marks books read through `POST /books/{id}/read`, and removes books through `POST /books/{id}/delete`. After each operation, the screen displays the resulting collection.

While a request is loading, the interface presents a loading state appropriate to the rendered interaction.

## Programmatic Acceptance

Requires: python-package=flask; scope=runtime

=== AC screen-root ===
Intent: The reading-list screen is reachable and returns a successful response.
from app import create_app

app = create_app({"TESTING": True, "READING_LIST_DATABASE": ":memory:"})
client = app.test_client()
response = client.get("/")
assert response.status_code == 200
=== END AC screen-root ===

=== AC screen-empty-state ===
Intent: An empty collection can be rendered successfully.
from app import create_app

app = create_app({"TESTING": True, "READING_LIST_DATABASE": ":memory:"})
client = app.test_client()
response = client.get("/")
assert response.status_code == 200
assert response.data is not None
=== END AC screen-empty-state ===

=== AC screen-workflow-routes ===
Intent: The screen can invoke each declared book workflow route.
from app import create_app
from app.database import Database

database_path = "acceptance-screen.sqlite"
app = create_app({"TESTING": True, "READING_LIST_DATABASE": database_path})
client = app.test_client()
title = "Screen Book"
author = "Screen Author"

created_response = client.post("/books", data={"title": title, "author": author})
assert created_response.status_code in (200, 302, 303)

book = Database(database_path).list_books()[0]
read_response = client.post(f"/books/{book.id}/read")
assert read_response.status_code in (200, 302, 303)

delete_response = client.post(f"/books/{book.id}/delete")
assert delete_response.status_code in (200, 302, 303)

final_response = client.get("/")
assert final_response.status_code == 200
=== END AC screen-workflow-routes ===

## User Acceptance

- A reader can identify the reading-list screen, add-book form, current books, status controls, and removal controls.
- While an interaction is loading, the interface presents a recognizable loading state.

## Guardrails

- Books remain in addition order.
- Every displayed book shows unread or read status.
- Invalid submissions are not displayed.
- The screen must not expose raw database details.
