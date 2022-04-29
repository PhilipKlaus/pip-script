import sys
from typing import List

from pipscript._executor import run_cmd


class Command:

    def __init__(self, command: List[str]):
        self._args = [sys.executable, "-m", "pip"] + command

    def __str__(self):
        return " ".join(self._args)

    def args(self) -> List[str]:
        return self._args

    def _run(self):
        return run_cmd(str(self), self._process_output)

    def _process_output(self, output: bytes):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()
