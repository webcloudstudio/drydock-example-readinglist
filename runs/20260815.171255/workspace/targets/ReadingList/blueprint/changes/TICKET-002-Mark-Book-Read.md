# CHANGE: Mark Book Read

| Field       | Value |
|-------------|-------|
| Version | 20260815 V1 |
| Description | Add the mark-read action and route for a listed book. Render each book's read or unread state and provide the mark-read control. |
| Amends | SCREEN-Reading-List.md |
| Depends On | SCREEN-Reading-List.md, UI-GENERAL.md, FEATURE-Book-Creation.md, FEATURE-Ordered-List.md, FEATURE-Book-Removal.md, FEATURE-Incomplete-Submission.md |
| Scope | additive |
| Origin | reading-list.md@02f4924 |
| Created | 2026-08-15 |
| Stories | mark-read-route, mark-read-view |

This ticket is additive. It supersedes nothing; every assertion in SCREEN-Reading-List.md remains in force.

## Summary

Add the mark-read action and route for a listed book. Render each book's read or unread state and provide the mark-read control.

## Requirements

### mark-book-read

> The reader can mark a book as read and view whether each book is unread or read.

### mark-book-read

> The reader can mark a book as read and view whether each book is unread or read.

## Specification

- Add the mark-read action and route for a listed book.

- Render each book's read or unread state and provide the mark-read control.

## Downstream Impact

This ticket changes a contract other stories consume. Rebuild or defer each:

- book-creation (consumes: book_store.add)
- ordered-list (consumes: book_store.list_ordered)
- book-removal (consumes: book_store.remove)
- book-creation (consumes: books_table)
- ordered-list (consumes: books_table)
- verification-suite (consumes: reading_list_screen)
