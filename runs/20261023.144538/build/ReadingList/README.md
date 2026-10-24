# ReadingList

## Intent

A reader-facing web application for keeping an ordered list of books to read. Each book has a title and an author. Readers add, view in insertion order, and remove books. The product exists so a reader can track what they intend to read without losing track of the order they added titles.

## What It Does

Let a reader add a book to the end of the reading list.

Guarantee that adding a book is covered by an automated test that runs under `pytest -q`.

Let a reader (and the reading list page) view every book in the order added.

Guarantee that listing books in the order added is covered by an automated test that runs under `pytest -q`.

The reader must never be able to add a book without an author. The submission is rejected and the reader is told why.

The reader must never be able to add a book without a title. The submission is rejected and the reader is told why.

Let a reader remove a book from the reading list.

The Reading List guardrail "Never ship a behavior without an automated test covering it" applies to removal. This specification governs the project's own pytest module `tests/test_remove_book.py`, written by the build agent beside the finished code against observed output. It exercises removal only through the public HTTP interface.

The guardrails "Never accept an empty title or an empty author" and "Never omit a rejection reason when a submission is rejected" require automated coverage. This specification governs the project's own pytest module `tests/test_validation.py`, written by the build agent beside the finished code. It exercises validation only through `POST /books` and `GET /books`.

The single page where a reader adds books, sees them in the order added, sees rejection reasons, and removes books.

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
