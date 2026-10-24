# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 8972
- execution id: 20261023.211018.519Z-310bad70

## Stories built
- Serve the ordered reading-list view. (reading-list) [story]
- Add a valid book to the reading list. (add-book) [story]
- Remove a selected book from the reading list. (remove-book) [story]
- Reject incomplete book submissions with correction feedback. (validate-book) [story]

## Reusable compacts
- DATABASE_compact.md

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 551)
- implements: FEATURE-READING-LIST.md (SP 732)
- context: ARCHITECTURE_compact.md (SP 129)
- context: DATABASE.md (SP 1361)
- stack: flask.md (SP 451)
- stack: persistence.md (SP 2816)
- implements: FEATURE-ADD-BOOK.md (SP 590)
- implements: FEATURE-REMOVE-BOOK.md (SP 669)
- implements: FEATURE-VALIDATE-BOOK.md (SP 861)

## Build directory changes
- app_server/__init__.py
- app_server/config.py
- app_server/features/reading_list/routes.py
- data/app.db
- tests/test_architecture.py

## Pre-build acceptance observation
- GREEN (prepassed): reading-list-reachable (FEATURE-READING-LIST.md)
  intent: The primary reading-list route is reachable and returns a successful page response.
  return code: 0
- RED: reading-list-order (FEATURE-READING-LIST.md)
  intent: The reading-list route presents persisted books in insertion order.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      first_title = 'Reading List First'
      body = '<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n  <title>Reading List</title>\n  <link rel="stylesheet" href="/static/reading-list.css">\n</head>\n<body><main class="page-shell">\n  <header class="page-header"><p class="eyebrow">ReadingList</p><h1>Books to read</h1><p class="intro">Keep track of the books you… (+1274 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "reading-list-order.py", line 26, in <module>
        first_position = body.index(first_title)
                         ^^^^^^^^^^^^^^^^^^^^^^^
    ValueError: substring not found
- GREEN (prepassed): reading-list-empty (FEATURE-READING-LIST.md)
  intent: The reading-list route successfully renders when no matching books are present.
  return code: 0
- RED: add-book-route (FEATURE-ADD-BOOK.md)
  intent: The book-creation route accepts a valid title and author submission.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "add-book-route.py", line 11, in <module>
        assert response.status_code == 302
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: add-book-persistence (FEATURE-ADD-BOOK.md)
  intent: A valid submission is persisted and readable through the public list workflow.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "add-book-persistence.py", line 11, in <module>
        assert created_response.status_code == 302
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: remove-book-route (FEATURE-REMOVE-BOOK.md)
  intent: The removal route deletes the selected book and returns to the reading-list workflow.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "remove-book-route.py", line 17, in <module>
        assert response.status_code == 302
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): remove-book-readback (FEATURE-REMOVE-BOOK.md)
  intent: Removing a book changes subsequent persisted reads so the selected identifier is absent.
  return code: 0
- RED: validate-book-route (FEATURE-VALIDATE-BOOK.md)
  intent: The book submission route rejects an empty title with a client-error response and does not persist the invalid submission.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "validate-book-route.py", line 10, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: validate-book-author (FEATURE-VALIDATE-BOOK.md)
  intent: The book submission route rejects an empty author with a client-error response and does not persist the invalid submission.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "validate-book-author.py", line 10, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: validate-book-correction (FEATURE-VALIDATE-BOOK.md)
  intent: A reader can correct an invalid submission and successfully add the corrected book.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "validate-book-correction.py", line 13, in <module>
        assert invalid_response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: reading-list-reachable (FEATURE-READING-LIST.md)
  intent: The primary reading-list route is reachable and returns a successful page response.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reading-list-order (FEATURE-READING-LIST.md)
  intent: The reading-list route presents persisted books in insertion order.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reading-list-empty (FEATURE-READING-LIST.md)
  intent: The reading-list route successfully renders when no matching books are present.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: add-book-route (FEATURE-ADD-BOOK.md)
  intent: The book-creation route accepts a valid title and author submission.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: add-book-persistence (FEATURE-ADD-BOOK.md)
  intent: A valid submission is persisted and readable through the public list workflow.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-book-route (FEATURE-REMOVE-BOOK.md)
  intent: The removal route deletes the selected book and returns to the reading-list workflow.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-book-readback (FEATURE-REMOVE-BOOK.md)
  intent: Removing a book changes subsequent persisted reads so the selected identifier is absent.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validate-book-route (FEATURE-VALIDATE-BOOK.md)
  intent: The book submission route rejects an empty title with a client-error response and does not persist the invalid submission.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validate-book-author (FEATURE-VALIDATE-BOOK.md)
  intent: The book submission route rejects an empty author with a client-error response and does not persist the invalid submission.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: validate-book-correction (FEATURE-VALIDATE-BOOK.md)
  intent: A reader can correct an invalid submission and successfully add the corrected book.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0

## Repair attempts
- attempt 0 (initial build): failed; 10/10 checks model=gpt-5.6-luna; execution 20261023.210837.317Z-0f9e54ab; reason: acceptance regression: database-books-create, database-books-list, database-books-delete
- attempt 1 (repair 1): built; 10/10 checks model=gpt-5.6-luna; execution 20261023.211018.519Z-310bad70

## Build summary
<reusable-compact filename="DATABASE.md">
Persistence provides `persistence.books` with:

- `list()` → ordered `BookRow[]`
- `create(title, author, insertion_order)` → `BookRow`
- `delete(id)` → `DeletedBook`

Books require non-empty title/author, retain insertion order, and use generated persistence only. Schema: `books(id, title, author, insertion_order UNIQUE)`.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- app_server/features/reading_list/routes.py

SUMMARY:
Implemented centralized ordered book reads for the list and validation workflows. Database regressions and all declared acceptance probes pass. `sh sources/full_test.sh`: 9 passed.

BLOCKERS:
- None
