# Soundings

Per-assertion acceptance board, one row per Blueprint Programmatic Acceptance check.
`drydock plan` projects every assertion as `— UNVERIFIED`; `drydock score ac` sets the
Status column from deterministic proof results. A rerun of `drydock plan` resets Status to
`— UNVERIFIED`; rescore to refresh.

| Status | Blueprint | AC Id | Text | Binding | Baseline | Previously Passed | Last Block | Evidence | Verified At |
|---|---|---|---|---|---|---|---|---|---|
| ✓ PASS | ARCHITECTURE.md | architecture-manifest | pyproject.toml parses and declares Flask and pytest as dependencies. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | ARCHITECTURE.md | architecture-tree | The lockfile, tests directory, and conftest exist at the application root. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ~ PREPASSED | ARCHITECTURE.md | architecture-pytest | The pytest runner is installed and starts from the application root. | yes | PREBUILD_PASSES empty-tree | yes | block-5 | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | DATABASE.md | books-create | books.create stores a book and returns the declared Output row carrying the supplied title and author. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | DATABASE.md | books-get | books.get reads back a created book by id with the stored title and author. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | DATABASE.md | books-list | books.list returns books in the order they were added. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | DATABASE.md | books-delete | books.delete removes a book so it no longer appears in the next list read, and leaves other books in place. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-AppShell.md | appshell-factory | create_app returns a Flask application. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-AppShell.md | appshell-client | web_client returns a usable test client for a testing-mode app. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-AppShell.md | appshell-health | GET /health is reachable and answers 200 with a JSON body. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-AppShell.md | appshell-unknown-route | A path no feature declares is absent and answers 404. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-AddBook.md | addbook-create | POST /books answers 201 and returns the title and author that were supplied, with an id. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-AddBook.md | addbook-persisted | A submitted book is read back from the store with the supplied title and author. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-AddBook.md | addbook-ascending-ids | Two books added in sequence receive ascending ids, preserving insertion order. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-ListBooks.md | listbooks-order | GET /books returns the books added during the check in the order they were added. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-ListBooks.md | listbooks-fields | Each listed book carries the supplied title and author and its id. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-ListBooks.md | listbooks-reachable | GET /books is reachable and returns a JSON array even when no check data exists. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-RemoveBook.md | remove-book-deletes | Removing an added book answers 204 and the book is absent from the next list read. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-RemoveBook.md | remove-book-unknown-id | Removing an id that does not exist answers 404, and removing the same id twice answers 404 the second time. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-RemoveBook.md | remove-book-preserves-order | Removing the middle book leaves the other books in the order they were added. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-RejectEmptyFields.md | reject-empty-title | POST /books with an empty title answers 400 and stores nothing. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-RejectEmptyFields.md | reject-empty-author | POST /books with an empty author answers 400 and stores nothing. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-RejectEmptyFields.md | reject-both-empty | POST /books with both fields empty answers 400 and stores nothing. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-RejectEmptyFields.md | reject-whitespace-and-missing | Whitespace-only and missing fields are rejected with 400 and nothing is stored. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-RejectEmptyFields.md | reject-validator | validate_book_input raises ValueError for an empty title or author. | yes | VALID product-missing | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-RejectEmptyFields.md | reject-valid-still-accepted | A submission with both fields present is still accepted with 201 after validation is in place. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | SCREEN-ReadingList.md | screen-index-renders | GET / answers 200 and shows an added book's title and author, and GET /books agrees with it on the same book. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | SCREEN-ReadingList.md | screen-add-form | POST /add with a title and author redirects 303 and the book then appears on GET / and in GET /books. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | SCREEN-ReadingList.md | screen-add-rejects-empty | POST /add with an empty title, an empty author, or whitespace-only values answers 400 and stores nothing. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | SCREEN-ReadingList.md | screen-remove-form | POST /remove/{book_id} redirects 303 and the book is gone from GET / and GET /books; an unknown id also redirects 303. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | SCREEN-ReadingList.md | screen-order-added | GET / presents books in the order they were added. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-TestRunner.md | test-runner-posix-syntax | bin/test.sh exists and parses as POSIX sh without errors. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ~ PREPASSED | FEATURE-TestRunner.md | test-runner-covers-behaviors | The test suite contains test modules for the add, list, remove, and rejection behaviors and pytest collects them without error. | yes | VALID existing-behavior | yes | block-5 | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-TestRunner.md | test-runner-full-suite | The Commander-owned entry point sources/full_test.sh dispatches to bin/test.sh and the complete automated suite exits zero. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
| ✓ PASS | FEATURE-TestRunner.md | test-runner-direct | Running sh bin/test.sh from the application root exits zero. | yes | VALID baseline-red | yes | block-5 |  | 2026-10-23T18:08:47+00:00 |
