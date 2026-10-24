#!/bin/sh
# Run the complete automated suite from the application root.
#
# Exits zero only when every test passes. The exit status is pytest's own, so any
# failure, error, or collection problem is reported as non-zero.
# POSIX sh only: no bashisms, arrays, or [[ ]].

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd) || exit 1
app_root=$(CDPATH= cd -- "$script_dir/.." && pwd) || exit 1
cd "$app_root" || exit 1

if [ -f .venv/bin/activate ]; then
    . .venv/bin/activate
fi

pytest -q
