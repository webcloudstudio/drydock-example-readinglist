# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 2810
- execution id: 20261014.052833.846Z-f9f2c800

## Stories built
- Serve the reading list page that adds, lists, and removes books. (screen-reading-list) [story]

## Stacked context
- compass: COMPASS.md (SP 833)
- implements: SCREEN-ReadingList.md (SP 986)
- stack: python_compact.md (SP 390)
- stack: flask_compact.md (SP 525)

## Build directory changes
- app_server/__init__.py
- app_server/pages.py
- app_server/templates/reading_list.html
- tests/test_app_factory.py
- tests/test_reading_list_page.py

## Pre-build acceptance observation
- RED: screen-get-root (SCREEN-ReadingList.md)
  intent: GET / returns status 200 with an HTML page.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "screen-get-root.py", line 5, in <module>
        assert response.status_code == 200
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): screen-add-list-remove (SCREEN-ReadingList.md)
  intent: The routes the page calls add, list, and remove a book, and an unknown id returns 404.
  return code: 0

## Post-build programmatic acceptance
- PASS: screen-get-root (SCREEN-ReadingList.md)
  intent: GET / returns status 200 with an HTML page.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-add-list-remove (SCREEN-ReadingList.md)
  intent: The routes the page calls add, list, and remove a book, and an unknown id returns 404.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
I'll start by inspecting the build directory and the prior blocks' output.The routes for books already exist, so this block only adds `GET /` and the page. Before changing anything, I'll get a baseline run of the existing suite and check the toolchain.Baseline is 58 passing. My plan:

- Add `app_server/pages.py`, a blueprint serving `GET /` via a Jinja template (autoescape stays on).
- Add `app_server/templates/reading_list.html` with the form, error slots, ordered list, and inline script. The script builds list items with `textContent`, so titles are never parsed as HTML.
- Register the blueprint in the factory.
- Update the existing route-set test, since `/` is now a declared route.
- Add tests that parse the HTML and read back the status codes.Next, I'll register the blueprint and update the route-set test, since `/` is now a declared route.Now the tests. They parse the HTML with the stdlib parser and check the page's structure and the routes it consumes through status codes and parsed JSON.I'll tidy two tests: drop the substring check (the before/after equality already covers it) and rename the submit test to match what it asserts.Now the full suite, then the two declared acceptance criteria. I'll run the criteria from a script in `/tmp` against a temporary store so nothing lands in `data/app.db`.Pytest exits 0 and both criteria pass. The page's script is the one part no test executes, so I'll at least syntax-check it if Node is available.The reading list page is in place: `GET /` serves HTML and the page calls the existing book routes. The declared acceptance criteria pass, and the full pytest suite is green.

Two notes on this step:
- I changed one existing project test, `test_create_app_registers_only_the_page_and_book_routes_besides_static`. It asserted the route set without `/`, and `/` is now a declared route. It is not one of the declared acceptance criteria.
- The page's inline script is only syntax-checked (Node's `--check`). Nothing exercises it in a browser, so the add/remove behaviour in the page is unverified beyond reading the code.

I did not create `bin/test.sh`. COMPASS requires it, but it belongs to a later build step.

RESULT: SUCCESS

FILES CHANGED:
- app_server/pages.py
- app_server/templates/reading_list.html
- app_server/__init__.py
- tests/test_reading_list_page.py
- tests/test_app_factory.py

SUMMARY:
- `app_server/pages.py`: new `pages` blueprint with `GET /` rendering `reading_list.html`. The route is registered in `create_app()` ahead of the book blueprint.
- `app_server/templates/reading_list.html`: the form (title and author text inputs, one submit control, an error span beside each field), an ordered list `#books`, and an inline script. The script:
  - loads `GET /books` on page load and renders the list in the order returned;
  - submits `POST /books`, and on 201 resets the form and reloads the list, or on 400 shows the error beside the field named in the response;
  - blocks empty or whitespace-only title or author client-side, before any request is sent;
  - removes via `DELETE /books/{id}` and reloads on 204;
  - builds list items with `textContent`, so stored titles are never interpreted as HTML.
- `tests/test_reading_list_page.py`: 16 tests. They parse the HTML with the stdlib parser and check the form, inputs, error slots, the ordered list, and the response to `POST /` (405). They also cover the page's three routes through status codes and parsed JSON, including ordering and the 400 and 404 paths.
- `tests/test_app_factory.py`: the route-set assertion now includes `/`.
- Declared acceptance criteria `screen-get-root` and `screen-add-list-remove` were run from a scratch script against a temporary store. Both pass; the scratch script was removed afterwards.
- Pytest: exit 0 after the change (the baseline was 58 passing before the new tests were added). No files in `sources/` were touched.

Choices I made:
- The page uses a JS-driven list (no server-rendered books), which the spec's "page calls the routes" implies.
- Whitespace-only input is rejected client-side as well as by the server.
- The client-side error text is "title must not be empty." and similar.

BLOCKERS:
- None for this block. `sh sources/full_test.sh` will still report a missing `bin/test.sh` until the story that creates it is built.
