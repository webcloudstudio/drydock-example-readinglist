# SCREEN: Reading List

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | The single page where a reader adds books, sees them in the order added, sees rejection reasons, and removes books. |
| Depends On | FEATURE-ListBooks.md, FEATURE-RemoveBook.md, FEATURE-RejectEmptyTitle.md, FEATURE-RejectEmptyAuthor.md, UI-GENERAL.md |
| Provides | GET / |
| Consumes | GET /books, POST /books, POST /books/{id}/delete |
| Route | / |
| Parent | — |
| Main Menu | Reading List (1) |
| Tab Order | — |

## Purpose

One page for the reader to track what they intend to read, in the order they added it.

## Layout

Rendered inside the shared base layout from `UI-GENERAL.md`:

1. Error region: shows the rejection reason when a submission was rejected; empty otherwise.
2. Add form: text inputs `title` and `author`, and a submit button, posting to `POST /books`.
3. Book list: an ordered list of books in insertion order. Each entry shows title and author and a remove form posting to `POST /books/{id}/delete`.
4. When no books exist the list area shows an empty-state message.

## Interactions

| Interaction | Route | Result |
|-------------|-------|--------|
| Open the page | `GET /` | Page lists every stored book in the order added |
| Submit the add form | `POST /books` | Valid: 303 redirect back to `/`. Rejected: 400 and the page re-rendered with the reason |
| Press remove on a book | `POST /books/{id}/delete` | 303 redirect back to `/`; the book is gone on the next read |
| Read the list as data | `GET /books` | JSON array of `id`, `title`, `author` in insertion order |

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md.

## Programmatic Acceptance

=== AC screen-index-reachable ===
Intent: The reading list page at GET / answers 200 and GET /books answers 200 with a JSON array.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client

client = web_client()
page = client.get("/")
assert page.status_code == 200
assert len(page.data) > 0
listing = client.get("/books")
assert listing.status_code == 200
assert isinstance(listing.get_json(), list)
=== END AC screen-index-reachable ===

=== AC screen-shows-books-in-order ===
Intent: Books added through POST /books appear on GET / in the order they were added, with GET /books agreeing.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

author = "ScreenOrderAuthor01"
titles = ["ScreenOrderAlpha", "ScreenOrderBravo", "ScreenOrderCharlie"]


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.author == author:
                db.books.delete(id=row.id)


client = web_client()
purge()
try:
    for t in titles:
        response = client.post("/books", data={"title": t, "author": author})
        assert response.status_code == 303
    html = client.get("/").get_data(as_text=True)
    positions = [html.find(t) for t in titles]
    assert all(p >= 0 for p in positions)
    assert positions == sorted(positions)
    data = client.get("/books").get_json()
    ours = [row["title"] for row in data if row["author"] == author]
    assert ours == titles
finally:
    purge()
=== END AC screen-shows-books-in-order ===

=== AC screen-rejection-shown ===
Intent: A rejected browser submission is answered 400 with a page, stores nothing, and the page remains reachable.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

marker = "ScreenRejectAuthor02"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.author == marker:
                db.books.delete(id=row.id)


client = web_client()
purge()
try:
    response = client.post("/books", data={"title": "", "author": marker})
    assert response.status_code == 400
    assert len(response.data) > 0
    with committed_session() as db:
        assert len([r for r in db.books.list() if r.author == marker]) == 0
    assert client.get("/").status_code == 200
finally:
    purge()
=== END AC screen-rejection-shown ===

=== AC screen-remove-book ===
Intent: Posting to the remove route redirects with 303 and the book is absent from GET / and GET /books on the next read.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

author = "ScreenRemoveAuthor03"
keep_title = "ScreenRemoveKeep"
drop_title = "ScreenRemoveDrop"
route = "/books/{id}/delete"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.author == author:
                db.books.delete(id=row.id)


client = web_client()
purge()
try:
    assert client.post("/books", data={"title": keep_title, "author": author}).status_code == 303
    assert client.post("/books", data={"title": drop_title, "author": author}).status_code == 303
    rows = [r for r in client.get("/books").get_json() if r["author"] == author]
    drop_id = [r["id"] for r in rows if r["title"] == drop_title][0]
    response = client.post(route.format(id=drop_id))
    assert response.status_code == 303
    after = [r["title"] for r in client.get("/books").get_json() if r["author"] == author]
    assert after == [keep_title]
    html = client.get("/").get_data(as_text=True)
    assert drop_title not in html
    assert keep_title in html
finally:
    purge()
=== END AC screen-remove-book ===

## User Acceptance

- The page reads clearly: the add form, the rejection reason, and the remove controls are easy to find and understand.

## Guardrails

- The page never presents books in any order other than the order added.
- A rejected submission always shows its reason.
- The page never reaches the store directly; it renders data from the feature routes.
