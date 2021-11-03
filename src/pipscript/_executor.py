import subprocess
import sys
from typing import Callable, Type

from src.pipscript.errors import PipProcessError


def run_cmd(cmd, processor: Callable[[bytes], Type]):
    try:
        if sys.platform == "win32":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            return processor(subprocess.check_output(cmd, stdin=subprocess.DEVNULL, startupinfo=startupinfo))
        else:
            return processor(subprocess.check_output(cmd, stdin=subprocess.DEVNULL))
    except subprocess.CalledProcessError as e:
        raise PipProcessError("Error executing pip command") from e
