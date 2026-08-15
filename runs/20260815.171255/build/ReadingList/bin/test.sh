#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
# Keep the verification boundary at the project root so every configured test is collected.
exec uv run --extra dev pytest tests/
