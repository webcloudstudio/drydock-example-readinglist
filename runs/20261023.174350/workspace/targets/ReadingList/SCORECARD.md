# Scorecard: ReadingList

## Specification

> **NOT YET RUN**
> drydock score spec ReadingList

## Acceptance

> **PASSED**
> drydock score ac ReadingList · 2026-10-23T18:09:45.157+00:00

PASS 33   FAIL 0   UNVERIFIED 0   PREPASSED 2   (35 AC total)

## Build

> **RECORDED**
> drydock score build ReadingList

Blocks: 5   Repaired: 0   Failed: 0
Tokens: 2,399,565 (cached 2,324,652, output 74,785)   Cache hit rate: 100.0%

## Release

> **RELEASED**
> drydock score release ReadingList · 2026-10-23T18:10:41.234+00:00

- Verdict: PASSED

ReadingList: PASSED — 6 of 6

  st-001  MET       bin/test.sh:1-16 is a #!/bin/sh script that changes to the app root, activates .venv if present, and runs `pytest -q` as its last command; governed gate full: argv `sh sources/full_test.sh`, return_code 0, stdout `117 passed in 2.65s`; sources/full_test.sh:17 execs `sh bin/test.sh`, so the gate's exit code is pytest's exit code
  st-002  MET       app_server/routes/pages.py:64-73 /add calls book_service.add_book and redirects to index on success; probe: POST /add {title: Dune, author: Frank Herbert} returned 303 Location /; probe: GET / contained 'Dune' and 'Frank Herbert' -> True
  st-003  MET       persistence/schema.py:36-51 declares the list operation; persistence/sqlite.py orders by insertion, and app_server/services/books.py:29 documents 'in the order it was added'; probe: page positions of Dune, Emma, Beloved were ascending; probe: GET /books titles returned ['Dune', 'Emma', 'Beloved']
  st-004  MET       app_server/routes/pages.py:76-79 /remove/<id> calls remove_book and redirects; probe: POST /remove/<Emma id> returned 303; probe: GET / no longer contains 'Emma'; GET /books returned ['Dune', 'Beloved']
  st-005  MET       app_server/services/books.py:11-19 validate_book_input rejects blank or non-text title/author with a message naming the field; probe: {title:'', author:'X'} -> 400, reason 'title must be non-empty text'; probe: {title:'Y', author:'   '} -> 400, reason 'author must be non-empty text'; probe: {title:'Z'} -> 400, reason 'author must be non-empty text'; probe: GET /books after rejects still ['Dune', 'Beloved']
  st-006  MET       tests/test_add_book.py: add behavior tests (e.g. test_post_answers_201_with_stored_book_fields); tests/test_list_books.py: test_list_returns_titles_in_the_order_they_were_added; tests/test_remove_book.py: test_removed_book_is_absent_from_next_list_read; tests/test_reject_empty_fields.py: test_blank_or_missing_field_answers_400_with_error_message; governed gate full: 117 passed, return_code 0

## Project acceptance

| ID | Type | Criterion | Verdict | Observed |
|---|---|---|---|---|
| st-001 | technical | The application shall provide a POSIX-compatible bin/test.sh that exits zero when every automated test passes. | MET | bin/test.sh:1-16 is a #!/bin/sh script that changes to the app root, activates .venv if present, and runs `pytest -q` as its last command; governed gate full: argv `sh sources/full_test.sh`, return_code 0, stdout `117 passed in 2.65s`; sources/full_test.sh:17 execs `sh bin/test.sh`, so the gate's exit code is pytest's exit code |
| st-002 | behavioral | When a reader submits a title and an author, the application shall store the book and show it in the list. | MET | app_server/routes/pages.py:64-73 /add calls book_service.add_book and redirects to index on success; probe: POST /add {title: Dune, author: Frank Herbert} returned 303 Location /; probe: GET / contained 'Dune' and 'Frank Herbert' -> True |
| st-003 | behavioral | The application shall present books in the order they were added. | MET | persistence/schema.py:36-51 declares the list operation; persistence/sqlite.py orders by insertion, and app_server/services/books.py:29 documents 'in the order it was added'; probe: page positions of Dune, Emma, Beloved were ascending; probe: GET /books titles returned ['Dune', 'Emma', 'Beloved'] |
| st-004 | behavioral | When a reader removes a book, the application shall omit it from the list on the next read. | MET | app_server/routes/pages.py:76-79 /remove/<id> calls remove_book and redirects; probe: POST /remove/<Emma id> returned 303; probe: GET / no longer contains 'Emma'; GET /books returned ['Dune', 'Beloved'] |
| st-005 | behavioral | If a submission carries an empty title or an empty author, then the application shall reject it and report the reason. | MET | app_server/services/books.py:11-19 validate_book_input rejects blank or non-text title/author with a message naming the field; probe: {title:'', author:'X'} -> 400, reason 'title must be non-empty text'; probe: {title:'Y', author:'   '} -> 400, reason 'author must be non-empty text'; probe: {title:'Z'} -> 400, reason 'author must be non-empty text'; probe: GET /books after rejects still ['Dune', 'Beloved'] |
| st-006 | technical | The application shall carry automated tests for adding a book, listing books in the order added, removing a book, rejecting an empty title or author | MET | tests/test_add_book.py: add behavior tests (e.g. test_post_answers_201_with_stored_book_fields); tests/test_list_books.py: test_list_returns_titles_in_the_order_they_were_added; tests/test_remove_book.py: test_removed_book_is_absent_from_next_list_read; tests/test_reject_empty_fields.py: test_blank_or_missing_field_answers_400_with_error_message; governed gate full: 117 passed, return_code 0 |

**Ranked improvements:**
1. README does not say how to provision the database before first run. create_app applies no schema, so a fresh DATABASE_URL serves 500 'no such table: books' until schema.sql is executed. Add a documented provisioning command (or a CLI step) to the README's Setup section.
2. st-001 says 'POSIX-compatible' but no machine check runs the script under a strict POSIX shell such as dash. Add that check to the suite, or name the shell it must run under.
3. Several criteria (st-002 to st-005) are proven only by the test suite and my probe. Adding an end-to-end test that drives the web form through a real server would make these trials observable without an ephemeral probe.
