# ReadingList

A web application for maintaining an ordered list of books to read.

## Intent

ReadingList is a small web application for readers who want to maintain a personal, ordered list of books to read. A reader can add a book with its title and author, review books in insertion order, and remove books when they are no longer needed.

## What It Does

Allow a reader to submit a non-empty title and author and have the book stored in the reading list.

Allow a reader to remove a selected book from the reading list.

Validate book submissions at the submission boundary before persistence.

Show every stored book in the same order in which it was added.

Provide automated tests for adding books, preserving insertion order, removing books, and rejecting empty titles or authors. The root-level `bin/test.sh` launcher is POSIX-compatible and runs the complete suite from the application root.

Presents the reader-facing form, ordered book list, empty state, validation feedback, and removal controls.

## Setup and Running

**Before first run:**

- Copy `.env.example` to `.env` and fill in local values before starting.
- Confirm the repository has the expected remote with `git remote -v`; add `origin` if the startup guard requires it.
- Run `git status --short` and commit or intentionally stash local changes before deployment-oriented runs.

**Install dependencies:**

```bash
uv sync
```

**Start the application:**

```bash
python run.py
```

## Verification

```bash
bash bin/test.sh
```

## Next Steps

- Complete the first-run checks above.
- Start the application with `python run.py`.
- Run `bash bin/test.sh` before making release or deployment changes.
