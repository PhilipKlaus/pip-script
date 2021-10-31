from typing import List

from src.pipscript._executor import run_cmd


class Command:

    def __init__(self, command: List[str]):
        self._args = ["pip"] + command

    def __str__(self):
        return " ".join(self._args)

    def args(self) -> List[str]:
        return self._args

    def run(self):
        return run_cmd(str(self), self._process_output)

    def _process_output(self, output: bytes):
        raise NotImplementedError()
