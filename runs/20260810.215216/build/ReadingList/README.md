# ReadingList

A web application for maintaining an ordered list of books to read.

## Intent

ReadingList is a web application for readers who want to maintain a personal list of books to read. It lets a reader add books with titles and authors, view them in insertion order, and remove them.

## What It Does

Present the reading list and controls for adding and removing books.

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
