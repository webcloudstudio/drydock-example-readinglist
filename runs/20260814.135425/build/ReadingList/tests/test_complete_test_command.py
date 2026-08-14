from pathlib import Path
import stat


def test_complete_test_command_is_executable_from_application_root() -> None:
    script = Path("bin/test.sh")

    assert script.is_file()
    assert script.stat().st_mode & (
        stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    )
