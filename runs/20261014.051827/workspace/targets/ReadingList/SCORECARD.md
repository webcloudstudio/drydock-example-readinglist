# Scorecard: ReadingList

## Specification

> **NOT YET RUN**
> drydock score spec ReadingList

## Acceptance

> **PASSED**
> drydock score ac ReadingList · 2026-10-14T05:33:50.799+00:00

PASS 14   FAIL 0   UNVERIFIED 0   PREPASSED 1   (15 AC total)

## Build

> **RECORDED**
> drydock score build ReadingList

Blocks: 5   Repaired: 0   Failed: 0
Tokens: 1,559,118 (cached 1,499,021, output 59,993)   Cache hit rate: 100.0%

## Release

> **RELEASED**
> drydock score release ReadingList · 2026-10-14T05:34:35.309+00:00

- Verdict: PASSED

ReadingList: PASSED — 6 of 6

  st-001  MET       governed_gate full: PASS, return_code 0, stdout shows all dots with no failures; bin/test.sh:1-13 is a POSIX sh script that runs `.venv/bin/python -m pytest -q` and exits with its status; probe: n/a, pinned by the green governed gate
  st-002  MET       app_server/books_views.py:23-30 POST /books calls add_book and returns 201 with id, title, author; probe: POST /books {Dune, Herbert} returned 201 with id 1; GET /books then returned it; app_server/templates/reading_list.html: on status 201 the script calls loadBooks(), which fetches /books and renders each entry
  st-003  MET       app_server/books_service.py:list_books sorts by id, the order added; probe: GET /books after adds returned ids 1, 2, 3 in order; probe: after DELETE of id 2, GET /books returned ids 1, 3 in order
  st-004  MET       app_server/books_views.py:33-38 DELETE returns 204 on success; probe: DELETE /books/2 returned 204; following GET /books omitted id 2; probe: a second DELETE /books/2 returned 404, leaving the list unchanged
  st-005  MET       app_server/books_service.py:_required raises InvalidBook for empty or whitespace-only values; probe: POST with title '  ' returned 400 {"field":"title"}; probe: POST with empty author returned 400 {"field":"author"}; missing author returned 400 {"field":"author"}; probe: GET /books after the rejections showed no new entries; app_server/templates/reading_list.html: the 400 handler shows '<field> must not be empty.' beside the field
  st-006  MET       tests/test_add_book.py: test_post_valid_book_is_listed_in_order_added, test_post_empty_title_returns_400_naming_title, test_post_empty_author_returns_400_naming_author; tests/test_list_books.py: test_get_books_lists_books_in_the_order_they_were_added; tests/test_remove_book.py: test_delete_stored_book_returns_204_with_empty_body, test_deleted_book_is_absent_from_next_list; governed_gate full: PASS

## Project acceptance

| ID | Type | Criterion | Verdict | Observed |
|---|---|---|---|---|
| st-001 | technical | The application shall provide a POSIX-compatible bin/test.sh that exits zero when every automated test passes. | MET | governed_gate full: PASS, return_code 0, stdout shows all dots with no failures; bin/test.sh:1-13 is a POSIX sh script that runs `.venv/bin/python -m pytest -q` and exits with its status; probe: n/a, pinned by the green governed gate |
| st-002 | behavioral | When a reader submits a title and an author, the application shall store the book and show it in the list. | MET | app_server/books_views.py:23-30 POST /books calls add_book and returns 201 with id, title, author; probe: POST /books {Dune, Herbert} returned 201 with id 1; GET /books then returned it; app_server/templates/reading_list.html: on status 201 the script calls loadBooks(), which fetches /books and renders each entry |
| st-003 | behavioral | The application shall present books in the order they were added. | MET | app_server/books_service.py:list_books sorts by id, the order added; probe: GET /books after adds returned ids 1, 2, 3 in order; probe: after DELETE of id 2, GET /books returned ids 1, 3 in order |
| st-004 | behavioral | When a reader removes a book, the application shall omit it from the list on the next read. | MET | app_server/books_views.py:33-38 DELETE returns 204 on success; probe: DELETE /books/2 returned 204; following GET /books omitted id 2; probe: a second DELETE /books/2 returned 404, leaving the list unchanged |
| st-005 | behavioral | If a submission carries an empty title or an empty author, then the application shall reject it and report the reason. | MET | app_server/books_service.py:_required raises InvalidBook for empty or whitespace-only values; probe: POST with title '  ' returned 400 {"field":"title"}; probe: POST with empty author returned 400 {"field":"author"}; missing author returned 400 {"field":"author"}; probe: GET /books after the rejections showed no new entries; app_server/templates/reading_list.html: the 400 handler shows '<field> must not be empty.' beside the field |
| st-006 | technical | The application shall carry automated tests for adding a book, listing books in the order added, removing a book, rejecting an empty title or author | MET | tests/test_add_book.py: test_post_valid_book_is_listed_in_order_added, test_post_empty_title_returns_400_naming_title, test_post_empty_author_returns_400_naming_author; tests/test_list_books.py: test_get_books_lists_books_in_the_order_they_were_added; tests/test_remove_book.py: test_delete_stored_book_returns_204_with_empty_body, test_deleted_book_is_absent_from_next_list; governed_gate full: PASS |

**Ranked improvements:**
1. The 400 response carries only the field name ({"field":"title"}); the human-readable reason exists only in the page's JavaScript. Returning a message in the JSON body would make st-005's 'report the reason' observable at the API level.
2. Add a Sea Trial that the page's rendered list is updated after a removal, since that behavior is currently observed only by reading the template source.
