# Evidence: Block 2 · Service (block-2)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 3493
- execution id: 20261014.052357.319Z-d192336e

## Stories built
- Accept a title and author, store the book, and reject empty fields with a named reason. (feature-add-book) [story]

## Stacked context
- compass: COMPASS.md (SP 833)
- implements: FEATURE-AddBook.md (SP 1094)
- context: ARCHITECTURE_compact.md (SP 261)
- context: DATABASE_compact.md (SP 272)
- stack: python_compact.md (SP 390)
- stack: flask_compact.md (SP 525)

## Build directory changes
- app_server/__init__.py
- app_server/books_service.py
- app_server/books_views.py
- app_server/settings.py
- data/app.db
- tests/conftest.py
- tests/test_add_book.py
- tests/test_app_factory.py

## Pre-build acceptance observation
- RED: add-book-stores-valid (FEATURE-AddBook.md)
  intent: A valid submission returns 201 with the stored book's title and author.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "add-book-stores-valid.py", line 8, in <module>
        assert response.status_code == 201
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: add-book-rejects-empty-title (FEATURE-AddBook.md)
  intent: An empty title returns 400 and names the title field.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "add-book-rejects-empty-title.py", line 7, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: add-book-rejects-empty-author (FEATURE-AddBook.md)
  intent: An empty author returns 400 and names the author field.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "add-book-rejects-empty-author.py", line 7, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: add-book-rejects-whitespace-title (FEATURE-AddBook.md)
  intent: A whitespace-only title is treated as empty and returns 400.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "add-book-rejects-whitespace-title.py", line 7, in <module>
        assert response.status_code == 400
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: add-book-stores-valid (FEATURE-AddBook.md)
  intent: A valid submission returns 201 with the stored book's title and author.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: add-book-rejects-empty-title (FEATURE-AddBook.md)
  intent: An empty title returns 400 and names the title field.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: add-book-rejects-empty-author (FEATURE-AddBook.md)
  intent: An empty author returns 400 and names the author field.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: add-book-rejects-whitespace-title (FEATURE-AddBook.md)
  intent: A whitespace-only title is treated as empty and returns 400.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261014.051827/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
The build directory has no routes yet, and `create_app()` registers nothing. The spec doesn't say where the store lives, and the acceptance checks call `web_client()` with no arguments, so I'll read the DSN from an environment variable with a `data/app.db` default. I'll write the settings module, the framework-independent service, the thin blueprint, and the factory wiring.Next, the tests. The existing factory test asserts that no routes are registered, which this feature changes, so I'll update it. I also want the test store isolated from `data/`, so I'll add an autouse fixture to the conftest. I need to read those files before editing them.Now I'll run the existing suite, then the four declared acceptance checks from `FEATURE-AddBook.md`, each as its own script outside the build directory.The `-I` flag also ignores `PYTHONPATH`, so the import failed on the path, not the code. The scripts live in their own directory, so I'll run them without `-I`.All four declared acceptance checks pass, and the project suite is green (38 tests, exit 0). I did not run `sources/full_test.sh`, because no criterion in this block invokes it.

**Summary**

`POST /books` now accepts a title and author, stores the book through `db.books.create`, and returns 201 with `id`, `title`, and `author`. An empty, whitespace-only, missing, or non-string field returns 400 with `{"field": "title"}` or `{"field": "author"}`, and nothing is stored. The route is a thin Blueprint. Validation and storage live in a framework-independent service, and no module outside `persistence` imports `sqlite3`.

I changed one existing test. `test_create_app_registers_no_feature_routes` asserted that no routes exist at all. This feature adds `/books`, so the assertion now expects exactly `/books` plus static. I also added an autouse fixture in `tests/conftest.py` that points tests at a temporary store.

**Choices I made (the spec didn't settle these)**

- **Database location:** `create_app()` reads `READINGLIST_DATABASE` and falls back to `data/app.db` in the project root. Acceptance checks run outside pytest, so they write to that `data/app.db`, which is gitignored and was already present.
- **Trimming:** title and author are trimmed before storage, matching DATABASE.md's "non-empty after trimming."
- **Bad bodies:** a non-JSON body, a JSON array, or a non-string field is rejected as a missing or empty title.

<blueprint-decisions>
[{"spec":"FEATURE-AddBook.md","severity":"Low","subject":"Database location for create_app","decision":"No spec names a DSN. create_app() reads READINGLIST_DATABASE and defaults to data/app.db under the project root. Tests redirect it to a temp store via an autouse fixture. Acceptance checks that call web_client() outside pytest write to data/app.db. Is that acceptable, or should the default become a temp store?"},{"spec":"FEATURE-AddBook.md","severity":"Low","subject":"Trim before storing","decision":"Title and author are trimmed before storage and the trimmed values are returned, following DATABASE.md's non-empty-after-trimming rule. Is that acceptable?"}]
</blueprint-decisions>

FILES CHANGED:
- app_server/__init__.py
- app_server/settings.py
- app_server/books_service.py
- app_server/books_views.py
- tests/conftest.py
- tests/test_app_factory.py
- tests/test_add_book.py

SUMMARY:
- Acceptance checks (FEATURE-AddBook.md, 4 of 4 pass): add-book-stores-valid, add-book-rejects-empty-title, add-book-rejects-empty-author, add-book-rejects-whitespace-title. Each ran as a standalone script from /tmp with the build directory on PYTHONPATH.
- Project suite: `.venv/bin/python -m pytest -q` exits 0, 38 tests passed. This includes 27 new tests in tests/test_add_book.py covering the route, the round-trip read-back through `db.books`, list order, rejected submissions not being stored, and the service. Also includes the updated factory route test.
- `sources/full_test.sh` was not run. No criterion in this block invokes it, and `bin/test.sh` belongs to a later block.

RESULT: SUCCESS
