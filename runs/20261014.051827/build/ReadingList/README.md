# ReadingList

## Intent

A small web application that keeps a reader's list of books to read. A reader adds a book with a title and author, views the books in the order added, and removes books. It exists so the reader can track what to read next without losing order or accepting incomplete entries.

## What It Does

A reader adds a book with a title and an author. An empty title or author is rejected with a clear error.

A reader views the books in the order they were added.

A reader removes a book from the list.

The reader's project must provide one command that runs every automated test and reports success only when all of them pass.

The reading list page where a reader adds, views, and removes books.

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
