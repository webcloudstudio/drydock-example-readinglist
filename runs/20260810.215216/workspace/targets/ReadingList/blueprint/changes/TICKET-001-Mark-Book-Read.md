# CHANGE: Mark Book Read

| Field       | Value |
|-------------|-------|
| Version | 20260810 V1 |
| Description | Add the route and application behavior for marking a selected book as read. |
| Amends | ARCHITECTURE.md |
| Depends On | ARCHITECTURE.md, — |
| Scope | amending |
| Origin | reading-list.md |
| Created | 2026-08-10 |
| Stories | mark-read-route |

This ticket amends ARCHITECTURE.md. It supersedes only the sections named under `## Amended Sections`; every other assertion in ARCHITECTURE.md remains in force.

## Summary

Add the route and application behavior for marking a selected book as read.

## Requirements

### mark-book-read

> The reader can mark a book as read and view whether each book is unread or read.

## Specification

- Add the route and application behavior for marking a selected book as read.

## Amended Sections

- Application Boundary
- Programmatic Acceptance

## Downstream Impact

This ticket changes a contract other stories consume. Rebuild or defer each:

- add-book (consumes: books persistence interface)
- remove-book (consumes: books persistence interface)
- list-books (consumes: books persistence interface)
