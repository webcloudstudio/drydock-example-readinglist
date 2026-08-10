import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
RUNNER = PROJECT_ROOT / "bin" / "test.sh"


def test_runner_is_posix_shell_and_executable():
    assert RUNNER.stat().st_mode & 0o111
    result = subprocess.run(
        ["sh", "-n", str(RUNNER)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0


def test_runner_executes_complete_pytest_suite_from_application_root():
    runner_source = RUNNER.read_text(encoding="utf-8")

    assert 'cd "$(dirname "$0")/.."' in runner_source
    assert "exec python -m pytest" in runner_source
    assert "pytest " not in runner_source
