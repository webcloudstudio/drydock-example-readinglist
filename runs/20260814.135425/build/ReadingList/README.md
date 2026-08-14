# ReadingList

A web application for maintaining an ordered reading list of books and tracking which books have been read.

## Intent

ReadingList is a small web application for readers who want to maintain an ordered list of books to read. A reader can add books with a title and author, inspect their reading status, mark books as read, and remove books. The application exists to make this workflow simple and verifiable.

## What It Does

A reader submits a title and author through the reading-list form. The application validates the submission before persistence, creates the book through `Database.create_book`, and returns a response that makes the new book available to the reading-list view.

The project test suite verifies the public reading-list workflows, including creation, validation, ordering, removal, marking books read, and displaying status.

The application root provides an executable `bin/test.sh` command. Running `sh bin/test.sh` invokes the complete automated suite and returns success only when the suite succeeds.

A reader can mark a book as read. The selected book's persisted status changes from unread to read and is shown as read on the next list view.

Books are retrieved in their addition order. Each book exposes a durable read-status value of unread or read, and later reads preserve that status.

A reader can remove a selected book, after which the book is absent from the next reading-list view while other books remain available.

The application rejects a submission when its title or author is empty, including when the value contains only surrounding whitespace. Rejected submissions return HTTP `400`, preserve the form context, and do not create a database row. The response includes a clear reason for the rejection for the reader.

Defines the browser screen for viewing and managing the ordered reading list.

## Setup and Running

**Before first run:**

- Confirm the repository has the expected remote with `git remote -v`; add `origin` if the startup guard requires it.
- Run `git status --short` and commit or intentionally stash local changes before deployment-oriented runs.

**Install dependencies:**

```bash
pip install -e .
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
