# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 5524
- execution id: 20261023.180241.264Z-b86c6ee1

## Stories built
- Render the reading list page with an add form, error display, and remove buttons. (screen-reading-list) [story]

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 895)
- implements: SCREEN-ReadingList.md (SP 2871)
- stack: flask.md (SP 691)

## Build directory changes
- app_server/routes/pages.py
- app_server/templates/reading_list.html
- data/app.db
- tests/test_app_shell.py
- tests/test_reading_list_page.py

## Pre-build acceptance observation
- RED: screen-index-renders (SCREEN-ReadingList.md)
  intent: GET / answers 200 and shows an added book's title and author, and GET /books agrees with it on the same book.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "screen-index-renders.py", line 13, in <module>
        assert page.status_code == 200
               ^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: screen-add-form (SCREEN-ReadingList.md)
  intent: POST /add with a title and author redirects 303 and the book then appears on GET / and in GET /books.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "screen-add-form.py", line 12, in <module>
        assert response.status_code == 303
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: screen-add-rejects-empty (SCREEN-ReadingList.md)
  intent: POST /add with an empty title, an empty author, or whitespace-only values answers 400 and stores nothing.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "screen-add-rejects-empty.py", line 19, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: screen-remove-form (SCREEN-ReadingList.md)
  intent: POST /remove/{book_id} redirects 303 and the book is gone from GET / and GET /books; an unknown id also redirects 303.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "screen-remove-form.py", line 11, in <module>
        assert response.status_code == 303
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: screen-order-added (SCREEN-ReadingList.md)
  intent: GET / presents books in the order they were added.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      title = 'ac-screen-order-6a944ab73f9a4f36a0630d7bbafcab52-2'
      titles = ['ac-screen-order-6a944ab73f9a4f36a0630d7bbafcab52-0', 'ac-screen-order-6a944ab73f9a4f36a0630d7bbafcab52-1', 'ac-screen-order-6a944ab73f9a4f36a0630d7bbafcab52-2']
      html = '<!doctype html>\n<html lang=en>\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "screen-order-added.py", line 14, in <module>
        positions = [html.index(title) for title in titles]
                     ^^^^^^^^^^^^^^^^^
    ValueError: substring not found

## Post-build programmatic acceptance
- PASS: screen-index-renders (SCREEN-ReadingList.md)
  intent: GET / answers 200 and shows an added book's title and author, and GET /books agrees with it on the same book.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-add-form (SCREEN-ReadingList.md)
  intent: POST /add with a title and author redirects 303 and the book then appears on GET / and in GET /books.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-add-rejects-empty (SCREEN-ReadingList.md)
  intent: POST /add with an empty title, an empty author, or whitespace-only values answers 400 and stores nothing.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-remove-form (SCREEN-ReadingList.md)
  intent: POST /remove/{book_id} redirects 303 and the book is gone from GET / and GET /books; an unknown id also redirects 303.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-order-added (SCREEN-ReadingList.md)
  intent: GET / presents books in the order they were added.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
The baseline is green (75 passed), the book service already validates input and keeps list order, and the routes for `/books` exist. I'll add the three page routes to the `pages` blueprint, a template, and tests.Now I'll update the route-registry test, since this block legitimately adds three routes to the app.Next, the page test module. It reads the rendered HTML through a small structural parser (list items, error region, input values, form actions) rather than substring checks on the page.One test I just wrote is muddled (it checks the plain load and the rejection in one body). I'll make it check only the rejection response.All 110 tests pass (75 existing plus 35 new, and the updated route test). Now I'll run the five declared scoped acceptance checks from the SCREEN spec myself, since they are not on disk and the runner will grade them.All five declared checks pass. Last, I'll confirm which files changed in the build directory.RESULT: SUCCESS

FILES CHANGED:
- app_server/routes/pages.py
- app_server/templates/reading_list.html
- tests/test_reading_list_page.py
- tests/test_app_shell.py

SUMMARY:
- **Routes** (`app_server/routes/pages.py`, added to the existing `pages` blueprint):
  - `GET /` renders the page with status 200.
  - `POST /add` calls `book_service.add_book`. Success redirects 303 to `/`. A `ValueError` re-renders the page with status 400, the error message, and the entered values echoed back into the form.
  - `POST /remove/<int:book_id>` calls `book_service.remove_book` and redirects 303 to `/`, including for unknown ids.
- **Template** (`app_server/templates/reading_list.html`, extends `base.html`): heading, error region shown only on rejection, add form posting to `/add`, ordered list with title and author, a remove form per book, and a "No books yet." message when empty. Jinja autoescaping is preserved and no JavaScript is used.
- **Existing test updated:** `test_factory_registers_only_the_declared_routes` in `tests/test_app_shell.py` now expects the three new routes. This is required by this block, since the screen adds them.
- **New tests** (`tests/test_reading_list_page.py`, 35 tests): they read back through the public interface (`GET /books`, `GET /`). The page is parsed structurally, not by substring. Coverage includes the order of the list, empty and missing or whitespace fields (parametrized), the error region, no stored rows on rejection, echoed values, removal and reappearance, unknown ids, and the no-script rule.

Verification:
- `.venv/bin/pytest -q`: **110 passed** (75 pre-existing, 35 new). Command run from the build directory; exit 0.
- The five declared scoped acceptance checks (`screen-index-renders`, `screen-add-form`, `screen-add-rejects-empty`, `screen-remove-form`, `screen-order-added`) were reconstructed from the SCREEN spec and run with `.venv/bin/python -I` against `app_server.testing.web_client`. All five passed. These are my reconstructions, not the staged originals, so the runner's grading is authoritative.
- `sources/full_test.sh` was not run. No criterion in this block invokes it, and it was not modified.

Choices I made:
- Put the page routes in the existing `pages` blueprint rather than a new module, since that blueprint already holds application-level routes.
- Used the service's own `ValueError` message for the error text. The spec asks only that the error state which field is missing; I did not assert on the wording in tests.

No blockers.
