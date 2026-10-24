# ReadingList

A web application for keeping a personal list of books to read, with add, ordered view, and remove.

## Intent

A web application that lets a reader keep a personal list of books to read. The reader adds a book with a title and author, views books in the order they were added, and removes books. It serves a single reader who needs a simple, dependable reading list with clear feedback on invalid input.

## What It Does

Let the reader add a book. A valid submission is stored and returned; the new book appears in later list reads.

Provide the runnable Flask application that later features register routes on, plus the shared base template and the in-process test client used by acceptance and pytest.

Let the reader view the books. Books are never presented in any order other than the order added.

Guarantee the application never accepts an empty title or empty author. Rejection reports a clear, human-readable error naming the offending field.

A reader removes a book they no longer want on their list. Once removed, the book must be absent from every subsequent list read, and the remaining books keep the order in which they were added.

Give the reader and the build a single dependable command, `sh bin/test.sh`, run from the application root, that executes every automated test and reports success only when all of them pass. This is the terminal verification story: it runs after every implementation story, and its command, exit code, standard output, and standard error are preserved as evidence.

Server-rendered page that shows the reading list in the order added, with an add form, error display, and per-book remove buttons.

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
