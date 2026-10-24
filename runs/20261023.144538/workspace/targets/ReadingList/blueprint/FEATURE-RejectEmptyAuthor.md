# FEATURE: Reject Empty Author

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | A book submission whose author is empty is rejected with a reported reason and nothing is stored. |
| Depends On | FEATURE-AddBook.md, UI-GENERAL.md |
| Provides | None |
| Consumes | POST /books |

## Purpose

The reader must never be able to add a book without an author. The submission is rejected and the reader is told why.

## Trigger

A reader submits `POST /books` where the `author` form field is missing, empty, or whitespace-only.

## Sequence

1. `POST /books` receives form fields `title` and `author`.
2. The author is trimmed. If the trimmed author is empty, validation fails. Title is checked first, so this rejection names `author` only when the title is valid.
3. The route answers status 400 and stores nothing.
4. If the request carries `Accept: application/json`, the body is JSON with `error` (a non-empty reason string) and `field` equal to `author`.
5. Otherwise the page is re-rendered in the shared layout's error region with the reason shown, still with status 400.

## Routes

| Route | Behavior |
|-------|----------|
| `POST /books` | Extended by this feature with author validation; valid submissions remain owned by FEATURE-AddBook.md |

## Reads

None.

## Writes

None. A rejected submission writes nothing.

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md.

## Programmatic Acceptance

=== AC reject-author-empty-json ===
Intent: An empty author on POST /books answers 400 with a non-empty reason naming the author field and stores nothing.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

marker = "RejAuthorEmptyTitle01"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.title == marker:
                db.books.delete(id=row.id)


def stored():
    with committed_session() as db:
        return [row for row in db.books.list() if row.title == marker]


client = web_client()
purge()
try:
    response = client.post(
        "/books",
        data={"title": marker, "author": ""},
        headers={"Accept": "application/json"},
    )
    assert response.status_code == 400
    body = response.get_json()
    assert isinstance(body["error"], str)
    assert body["error"].strip()
    assert body["field"] == "author"
    assert len(stored()) == 0
finally:
    purge()
=== END AC reject-author-empty-json ===

=== AC reject-author-whitespace ===
Intent: A whitespace-only author is treated as empty, rejected with 400, and nothing is stored.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

marker = "RejAuthorBlankTitle02"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.title == marker:
                db.books.delete(id=row.id)


def stored():
    with committed_session() as db:
        return [row for row in db.books.list() if row.title == marker]


client = web_client()
purge()
try:
    response = client.post(
        "/books",
        data={"title": marker, "author": "   "},
        headers={"Accept": "application/json"},
    )
    assert response.status_code == 400
    body = response.get_json()
    assert body["error"].strip()
    assert body["field"] == "author"
    assert len(stored()) == 0
finally:
    purge()
=== END AC reject-author-whitespace ===

=== AC reject-author-missing ===
Intent: A POST /books with no author field at all is rejected with 400 and nothing is stored.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

marker = "RejAuthorMissingTitle03"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.title == marker:
                db.books.delete(id=row.id)


def stored():
    with committed_session() as db:
        return [row for row in db.books.list() if row.title == marker]


client = web_client()
purge()
try:
    response = client.post(
        "/books",
        data={"title": marker},
        headers={"Accept": "application/json"},
    )
    assert response.status_code == 400
    body = response.get_json()
    assert body["error"].strip()
    assert body["field"] == "author"
    assert len(stored()) == 0
finally:
    purge()
=== END AC reject-author-missing ===

=== AC reject-author-html ===
Intent: A browser submission with an empty author is answered 400 with a re-rendered page and nothing is stored.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

marker = "RejAuthorHtmlTitle04"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.title == marker:
                db.books.delete(id=row.id)


def stored():
    with committed_session() as db:
        return [row for row in db.books.list() if row.title == marker]


client = web_client()
purge()
try:
    response = client.post("/books", data={"title": marker, "author": ""})
    assert response.status_code == 400
    assert len(response.data) > 0
    assert len(stored()) == 0
finally:
    purge()
=== END AC reject-author-html ===

## User Acceptance

- None.

## Guardrails

- Never accept an empty author.
- Never reject a submission without a non-empty reason.
- Never store a book from a rejected submission.
