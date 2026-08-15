# Release Scorecard: ReadingList

- Verdict: PASSED
- Code identity: 2f884934bb2267041cab4c34d4f2b3d3e743ad36

## Project acceptance

| ID | Type | Criterion | Verdict | Observed |
|---|---|---|---|---|
| st-001 | technical | The application shall provide a POSIX-compatible bin/test.sh that exits zero when every automated test passes. | MET | bin/test.sh; command: bash bin/test.sh exited 0 with 44 passed |
| st-002 | behavioral | When a reader submits a title and an author, the application shall store the book and show it in the list. | MET | app/routes.py:19; app/persistence.py:52; probe: add submissions returned redirects and listed both books |
| st-003 | behavioral | The application shall present books in the order they were added. | MET | app/persistence.py:76; probe: body.index("First") < body.index("Second") |
| st-004 | behavioral | When a reader removes a book, the application shall omit it from the list on the next read. | MET | app/routes.py:37; app/persistence.py:92; probe: removed First; Second remained and First was absent |
| st-005 | behavioral | If a submission carries an empty title or an empty author, then the application shall reject it and report the reason. | MET | app/routes.py:23; app/templates/index.html:8; probe: both invalid submissions returned 400 with role="alert" |
| st-006 | technical | The application shall carry automated tests for adding a book, listing books in the order added, removing a book, rejecting an empty title or author | MET | tests/test_persistence.py:5; tests/test_persistence.py:45; tests/test_persistence.py:66; tests/test_persistence.py:78; tests/test_routes.py:3; command: bash bin/test.sh reported 44 passed |

## Failures

- None.

## Manual verification required

- None.

## Could not judge

- None.

## Advisory warnings

- Build directory has uncommitted changes

## Ranked improvements

None.
