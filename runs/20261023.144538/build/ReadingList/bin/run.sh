#!/bin/sh
# ReadingList development server launcher.
# Activates the project .venv and starts Flask with the application factory.
set -eu

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

if [ ! -f .venv/bin/activate ]; then
    echo "error: .venv is missing. Run 'uv sync' from the application root first." >&2
    exit 1
fi

. .venv/bin/activate
exec flask --app app_server:create_app run "$@"
