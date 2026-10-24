# Evidence: Block 3 · Service (block-3)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 3998
- execution id: 20261014.052631.587Z-34851033

## Stories built
- List stored books in the order they were added. (feature-list-books) [story]
- Remove a book and omit it from the next read; report a missing id without altering the list. (feature-remove-book) [story]

## Stacked context
- compass: COMPASS.md (SP 833)
- implements: FEATURE-ListBooks.md (SP 690)
- context: ARCHITECTURE_compact.md (SP 261)
- context: DATABASE_compact.md (SP 272)
- stack: python_compact.md (SP 390)
- stack: flask_compact.md (SP 525)
- implements: FEATURE-RemoveBook.md (SP 896)

## Build directory changes
- app_server/books_service.py
- app_server/books_views.py
- data/app.db
- tests/test_app_factory.py
- tests/test_list_books.py
- tests/test_remove_book.py

## Pre-build acceptance observation
- RED: list-books-returns-ok (FEATURE-ListBooks.md)
  intent: GET /books returns status 200 with a JSON array.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "list-books-returns-ok.py", line 5, in <module>
        assert response.status_code == 200
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: list-books-insertion-order (FEATURE-ListBooks.md)
  intent: Books added in sequence are listed in the order they were added.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "list-books-insertion-order.py", line 13, in <module>
        assert listing.status_code == 200
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: remove-book-deletes (FEATURE-RemoveBook.md)
  intent: A removed book returns status 204 and is absent from the next list read.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "remove-book-deletes.py", line 10, in <module>
        assert deleted.status_code == 204
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: remove-book-missing-id (FEATURE-RemoveBook.md)
  intent: Removing an id that is not in the list returns 404 and leaves the list unchanged.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      client = <FlaskClient <Flask 'app_server'>>
      book_id = 7
    --- drydock: end values ---
    Traceback (most recent call last):
      File "remove-book-missing-id.py", line 9, in <module>
        assert client.delete(f"/books/{book_id}").status_code == 204
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: list-books-returns-ok (FEATURE-ListBooks.md)
  intent: GET /books returns status 200 with a JSON array.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: list-books-insertion-order (FEATURE-ListBooks.md)
  intent: Books added in sequence are listed in the order they were added.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-book-deletes (FEATURE-RemoveBook.md)
  intent: A removed book returns status 204 and is absent from the next list read.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: remove-book-missing-id (FEATURE-RemoveBook.md)
  intent: Removing an id that is not in the list returns 404 and leaves the list unchanged.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
Existing code covers POST /books and the persistence layer. Before changing anything, I'll get a baseline test run.Baseline is green (38 passing). Now the service layer: list and remove, both going through the declared `books` operations.Now the routes. The 404 body names the id that was not found, matching the 400 convention of naming the offending field.The existing `test_app_factory` asserts the exact set of routes, so it has to change with the new route. Updating that test, then adding tests for both stories.Now the full suite, then the declared acceptance assertions run verbatim.Suite passes (38 → 58 tests). Running the four declared acceptance assertions as written in the specs:All four declared assertions exit 0. Checking that only the intended files changed:Both stories are implemented, and the four declared acceptance assertions pass when run as written. The project suite is green: 58 tests, up from 38.

RESULT: SUCCESS

FILES CHANGED:
- app_server/books_service.py
- app_server/books_views.py
- tests/test_app_factory.py
- tests/test_list_books.py
- tests/test_remove_book.py

SUMMARY:
- **List (`GET /books`)**: returns 200 with a JSON array of `{id, title, author}`. The service sorts by id, because the generated SELECT has no ORDER BY and I can't change the shipped persistence layer.
- **Remove (`DELETE /books/<int:id>`)**: a stored id is removed through `books.get` then `books.delete` and returns 204 with an empty body. An unknown id returns 404 with `{"id": <id>}` and leaves the list unchanged.
- **Existing test changed**: `test_create_app_registers_only_the_add_book_route_besides_static` asserted the exact route set, so the new route broke it. I updated it to include `/books/<int:book_id>`. It is not a declared acceptance assertion.
- **Tests**: 20 new tests cover ordering, the empty store, read-back after add, the 204/404 paths, repeated delete, non-integer ids, and the service functions. Each test uses its own temporary store.
- **Test counts**: the project suite (`.venv/bin/python -m pytest -q`) is 58 passed, exit 0. The four declared ACs were run verbatim, all exit 0.
- **Not touched**: `bin/test.sh` does not exist yet. `sources/full_test.sh` will therefore fail until the block that delivers that entry point, which is outside this step.

<blueprint-decisions>
[{"spec":"FEATURE-RemoveBook.md","severity":"Low","subject":"404 response body","decision":"The spec requires status 404 but no body. I return {\"id\": <requested id>} so the caller can see which id was missing, mirroring the 400 responses that name the offending field. Is that acceptable, or should the body be empty?"},{"spec":"FEATURE-ListBooks.md","severity":"Low","subject":"Ordering guarantee","decision":"The DATABASE spec says ascending id, but the shipped SELECT has no ORDER BY. I sort by id in list_books so ordering does not depend on the engine. Is that acceptable?"}]
</blueprint-decisions>

BLOCKERS:
- None for this block.
