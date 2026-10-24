# Evidence: Block 9 · Service (block-9)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 4766
- execution id: 20261023.150733.690Z-2bca0178

## Stories built
- Render the reading list page with the add form, rejection messages, and remove controls. (screen-reading-list) [story]

## Acceptance tooling authorization
- SCREEN-ReadingList.md#screen-index-reachable: python-package=pytest; scope=test; authorization=existing Target environment
- SCREEN-ReadingList.md#screen-shows-books-in-order: python-package=pytest; scope=test; authorization=existing Target environment
- SCREEN-ReadingList.md#screen-rejection-shown: python-package=pytest; scope=test; authorization=existing Target environment
- SCREEN-ReadingList.md#screen-remove-book: python-package=pytest; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 781)
- implements: SCREEN-ReadingList.md (SP 2287)
- stack: flask.md (SP 691)

## Build directory changes
- app_server/books.py
- app_server/templates/reading_list.html
- tests/test_create_app_wiring.py
- tests/test_reading_list_page.py

## Pre-build acceptance observation
- RED: screen-index-reachable (SCREEN-ReadingList.md)
  intent: The reading list page at GET / answers 200 and GET /books answers 200 with a JSON array.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "screen-index-reachable.py", line 5, in <module>
        assert page.status_code == 200
               ^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: screen-shows-books-in-order (SCREEN-ReadingList.md)
  intent: Books added through POST /books appear on GET / in the order they were added, with GET /books agreeing.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      positions = [-1, -1, -1]
    --- drydock: end values ---
    Traceback (most recent call last):
      File "screen-shows-books-in-order.py", line 23, in <module>
        assert all(p >= 0 for p in positions)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: screen-rejection-shown (SCREEN-ReadingList.md)
  intent: A rejected browser submission is answered 400 with a page, stores nothing, and the page remains reachable.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      client = <FlaskClient <Flask 'app_server'>>
    --- drydock: end values ---
    Traceback (most recent call last):
      File "screen-rejection-shown.py", line 22, in <module>
        assert client.get("/").status_code == 200
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: screen-remove-book (SCREEN-ReadingList.md)
  intent: Posting to the remove route redirects with 303 and the book is absent from GET / and GET /books on the next read.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      keep_title = 'ScreenRemoveKeep'
      html = '<!doctype html>\n<html lang=en>\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "screen-remove-book.py", line 30, in <module>
        assert keep_title in html
               ^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: screen-index-reachable (SCREEN-ReadingList.md)
  intent: The reading list page at GET / answers 200 and GET /books answers 200 with a JSON array.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-shows-books-in-order (SCREEN-ReadingList.md)
  intent: Books added through POST /books appear on GET / in the order they were added, with GET /books agreeing.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-rejection-shown (SCREEN-ReadingList.md)
  intent: A rejected browser submission is answered 400 with a page, stores nothing, and the page remains reachable.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: screen-remove-book (SCREEN-ReadingList.md)
  intent: Posting to the remove route redirects with 303 and the book is absent from GET / and GET /books on the next read.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.144538/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
The page route `GET /` doesn't exist yet, and the rejection path renders only `base.html`. Before changing anything, I'll get a baseline test run.Baseline is 117 passing. Now I'll add the `GET /` route, the page template, and make the HTML rejection path re-render the full reading list page (per the spec's "page re-rendered with the reason").One existing wiring test pins the endpoint set exactly. Let me read it before deciding how to update it.That test's intent is "only the book routes exist." The `GET /` page is a new route this step is required to add, so I'll extend the expected set to include it and say so in the summary. Next, the new tests for the page.Running the full suite now.All 134 tests pass. Next I'll run the four declared acceptance criteria for this step, with each one in its own script kept outside the build directory.All four declared criteria pass. I'll remove one redundant assertion loop in my new test file, re-run the suite, and check the changed-file list.RESULT: SUCCESS

FILES CHANGED:
- app_server/books.py
- app_server/templates/reading_list.html
- tests/test_reading_list_page.py
- tests/test_create_app_wiring.py

SUMMARY:
- **`GET /`** now renders the reading list page. It lists books in insertion order (via `list_books`, which sorts by id), shows an empty-state message when there are none, and has one remove form per book posting to `/books/{id}/delete`.
- **Add form** posts `title` and `author` to `POST /books`.
- **Rejections:** the HTML 400 path now re-renders the full reading list page with the reason in the alert region, instead of the bare base layout. The JSON 400 path is unchanged.
- **Template:** `reading_list.html` extends the shared `base.html`, so the alert region is inherited.
- **Wiring test:** `test_create_app_registers_only_book_routes_beside_static` pins the exact endpoint set, so I added `books.index` to its expected set. This is the one existing test I changed; no declared acceptance criterion was touched.
- **New tests:** `tests/test_reading_list_page.py` (23 tests) parses the rendered HTML and checks forms, list items, alerts, ordering, escaping, and post-rejection rendering.
- **Declared acceptance criteria (`Suite: scoped`):** all four pass when run as standalone scripts (`screen-index-reachable`, `screen-shows-books-in-order`, `screen-rejection-shown`, `screen-remove-book`). The scripts live in `/tmp/drydock-acs/`, outside the build directory.
- **Project suite:** `pytest -q` gives 134 passed (117 before, plus the new tests). I did not run `sources/full_test.sh`, since no criterion in this step invokes it.
- **Not done:** no git commit, per the build instructions.

BLOCKERS:
- None.

<blueprint-decisions>
[{"spec":"SCREEN-ReadingList.md","severity":"Low","subject":"Rejected HTML submission response","decision":"The spec says a rejected submission re-renders the page with the reason. I render the full reading list page (alert region, add form, and current books) with the 400 status, instead of the bare base layout the route used before. Is that acceptable?"}]
</blueprint-decisions>
