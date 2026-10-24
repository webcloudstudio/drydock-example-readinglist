# Evidence: Block 3 · Service (block-3)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 10531
- execution id: 20261023.175350.426Z-06f129a2

## Stories built
- Add a book with a title and author and persist it. (add-book) [story]
- List books in the order they were added. (list-books) [story]
- Remove a book so it no longer appears in the list. (remove-book) [story]
- Reject a submission with an empty title or author with a clear error. (reject-empty-fields) [story]

## Acceptance tooling authorization
- FEATURE-AddBook.md#addbook-create: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-AddBook.md#addbook-persisted: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-AddBook.md#addbook-ascending-ids: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-ListBooks.md#listbooks-order: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-ListBooks.md#listbooks-fields: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-ListBooks.md#listbooks-reachable: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-RejectEmptyFields.md#reject-empty-title: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-RejectEmptyFields.md#reject-empty-author: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-RejectEmptyFields.md#reject-both-empty: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-RejectEmptyFields.md#reject-whitespace-and-missing: python-package=flask; scope=test; authorization=existing Target environment
- FEATURE-RejectEmptyFields.md#reject-valid-still-accepted: python-package=flask; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 895)
- implements: FEATURE-AddBook.md (SP 1569)
- context: ARCHITECTURE_compact.md (SP 424)
- context: DATABASE_compact.md (SP 317)
- stack: flask.md (SP 691)
- implements: FEATURE-ListBooks.md (SP 1384)
- implements: FEATURE-RemoveBook.md (SP 1774)
- implements: FEATURE-RejectEmptyFields.md (SP 2092)

## Build directory changes
- app_server/__init__.py
- app_server/routes/books.py
- app_server/services/__init__.py
- app_server/services/books.py
- data/app.db
- tests/conftest.py
- tests/test_add_book.py
- tests/test_app_shell.py
- tests/test_books_service.py
- tests/test_list_books.py
- tests/test_reject_empty_fields.py
- tests/test_remove_book.py

## Pre-build acceptance observation
- RED: addbook-create (FEATURE-AddBook.md)
  intent: POST /books answers 201 and returns the title and author that were supplied, with an id.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "addbook-create.py", line 10, in <module>
        assert response.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: addbook-persisted (FEATURE-AddBook.md)
  intent: A submitted book is read back from the store with the supplied title and author.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "addbook-persisted.py", line 9, in <module>
        assert response.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: addbook-ascending-ids (FEATURE-AddBook.md)
  intent: Two books added in sequence receive ascending ids, preserving insertion order.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "addbook-ascending-ids.py", line 9, in <module>
        assert response.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: listbooks-order (FEATURE-ListBooks.md)
  intent: GET /books returns the books added during the check in the order they were added.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "listbooks-order.py", line 10, in <module>
        assert response.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: listbooks-fields (FEATURE-ListBooks.md)
  intent: Each listed book carries the supplied title and author and its id.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "listbooks-fields.py", line 10, in <module>
        assert response.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: listbooks-reachable (FEATURE-ListBooks.md)
  intent: GET /books is reachable and returns a JSON array even when no check data exists.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "listbooks-reachable.py", line 4, in <module>
        assert response.status_code == 200
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: remove-book-deletes (FEATURE-RemoveBook.md)
  intent: Removing an added book answers 204 and the book is absent from the next list read.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "remove-book-deletes.py", line 8, in <module>
        assert created.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: remove-book-unknown-id (FEATURE-RemoveBook.md)
  intent: Removing an id that does not exist answers 404, and removing the same id twice answers 404 the second time.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "remove-book-unknown-id.py", line 7, in <module>
        assert created.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: remove-book-preserves-order (FEATURE-RemoveBook.md)
  intent: Removing the middle book leaves the other books in the order they were added.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "remove-book-preserves-order.py", line 10, in <module>
        assert resp.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: reject-empty-title (FEATURE-RejectEmptyFields.md)
  intent: POST /books with an empty title answers 400 and stores nothing.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "reject-empty-title.py", line 8, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: reject-empty-author (FEATURE-RejectEmptyFields.md)
  intent: POST /books with an empty author answers 400 and stores nothing.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "reject-empty-author.py", line 8, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: reject-both-empty (FEATURE-RejectEmptyFields.md)
  intent: POST /books with both fields empty answers 400 and stores nothing.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "reject-both-empty.py", line 8, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: reject-whitespace-and-missing (FEATURE-RejectEmptyFields.md)
  intent: Whitespace-only and missing fields are rejected with 400 and nothing is stored.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "reject-whitespace-and-missing.py", line 15, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: reject-validator (FEATURE-RejectEmptyFields.md)
  intent: validate_book_input raises ValueError for an empty title or author.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "reject-validator.py", line 1, in <module>
        from app_server.services.books import validate_book_input
    ModuleNotFoundError: No module named 'app_server.services'
- RED: reject-valid-still-accepted (FEATURE-RejectEmptyFields.md)
  intent: A submission with both fields present is still accepted with 201 after validation is in place.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "reject-valid-still-accepted.py", line 9, in <module>
        assert response.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: addbook-create (FEATURE-AddBook.md)
  intent: POST /books answers 201 and returns the title and author that were supplied, with an id.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: addbook-persisted (FEATURE-AddBook.md)
  intent: A submitted book is read back from the store with the supplied title and author.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: addbook-ascending-ids (FEATURE-AddBook.md)
  intent: Two books added in sequence receive ascending ids, preserving insertion order.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: listbooks-order (FEATURE-ListBooks.md)
  intent: GET /books returns the books added during the check in the order they were added.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: listbooks-fields (FEATURE-ListBooks.md)
  intent: Each listed book carries the supplied title and author and its id.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: listbooks-reachable (FEATURE-ListBooks.md)
  intent: GET /books is reachable and returns a JSON array even when no check data exists.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-book-deletes (FEATURE-RemoveBook.md)
  intent: Removing an added book answers 204 and the book is absent from the next list read.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-book-unknown-id (FEATURE-RemoveBook.md)
  intent: Removing an id that does not exist answers 404, and removing the same id twice answers 404 the second time.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-book-preserves-order (FEATURE-RemoveBook.md)
  intent: Removing the middle book leaves the other books in the order they were added.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reject-empty-title (FEATURE-RejectEmptyFields.md)
  intent: POST /books with an empty title answers 400 and stores nothing.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reject-empty-author (FEATURE-RejectEmptyFields.md)
  intent: POST /books with an empty author answers 400 and stores nothing.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reject-both-empty (FEATURE-RejectEmptyFields.md)
  intent: POST /books with both fields empty answers 400 and stores nothing.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reject-whitespace-and-missing (FEATURE-RejectEmptyFields.md)
  intent: Whitespace-only and missing fields are rejected with 400 and nothing is stored.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reject-validator (FEATURE-RejectEmptyFields.md)
  intent: validate_book_input raises ValueError for an empty title or author.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reject-valid-still-accepted (FEATURE-RejectEmptyFields.md)
  intent: A submission with both fields present is still accepted with 201 after validation is in place.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
Block 3 is the four book stories: the service layer, the `/books` routes, and their tests. `bin/test.sh` belongs to a later story, so I'll leave it alone. Before writing anything, I'll confirm the existing suite runs in this environment.Baseline is 25 passing. No new dependencies are needed, so I'll write the service layer first.I split the Flask import across two lines in the routes file. I'll merge it, then wire the blueprint into the factory.The app-shell test asserts that only `/health` is registered, which this block changes by design. I'll update it to the expected route set, then add an isolated-store fixture to conftest so the HTTP tests can cover an empty list and reopening the store.The fixtures are in place. I'll add a `fresh_db` handle fixture, then write the service-level and HTTP-level tests. Each test reads state back through the public interface.I wrote the first list-order test sloppily (a confusing title set and a `[-3:]` slice). The store is fresh, so the assertion can be exact. I'll fix that and drop an unused fixture parameter.All test modules are written. Now I'll run the full suite.All 75 pass. Next I'll run the declared acceptance criteria from the four feature specs. I'm extracting them to a scratch directory outside the build tree and running each against the project.My extraction kept the `Intent:`/`Requires:`/`Suite:` header lines, which are not Python. I'll strip those and re-run.`-I` also ignores `PYTHONPATH`, so the import failed. I'll keep `-I` and put the project root on `sys.path` from a small driver instead.All 15 declared criteria pass. Last step is confirming that only the intended files changed and that nothing under `sources/` was touched.RESULT: SUCCESS

FILES CHANGED:
- app_server/__init__.py
- app_server/routes/books.py
- app_server/services/__init__.py
- app_server/services/books.py
- tests/conftest.py
- tests/test_app_shell.py
- tests/test_add_book.py
- tests/test_list_books.py
- tests/test_remove_book.py
- tests/test_reject_empty_fields.py
- tests/test_books_service.py

SUMMARY:
Block 3 implements the four book stories on top of the block 1–2 foundation.

- **Service layer** (`app_server/services/books.py`): `add_book`, `list_books`, `remove_book`, and `validate_book_input`. The service imports no Flask. `add_book` validates before any store call and stores the title and author exactly as supplied. `remove_book` calls `books.get` first and returns False without changing anything for an unknown id.
- **Routes** (`app_server/routes/books.py`, registered in `create_app`): `POST /books` returns 201 with `{id, title, author}`, or 400 with `{"error": ...}`. `GET /books` returns the array in id order, with `[]` when empty. `DELETE /books/<int:book_id>` returns 204 with an empty body, or 404 with an error body. A non-integer id does not match the route.
- **Validation**: a missing, non-string, or whitespace-only title or author raises `ValueError` naming the field. Both fields are named when both are blank. A non-JSON body is treated as an empty submission and gets 400.
- **Tests**: 50 new tests, using a per-test temporary store with the generated schema applied. The configured `data/app.db` is never written by the tests. The HTTP tests cover the empty list, the response fields, read-back, order across reopening the store, removal persisting across reopening, and repeat or unknown removal.
- **Existing test changed**: `test_factory_registers_only_the_health_route` is now `test_factory_registers_only_the_declared_routes`, and it expects `/health`, `/books`, and `/books/<int:book_id>`. The old assertion would fail by design once the book routes are registered.
- **Shared fixtures**: `conftest.py` gained `store_path`, `fresh_app`, `fresh_client`, and `fresh_db`.

Results:
- `.venv/bin/python -m pytest -q`: 75 passed, 0 failed (baseline was 25 before this block).
- The 15 declared acceptance criteria from FEATURE-AddBook, ListBooks, RemoveBook, and RejectEmptyFields: 15 passed. I ran them manually from the spec text with the project root on the path. They clean up their own records, and the configured store was left with 0 books.

Choices I made that you may want to change:
- Validation error wording: a single blank field gives "title must be non-empty text", and both give "title and author must be non-empty text".
- The 404 body for an unknown id is `{"error": "no book with id N"}`.
- `bin/test.sh` is not built here. It belongs to the test-runner story, which is outside this block.

BLOCKERS:
- None.

<blueprint-decisions>
[{"spec":"FEATURE-RejectEmptyFields.md","severity":"Low","subject":"Validation error message format","decision":"Missing, non-string, or whitespace-only fields produce 'title must be non-empty text' (or 'title and author must be non-empty text' when both fail). This names the field and is human-readable, as the spec requires. Acceptable, or should the wording change on replan?"}]
</blueprint-decisions>
