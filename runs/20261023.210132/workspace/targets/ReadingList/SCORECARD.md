# Scorecard: ReadingList

## Specification

> **NOT YET RUN**
> drydock score spec ReadingList

## Acceptance

> **FAILED**
> drydock score ac ReadingList · 2026-10-23T21:15:28.264+00:00

PASS 10   FAIL 3   UNVERIFIED 0   PREPASSED 9   (22 AC total)

Failed:
- database-books-create — DATABASE.md
- database-books-list — DATABASE.md
- database-books-delete — DATABASE.md

## Build

> **RECORDED**
> drydock score build ReadingList

Blocks: 6   Repaired: 1   Failed: 0
Tokens: 2,023,419 (cached 1,764,224, output 36,275)   Cache hit rate: 88.8%

## Release

> **RELEASED**
> drydock score release ReadingList · 2026-10-23T21:16:06.568+00:00

- Verdict: PASSED

ReadingList: PASSED — 6 of 6

  st-001  MET       governed gate full returned 0 with 18 passing tests; bin/test.sh:1-12
  st-002  MET       probe: POST /books succeeded and GET / contained the submitted title; app_server/features/reading_list/routes.py:25-40
  st-003  MET       probe: First Probe Book appeared before Second Probe Book; app_server/features/reading_list/routes.py:17-22
  st-004  MET       probe: POST /books/<id>/delete succeeded and the removed title was absent from GET /; app_server/features/reading_list/routes.py:43-50
  st-005  MET       probe: empty title and whitespace-only author both returned 400 with required-field messages; app_server/features/reading_list/routes.py:29-34
  st-006  MET       tests/test_verification_runner.py:17-80; tests/test_reading_list_screen.py:38-88; governed gate full passed

## Project acceptance

| ID | Type | Criterion | Verdict | Observed |
|---|---|---|---|---|
| st-001 | technical | The application shall provide a POSIX-compatible bin/test.sh that exits zero when every automated test passes. | MET | governed gate full returned 0 with 18 passing tests; bin/test.sh:1-12 |
| st-002 | behavioral | When a reader submits a title and an author, the application shall store the book and show it in the list. | MET | probe: POST /books succeeded and GET / contained the submitted title; app_server/features/reading_list/routes.py:25-40 |
| st-003 | behavioral | The application shall present books in the order they were added. | MET | probe: First Probe Book appeared before Second Probe Book; app_server/features/reading_list/routes.py:17-22 |
| st-004 | behavioral | When a reader removes a book, the application shall omit it from the list on the next read. | MET | probe: POST /books/<id>/delete succeeded and the removed title was absent from GET /; app_server/features/reading_list/routes.py:43-50 |
| st-005 | behavioral | If a submission carries an empty title or an empty author, then the application shall reject it and report the reason. | MET | probe: empty title and whitespace-only author both returned 400 with required-field messages; app_server/features/reading_list/routes.py:29-34 |
| st-006 | technical | The application shall carry automated tests for adding a book, listing books in the order added, removing a book, rejecting an empty title or author | MET | tests/test_verification_runner.py:17-80; tests/test_reading_list_screen.py:38-88; governed gate full passed |

**Material decisions:**

- Primary web workflow routes — 
- Validation response behavior — 
