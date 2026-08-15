# CHANGE: Mark Book Read

| Field       | Value |
|-------------|-------|
| Version | 20260815 V1 |
| Description | Add persisted read state per book and migrate existing rows. |
| Amends | DATABASE.md |
| Depends On | DATABASE.md, ARCHITECTURE.md |
| Scope | amending |
| Origin | reading-list.md@02f4924 |
| Created | 2026-08-15 |
| Stories | mark-read-schema |

This ticket amends DATABASE.md. It supersedes only the sections named under `## Amended Sections`; every other assertion in DATABASE.md remains in force.

## Summary

Add persisted read state per book and migrate existing rows.

## Requirements

### mark-book-read

> The reader can mark a book as read and view whether each book is unread or read.

## Specification

- Add persisted read state per book and migrate existing rows.

## Amended Sections

- Schema

## Downstream Impact

This ticket changes a contract other stories consume. Rebuild or defer each:

- book-creation (consumes: book_store.add)
- ordered-list (consumes: book_store.list_ordered)
- book-removal (consumes: book_store.remove)
- book-creation (consumes: books_table)
- ordered-list (consumes: books_table)
- verification-suite (consumes: reading_list_screen)
