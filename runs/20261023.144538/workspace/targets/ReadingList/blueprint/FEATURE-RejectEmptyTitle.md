# FEATURE: Reject Empty Title

| Field | Value |
|-------|-------|
| Version | 20261023 V1 |
| Description | A book submission whose title is empty is rejected with a reported reason and nothing is stored. |
| Depends On | FEATURE-AddBook.md, UI-GENERAL.md |
| Provides | None |
| Consumes | POST /books |

## Purpose

The reader must never be able to add a book without a title. The submission is rejected and the reader is told why.

## Trigger

A reader submits `POST /books` where the `title` form field is missing, empty, or whitespace-only.

## Sequence

1. `POST /books` receives form fields `title` and `author`.
2. The title is trimmed. If the trimmed title is empty, validation fails. Title is checked before author, so when both are empty the rejection names `title`.
3. The route answers status 400 and stores nothing.
4. If the request carries `Accept: application/json`, the body is JSON with `error` (a non-empty reason string) and `field` equal to `title`.
5. Otherwise the page is re-rendered in the shared layout's error region with the reason shown, still with status 400.

## Routes

| Route | Behavior |
|-------|----------|
| `POST /books` | Extended by this feature with title validation; valid submissions remain owned by FEATURE-AddBook.md |

## Reads

None.

## Writes

None. A rejected submission writes nothing.

## Database Interface

- None — persistence is owned by FEATURE-AddBook.md.

## Programmatic Acceptance

=== AC reject-title-empty-json ===
Intent: An empty title on POST /books answers 400 with a non-empty reason naming the title field and stores nothing.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

marker = "RejTitleEmptyAuthor01"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.author == marker:
                db.books.delete(id=row.id)


def stored():
    with committed_session() as db:
        return [row for row in db.books.list() if row.author == marker]


client = web_client()
purge()
try:
    response = client.post(
        "/books",
        data={"title": "", "author": marker},
        headers={"Accept": "application/json"},
    )
    assert response.status_code == 400
    body = response.get_json()
    assert isinstance(body["error"], str)
    assert body["error"].strip()
    assert body["field"] == "title"
    assert len(stored()) == 0
finally:
    purge()
=== END AC reject-title-empty-json ===

=== AC reject-title-whitespace ===
Intent: A whitespace-only title is treated as empty, rejected with 400, and nothing is stored.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

marker = "RejTitleBlankAuthor02"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.author == marker:
                db.books.delete(id=row.id)


def stored():
    with committed_session() as db:
        return [row for row in db.books.list() if row.author == marker]


client = web_client()
purge()
try:
    response = client.post(
        "/books",
        data={"title": "   ", "author": marker},
        headers={"Accept": "application/json"},
    )
    assert response.status_code == 400
    body = response.get_json()
    assert body["error"].strip()
    assert body["field"] == "title"
    assert len(stored()) == 0
finally:
    purge()
=== END AC reject-title-whitespace ===

=== AC reject-title-missing ===
Intent: A POST /books with no title field at all is rejected with 400 and nothing is stored.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

marker = "RejTitleMissingAuthor03"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.author == marker:
                db.books.delete(id=row.id)


def stored():
    with committed_session() as db:
        return [row for row in db.books.list() if row.author == marker]


client = web_client()
purge()
try:
    response = client.post(
        "/books",
        data={"author": marker},
        headers={"Accept": "application/json"},
    )
    assert response.status_code == 400
    body = response.get_json()
    assert body["error"].strip()
    assert body["field"] == "title"
    assert len(stored()) == 0
finally:
    purge()
=== END AC reject-title-missing ===

=== AC reject-title-html ===
Intent: A browser submission with an empty title is answered 400 with a re-rendered page and nothing is stored.
Suite: scoped
Requires: python-package=pytest; scope=test

from app_server.testing import web_client
from persistence.testing import committed_session

marker = "RejTitleHtmlAuthor04"


def purge():
    with committed_session() as db:
        for row in db.books.list():
            if row.author == marker:
                db.books.delete(id=row.id)


def stored():
    with committed_session() as db:
        return [row for row in db.books.list() if row.author == marker]


client = web_client()
purge()
try:
    response = client.post("/books", data={"title": "", "author": marker})
    assert response.status_code == 400
    assert len(response.data) > 0
    assert len(stored()) == 0
finally:
    purge()
=== END AC reject-title-html ===

## User Acceptance

- None.

## Guardrails

- Never accept an empty title.
- Never reject a submission without a non-empty reason.
- Never store a book from a rejected submission.
