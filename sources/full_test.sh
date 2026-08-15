#!/bin/sh
# full_test.sh — scoring entry point. Do not filter, skip, or reinterpret.
#
# `drydock uat` runs `sh sources/full_test.sh` from the completed application root and takes its
# exit code and output as the score.
#
# Unlike a conformance fixture, this Target supplies no suite of its own: the source prose makes
# "the application provides a POSIX-compatible bin/test.sh" a product requirement (st-001), so the
# tests are part of the deliverable. This harness is therefore a dispatcher, and its whole value
# is that it is still Commander-owned. An absent bin/test.sh is a delivered product that failed to
# meet st-001, which this script reports as a failure — rather than leaving the release gate with
# no oracle at all, where an unbuilt project grades PASSED by default.
set -eu

if [ ! -f bin/test.sh ]; then
    echo "error: no bin/test.sh at the application root." >&2
    echo "st-001 requires the application to provide a POSIX-compatible bin/test.sh that exits" >&2
    echo "zero when every automated test passes." >&2
    exit 1
fi

exec sh bin/test.sh
