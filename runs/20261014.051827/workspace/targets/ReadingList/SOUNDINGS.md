# Soundings

Per-assertion acceptance board, one row per Blueprint Programmatic Acceptance check.
`drydock plan` projects every assertion as `— UNVERIFIED`; `drydock score ac` sets the
Status column from deterministic proof results. A rerun of `drydock plan` resets Status to
`— UNVERIFIED`; rescore to refresh.

| Status | Blueprint | AC Id | Text | Binding | Baseline | Previously Passed | Last Block | Evidence | Verified At |
|---|---|---|---|---|---|---|---|---|---|
| ✓ PASS | ARCHITECTURE.md | architecture-create-app | create_app returns a Flask application instance. | yes | VALID product-missing | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | ARCHITECTURE.md | architecture-web-client-testing | web_client returns a test client whose application has TESTING enabled. | yes | VALID product-missing | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | ARCHITECTURE.md | architecture-web-client-unregistered | web_client answers a path no story registers with 404. | yes | VALID product-missing | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-AddBook.md | add-book-stores-valid | A valid submission returns 201 with the stored book's title and author. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-AddBook.md | add-book-rejects-empty-title | An empty title returns 400 and names the title field. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-AddBook.md | add-book-rejects-empty-author | An empty author returns 400 and names the author field. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-AddBook.md | add-book-rejects-whitespace-title | A whitespace-only title is treated as empty and returns 400. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-ListBooks.md | list-books-returns-ok | GET /books returns status 200 with a JSON array. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-ListBooks.md | list-books-insertion-order | Books added in sequence are listed in the order they were added. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-RemoveBook.md | remove-book-deletes | A removed book returns status 204 and is absent from the next list read. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-RemoveBook.md | remove-book-missing-id | Removing an id that is not in the list returns 404 and leaves the list unchanged. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | SCREEN-ReadingList.md | screen-get-root | GET / returns status 200 with an HTML page. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ~ PREPASSED | SCREEN-ReadingList.md | screen-add-list-remove | The routes the page calls add, list, and remove a book, and an unknown id returns 404. | yes | VALID existing-behavior | yes | block-5 | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-TestRunner.md | test-runner-posix-syntax | bin/test.sh parses as POSIX sh. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
| ✓ PASS | FEATURE-TestRunner.md | test-runner-full-suite | The complete automated suite runs unfiltered through sh bin/test.sh and exits zero only when every test passes. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-14T05:33:15+00:00 |
