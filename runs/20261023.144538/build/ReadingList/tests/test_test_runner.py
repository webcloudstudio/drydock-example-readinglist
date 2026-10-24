"""Test runner tests: bin/test.sh is POSIX sh, runs the whole suite, and reports its verdict.

Each behavior is exercised by running the real runner against a temporary application root
and reading back the process exit status. Temporary roots carry their own tests, so the
runner's verdict is observed without re-entering this suite.
"""

import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNNER = PROJECT_ROOT / "bin" / "test.sh"
VENV_BIN = Path(sys.executable).parent  # not resolved: the venv's own bin holds pytest


def _make_app_root(root: Path, test_source: str) -> Path:
    """Build a minimal application root holding the runner and one test module."""
    (root / "bin").mkdir(parents=True)
    shutil.copy(RUNNER, root / "bin" / "test.sh")
    (root / "tests").mkdir()
    (root / "tests" / "test_sample.py").write_text(test_source)
    return root


def _run_runner(runner: Path, cwd: Path) -> subprocess.CompletedProcess:
    """Run the runner with pytest reachable on PATH and no project .venv in the temporary root."""
    env = {"PATH": f"{VENV_BIN}:/usr/bin:/bin", "HOME": str(cwd)}
    return subprocess.run(["sh", str(runner)], cwd=cwd, env=env, capture_output=True, text=True)


def test_runner_is_posix_sh_syntax():
    result = subprocess.run(["sh", "-n", str(RUNNER)], capture_output=True, text=True)

    assert result.returncode == 0


def test_runner_exits_zero_when_every_test_passes(tmp_path):
    root = _make_app_root(tmp_path / "app", "def test_passes():\n    assert 1 + 1 == 2\n")

    result = _run_runner(root / "bin" / "test.sh", cwd=tmp_path)

    assert result.returncode == 0


def test_runner_exits_nonzero_when_a_test_fails(tmp_path):
    root = _make_app_root(tmp_path / "app", "def test_fails():\n    assert 1 + 1 == 3\n")

    result = _run_runner(root / "bin" / "test.sh", cwd=tmp_path)

    assert result.returncode != 0


def test_runner_exits_nonzero_when_one_of_many_tests_fails(tmp_path):
    source = (
        "def test_first():\n    assert True\n\n"
        "def test_second():\n    assert False\n\n"
        "def test_third():\n    assert True\n"
    )
    root = _make_app_root(tmp_path / "app", source)

    result = _run_runner(root / "bin" / "test.sh", cwd=tmp_path)

    assert result.returncode != 0


def test_runner_runs_from_application_root_regardless_of_working_directory(tmp_path):
    # Started from tmp_path, not the application root: the run only finds and passes the
    # temporary suite if the runner changed into the application root before pytest.
    root = _make_app_root(tmp_path / "app", "def test_passes():\n    assert True\n")
    unrelated = tmp_path / "unrelated"
    unrelated.mkdir()

    result = _run_runner(root / "bin" / "test.sh", cwd=unrelated)

    assert result.returncode == 0


def test_runner_exit_status_is_pytest_status_for_failing_suite(tmp_path):
    root = _make_app_root(tmp_path / "app", "def test_fails():\n    assert False\n")

    result = _run_runner(root / "bin" / "test.sh", cwd=tmp_path)

    # pytest reports a failed run with exit status 1; the runner must not mask it.
    assert result.returncode == 1
