#!/bin/sh
# bin/test.sh — terminal verification gate. Runs the complete pytest suite
# from .venv and exits with its status. It runs no subset.
set -u

root=$(cd "$(dirname "$0")/.." && pwd) || exit 1
cd "$root" || exit 1

if [ ! -x .venv/bin/python ]; then
    echo "error: .venv not found at the application root." >&2
    echo "create it with 'uv venv' and install dependencies with 'uv sync'." >&2
    exit 1
fi

exec .venv/bin/python -m pytest -q
