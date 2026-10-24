# ReadingList

A web application for maintaining an ordered list of books to read.

## Intent

ReadingList is a small web application for readers who want to maintain a personal list of books to read. A reader can add books with titles and authors, view them in insertion order, and remove them. The application must be easy to exercise through its primary web page and fully verifiable through its supplied test runner.

## What It Does

A reader submits a title and author to `POST /books`. The feature persists the book through `books.create` and returns the reader to a usable reading-list workflow where the new book can be seen.

The primary reading-list page retrieves persisted books through `persistence.books.list` and presents them in insertion order. It renders a clear empty state when no books are available.

A reader submits the removal action for a selected book. The feature deletes only that persisted identifier through `books.delete`, then returns to the list workflow.

The validation boundary protects the reading list from incomplete books. Submissions with an empty title, empty author, or both are rejected before persistence with a client-error response. The form remains usable so the reader can correct and resubmit.

Defines the primary server-rendered screen for maintaining the reading list.

## Setup and Running

**Before first run:**

- Confirm the repository has the expected remote with `git remote -v`; add `origin` if the startup guard requires it.
- Run `git status --short` and commit or intentionally stash local changes before deployment-oriented runs.

**Install dependencies:**

```bash
uv sync
```

## Verification

```bash
bash bin/test.sh
```

## Next Steps

- Complete the first-run checks above.
- Run `bash bin/test.sh` before making release or deployment changes.
