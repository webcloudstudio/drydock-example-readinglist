import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = PROJECT_ROOT / "bin" / "test.sh"


def test_test_launcher_has_valid_posix_syntax():
    result = subprocess.run(
        ["sh", "-n", str(LAUNCHER)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0


def test_test_launcher_runs_pytest_from_project_root():
    launcher_text = LAUNCHER.read_text()

    assert 'cd "$(dirname "$0")/.."' in launcher_text
    assert "pytest tests/" in launcher_text
