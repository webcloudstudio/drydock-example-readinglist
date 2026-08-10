# CHANGE: Mark Book Read

| Field       | Value |
|-------------|-------|
| Version | 20260810 V1 |
| Description | Add automated coverage for persisted read state, marking books read, and rendering read and unread states. |
| Amends | FEATURE-Verification.md |
| Depends On | FEATURE-Verification.md, ARCHITECTURE.md, DATABASE.md, UI-GENERAL.md, FEATURE-Add-Book.md, FEATURE-List-Books.md, FEATURE-Validate-Book.md, FEATURE-Remove-Book.md, SCREEN-Reading-List.md |
| Scope | amending |
| Origin | reading-list.md |
| Created | 2026-08-10 |
| Stories | mark-read-verification |

This ticket amends FEATURE-Verification.md. It supersedes only the sections named under `## Amended Sections`; every other assertion in FEATURE-Verification.md remains in force.

## Summary

Add automated coverage for persisted read state, marking books read, and rendering read and unread states.

## Requirements

### mark-book-read

> The reader can mark a book as read and view whether each book is unread or read.

## Specification

- Add automated coverage for persisted read state, marking books read, and rendering read and unread states.

## Amended Sections

- Verification Workflow
- Programmatic Acceptance

## Downstream Impact

This ticket changes a contract other stories consume. Rebuild or defer each:

- add-book (consumes: books persistence interface)
- remove-book (consumes: books persistence interface)
- list-books (consumes: books persistence interface)
