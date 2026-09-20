import os
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


@pytest.mark.parametrize("entrypoint", ["module", "console"])
def test_cli_exits_successfully(entrypoint: str) -> None:
    # Run outside the checkout to verify that the package is installed correctly.
    if entrypoint == "module":
        command = [sys.executable, "-m", "my_python_template"]
    else:
        suffix = ".exe" if os.name == "nt" else ""
        command = [str(Path(sys.executable).parent / f"my-python-template{suffix}")]

    with TemporaryDirectory() as directory:
        result = subprocess.run(command, cwd=directory, capture_output=True, text=True, timeout=10, check=False)

    assert result.returncode == 0, result.stderr
    assert result.stdout == "Hello from my-python-template!\n"
    assert result.stderr == ""
