"""Behavior of bin/test.sh, the terminal verification gate.

Each runner check executes a copy of the script inside its own temporary application root,
so the nested suite never re-enters this file and no residue is left in the build directory.
"""

import os
import shutil
import subprocess
from pathlib import Path

RUNNER = Path(__file__).resolve().parents[1] / "bin" / "test.sh"
PROJECT_VENV = Path(__file__).resolve().parents[1] / ".venv"


def _make_root(tmp_path: Path, *, with_venv: bool) -> Path:
    root = tmp_path / "app"
    (root / "bin").mkdir(parents=True)
    shutil.copy(RUNNER, root / "bin" / "test.sh")
    if with_venv:
        os.symlink(PROJECT_VENV, root / ".venv", target_is_directory=True)
    (root / "tests").mkdir()
    return root


def _run(root: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["sh", "bin/test.sh"], cwd=root, capture_output=True, text=True)


def test_runner_parses_as_posix_sh():
    result = subprocess.run(["sh", "-n", str(RUNNER)], capture_output=True, text=True)
    assert result.returncode == 0


def test_runner_exits_nonzero_when_venv_is_missing(tmp_path):
    root = _make_root(tmp_path, with_venv=False)
    (root / "tests" / "test_ok.py").write_text("def test_ok():\n    assert True\n")
    assert _run(root).returncode != 0


def test_runner_exits_zero_when_every_test_passes(tmp_path):
    root = _make_root(tmp_path, with_venv=True)
    (root / "tests" / "test_ok.py").write_text("def test_ok():\n    assert True\n")
    assert _run(root).returncode == 0


def test_runner_exits_nonzero_when_any_test_fails(tmp_path):
    root = _make_root(tmp_path, with_venv=True)
    (root / "tests" / "test_ok.py").write_text("def test_ok():\n    assert True\n")
    (root / "tests" / "test_fail.py").write_text("def test_fail():\n    assert False\n")
    assert _run(root).returncode != 0


def test_runner_runs_from_any_working_directory(tmp_path):
    root = _make_root(tmp_path, with_venv=True)
    (root / "tests" / "test_ok.py").write_text("def test_ok():\n    assert True\n")
    result = subprocess.run(
        ["sh", str(root / "bin" / "test.sh")],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

