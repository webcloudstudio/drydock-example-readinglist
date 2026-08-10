# Evidence: Block 2 · Service (block-2)

- block type: block
- date: 2026-08-10
- resulting state: closed/verified
- story points (combined assembled cost): 6975
- execution id: 20260810.215934.742Z-b9ec3e6b

## Stories built
- Store a submitted book with its title and author. (add-book) [story]
- Remove a selected book from the reading list. (remove-book) [story]
- Retrieve books in insertion order. (list-books) [story]
- Reject book submissions with an empty title or author. (validate-book) [story]

## Acceptance tooling authorization
- FEATURE-Add-Book.md#add-route: python-package=flask; scope=test; authorization=existing Target dependency manifest
- FEATURE-Remove-Book.md#removes-selected-book: python-package=flask; scope=test; authorization=existing Target dependency manifest
- FEATURE-List-Books.md#list-route: python-package=flask; scope=test; authorization=existing Target dependency manifest
- FEATURE-Validate-Book.md#rejects-empty-title: python-package=flask; scope=test; authorization=existing Target dependency manifest

## Reusable compacts
- FEATURE-Add-Book_compact.md
- FEATURE-Remove-Book_compact.md
- FEATURE-List-Books_compact.md
- FEATURE-Validate-Book_compact.md

## Stacked context
- compass: COMPASS.md (SP 685)
- implements: FEATURE-Add-Book.md (SP 698)
- context: ARCHITECTURE_compact.md (SP 109)
- context: DATABASE_compact.md (SP 113)
- stack: python_compact.md (SP 1534)
- stack: flask_compact.md (SP 1083)
- stack: sqlite_compact.md (SP 876)
- implements: FEATURE-Remove-Book.md (SP 591)
- implements: FEATURE-List-Books.md (SP 613)
- implements: FEATURE-Validate-Book.md (SP 515)

## Build directory changes
- persistence.py
- routes.py
- tests/test_acceptance.py

## Pre-build acceptance observation
- RED: add-route (FEATURE-Add-Book.md)
  intent: The add route accepts a valid title and author.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: add-round-trip (FEATURE-Add-Book.md)
  intent: A successful add is visible through the public list route.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: add-requires-both-fields (FEATURE-Add-Book.md)
  intent: A valid add creates a record containing both required fields.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: removes-selected-book (FEATURE-Remove-Book.md)
  intent: A selected book is absent after removal.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: preserves-other-books (FEATURE-Remove-Book.md)
  intent: Removing one book does not remove other books.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: unknown-book-removal (FEATURE-Remove-Book.md)
  intent: Removing an unknown book does not create or alter a book.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: list-route (FEATURE-List-Books.md)
  intent: The list route is reachable and returns an empty collection for a new store.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: list-round-trip (FEATURE-List-Books.md)
  intent: The list route returns books persisted through the add workflow.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: list-preserves-order (FEATURE-List-Books.md)
  intent: The route preserves insertion order independently of request order.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: rejects-empty-title (FEATURE-Validate-Book.md)
  intent: An empty title is rejected before persistence.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: rejects-empty-author (FEATURE-Validate-Book.md)
  intent: An empty author is rejected before persistence.
  error: baseline unavailable: authorized Target tooling is not provisioned
- RED: accepts-complete-submission (FEATURE-Validate-Book.md)
  intent: A submission with a non-empty title and author is not rejected by validation.
  error: baseline unavailable: authorized Target tooling is not provisioned

## Build summary
<reusable-compact filename="FEATURE-Add-Book.md">
POST /books accepts non-whitespace title and author form fields, validates before persistence, stores via BookStore.add, and redirects to the reading-list view. GET /books returns stored records as JSON with id, title, and author.
</reusable-compact>

<reusable-compact filename="FEATURE-Remove-Book.md">
POST /books/{id}/remove removes only the selected local record. Subsequent GET /books omits it while preserving remaining insertion order. Unknown IDs return an allowed not-found or no-op response.
</reusable-compact>

<reusable-compact filename="FEATURE-List-Books.md">
GET /books returns HTTP 200 with a JSON array from BookStore.list, ordered by insertion. An empty store returns [].
</reusable-compact>

<reusable-compact filename="FEATURE-Validate-Book.md">
POST /books rejects empty or whitespace-only title or author with HTTP 400 before persistence. Valid submissions continue to persistence.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- routes.py
- persistence.py
- tests/test_acceptance.py

SUMMARY:
Implemented JSON listing, validated add flow, selected-book removal with unknown-ID handling, and comprehensive acceptance tests. Full suite: 16 passed. Ruff passed.

BLOCKERS:
- None
