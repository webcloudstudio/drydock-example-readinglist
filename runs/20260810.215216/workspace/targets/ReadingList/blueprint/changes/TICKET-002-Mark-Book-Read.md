# CHANGE: Mark Book Read

| Field       | Value |
|-------------|-------|
| Version | 20260810 V1 |
| Description | Add persisted read state per book, the corresponding BookStore operations, and migration handling for existing rows. |
| Amends | DATABASE.md |
| Depends On | DATABASE.md, ARCHITECTURE.md |
| Scope | amending |
| Origin | reading-list.md |
| Created | 2026-08-10 |
| Stories | mark-read-schema |

This ticket amends DATABASE.md. It supersedes only the sections named under `## Amended Sections`; every other assertion in DATABASE.md remains in force.

## Summary

Add persisted read state per book, the corresponding BookStore operations, and migration handling for existing rows.

## Requirements

### mark-book-read

> The reader can mark a book as read and view whether each book is unread or read.

## Specification

- Add persisted read state per book, the corresponding BookStore operations, and migration handling for existing rows.

## Amended Sections

- Persistence Interfaces
- Schema
- Migrations

## Downstream Impact

This ticket changes a contract other stories consume. Rebuild or defer each:

- add-book (consumes: books persistence interface)
- remove-book (consumes: books persistence interface)
- list-books (consumes: books persistence interface)
