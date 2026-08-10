# CHANGE: Mark Book Read

| Field       | Value |
|-------------|-------|
| Version | 20260810 V1 |
| Description | Display each book's unread or read state and provide the mark-read control. |
| Amends | SCREEN-Reading-List.md |
| Depends On | SCREEN-Reading-List.md, UI-GENERAL.md, FEATURE-Add-Book.md, FEATURE-List-Books.md, FEATURE-Validate-Book.md, FEATURE-Remove-Book.md |
| Scope | amending |
| Origin | reading-list.md |
| Created | 2026-08-10 |
| Stories | mark-read-view |

This ticket amends SCREEN-Reading-List.md. It supersedes only the sections named under `## Amended Sections`; every other assertion in SCREEN-Reading-List.md remains in force.

## Summary

Display each book's unread or read state and provide the mark-read control.

## Requirements

### mark-book-read

> The reader can mark a book as read and view whether each book is unread or read.

## Specification

- Display each book's unread or read state and provide the mark-read control.

## Amended Sections

- Layout and Interactions
- Programmatic Acceptance

## Downstream Impact

This ticket changes a contract other stories consume. Rebuild or defer each:

- add-book (consumes: books persistence interface)
- remove-book (consumes: books persistence interface)
- list-books (consumes: books persistence interface)
