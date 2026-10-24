"""Behavior tests for bin/test.sh, the POSIX entry point for the full suite.

Each test runs the real script from a temporary application root. A stub `pytest` placed first on
PATH records what it observed and exits with a chosen status, so the script's own behavior is
checked without recursively running this suite.
"""

import os
import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = PROJECT_ROOT / "bin" / "test.sh"

RunScript = Callable[..., subprocess.CompletedProcess]


def _write_executable(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    path.chmod(0o755)


@pytest.fixture
def app_root(tmp_path: Path) -> Path:
    """Return a temporary application root holding a copy of the real bin/test.sh."""
    root = tmp_path / "app"
    (root / "bin").mkdir(parents=True)
    shutil.copy2(SCRIPT, root / "bin" / "test.sh")
    return root


@pytest.fixture
def stub_bin(tmp_path: Path) -> Path:
    """Return a directory that will hold the stub pytest, placed first on PATH."""
    directory = tmp_path / "stubs"
    directory.mkdir()
    return directory


@pytest.fixture
def run_script(app_root: Path, stub_bin: Path) -> RunScript:
    """Return a runner that executes `sh bin/test.sh` with the given stub exit status."""

    def run(status: int = 0, cwd: Path | None = None) -> subprocess.CompletedProcess:
        record = app_root.parent / "pytest-record.txt"
        _write_executable(
            stub_bin / "pytest",
            "#!/bin/sh\n"
            f'printf "%s\\n" "$(pwd)" "$*" "${{RL_VENV_MARKER:-unset}}" > "{record}"\n'
            f"exit {status}\n",
        )
        env = {**os.environ, "PATH": f"{stub_bin}{os.pathsep}{os.environ['PATH']}"}
        env.pop("RL_VENV_MARKER", None)
        return subprocess.run(
            ["sh", str(app_root / "bin" / "test.sh")],
            cwd=cwd or app_root,
            env=env,
            capture_output=True,
            text=True,
        )

    return run


def _read_record(app_root: Path) -> list[str]:
    return (app_root.parent / "pytest-record.txt").read_text(encoding="utf-8").splitlines()


def test_runner_exits_zero_when_pytest_passes(run_script: RunScript) -> None:
    result = run_script(status=0)

    assert result.returncode == 0


def test_runner_passes_through_pytest_failure_status(run_script: RunScript) -> None:
    result = run_script(status=3)

    assert result.returncode == 3


def test_runner_passes_through_pytest_error_status(run_script: RunScript) -> None:
    result = run_script(status=5)

    assert result.returncode == 5


def test_runner_invokes_pytest_quietly(run_script: RunScript, app_root: Path) -> None:
    run_script(status=0)

    assert _read_record(app_root)[1] == "-q"


def test_runner_changes_to_app_root_from_another_directory(
    run_script: RunScript, app_root: Path, tmp_path: Path
) -> None:
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()

    result = run_script(status=0, cwd=elsewhere)

    assert result.returncode == 0
    assert Path(_read_record(app_root)[0]).resolve() == app_root.resolve()


def test_runner_activates_venv_when_present(run_script: RunScript, app_root: Path) -> None:
    _write_executable(
        app_root / ".venv" / "bin" / "activate",
        'export RL_VENV_MARKER="activated"\n',
    )

    run_script(status=0)

    assert _read_record(app_root)[2] == "activated"


def test_runner_uses_path_pytest_when_venv_absent(run_script: RunScript, app_root: Path) -> None:
    assert not (app_root / ".venv").exists()

    result = run_script(status=0)

    assert result.returncode == 0
    assert _read_record(app_root)[2] == "unset"
