#!/bin/sh
# ReadingList full test suite runner.
# Runs the complete pytest suite from the application root and exits with pytest's status.
set -eu

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

if [ -f .venv/bin/activate ]; then
    # The venv activate script reads variables that may be unset, so relax -u only for it.
    set +u
    . .venv/bin/activate
    set -u
fi

exec pytest -q
