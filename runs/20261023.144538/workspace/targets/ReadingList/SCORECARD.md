# Scorecard: ReadingList

## Specification

> **NOT YET RUN**
> drydock score spec ReadingList

## Acceptance

> **PASSED**
> drydock score ac ReadingList · 2026-10-23T15:24:01.343+00:00

PASS 28   FAIL 0   UNVERIFIED 0   PREPASSED 25   (53 AC total)

## Build

> **RECORDED**
> drydock score build ReadingList

Blocks: 14   Repaired: 0   Failed: 0
Tokens: 4,867,994 (cached 4,715,406, output 152,296)   Cache hit rate: 100.0%

## Release

> **RELEASED**
> drydock score release ReadingList · 2026-10-23T15:24:53.106+00:00

- Verdict: PASSED

ReadingList: PASSED — 6 of 6

  st-001  MET       bin/test.sh:1-11 is `#!/bin/sh` with `set -eu` and ends in `exec pytest -q`; governed gate full: outcome PASS, return_code 0, stdout '191 passed in 9.87s'
  st-002  MET       app_server/books.py:create_book POST /books calls add_book and redirects 303; probe: add status 303 Location '/'; probe: GET /books returned [{'title': 'Dune', 'author': 'Frank Herbert', ...}]; probe: GET / page contains 'Dune' and 'Frank Herbert'; tests/test_add_book.py round-trip tests pass in the gate
  st-003  MET       app_server/book_service.py:list_books returns sorted(..., key=id); probe: list returned Dune (id 1) then Emma (id 2); tests/test_list_books.py:58 test_several_books_are_listed_in_the_order_added passes in the gate
  st-004  MET       app_server/books.py:delete_book POST /books/<int:book_id>/delete calls remove_book then 303; probe: after remove, GET /books returned ['Emma']; tests/test_remove_book.py:64 test_removed_book_is_absent_from_the_next_listing passes in the gate
  st-005  MET       app_server/book_service.py:add_book raises BookRejected('rejected: title is empty' / 'rejected: author is empty') before any write; probe: empty title, HTML -> 400, alert region and 'rejected: title is empty' present; probe: blank author, JSON Accept -> 400 {'error': 'rejected: author is empty', 'field': 'author'}; tests/test_reject_empty_title.py and test_reject_empty_author.py assert nothing is stored; they pass in the gate
  st-006  MET       tests/test_add_book.py; tests/test_list_books.py (order-added tests at lines 58 and 117); tests/test_remove_book.py; tests/test_reject_empty_title.py; tests/test_reject_empty_author.py; governed gate full: 191 passed, return_code 0

## Project acceptance

| ID | Type | Criterion | Verdict | Observed |
|---|---|---|---|---|
| st-001 | technical | The application shall provide a POSIX-compatible bin/test.sh that exits zero when every automated test passes. | MET | bin/test.sh:1-11 is `#!/bin/sh` with `set -eu` and ends in `exec pytest -q`; governed gate full: outcome PASS, return_code 0, stdout '191 passed in 9.87s' |
| st-002 | behavioral | When a reader submits a title and an author, the application shall store the book and show it in the list. | MET | app_server/books.py:create_book POST /books calls add_book and redirects 303; probe: add status 303 Location '/'; probe: GET /books returned [{'title': 'Dune', 'author': 'Frank Herbert', ...}]; probe: GET / page contains 'Dune' and 'Frank Herbert'; tests/test_add_book.py round-trip tests pass in the gate |
| st-003 | behavioral | The application shall present books in the order they were added. | MET | app_server/book_service.py:list_books returns sorted(..., key=id); probe: list returned Dune (id 1) then Emma (id 2); tests/test_list_books.py:58 test_several_books_are_listed_in_the_order_added passes in the gate |
| st-004 | behavioral | When a reader removes a book, the application shall omit it from the list on the next read. | MET | app_server/books.py:delete_book POST /books/<int:book_id>/delete calls remove_book then 303; probe: after remove, GET /books returned ['Emma']; tests/test_remove_book.py:64 test_removed_book_is_absent_from_the_next_listing passes in the gate |
| st-005 | behavioral | If a submission carries an empty title or an empty author, then the application shall reject it and report the reason. | MET | app_server/book_service.py:add_book raises BookRejected('rejected: title is empty' / 'rejected: author is empty') before any write; probe: empty title, HTML -> 400, alert region and 'rejected: title is empty' present; probe: blank author, JSON Accept -> 400 {'error': 'rejected: author is empty', 'field': 'author'}; tests/test_reject_empty_title.py and test_reject_empty_author.py assert nothing is stored; they pass in the gate |
| st-006 | technical | The application shall carry automated tests for adding a book, listing books in the order added, removing a book, rejecting an empty title or author | MET | tests/test_add_book.py; tests/test_list_books.py (order-added tests at lines 58 and 117); tests/test_remove_book.py; tests/test_reject_empty_title.py; tests/test_reject_empty_author.py; governed gate full: 191 passed, return_code 0 |

**Ranked improvements:**
1. The round-trip tests in tests/test_add_book.py (and the other web tests that use committed_session) write to the configured shared store and clean up by deleting their own titles. Give them an isolated store per test, as the fixtures in test_add_book.py already do for their first half, so a failed run cannot leave rows behind in data/app.db.
2. st-006 is judged by file names and the green suite rather than by a mapping from each named behavior to a test ID. Add a short traceability note in README.md mapping each criterion to its test file so that future reviews can confirm coverage without searching.

**Material decisions:**

- Empty or absent title/author on POST /books — 
- Ordering enforced in service, not the store — 
