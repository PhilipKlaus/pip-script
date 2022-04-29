from pathlib import Path
from typing import List

from pipscript.commands import Command


class FreezeCmd(Command):

    def __init__(self):
        super().__init__(["freeze"])

    def run(self) -> None:
        return self._run()

    def _process_output(self, output: bytes) -> List[str]:
        return [x.decode("utf8") for x in output.split(b"\r\n") if len(x)]

    def requirement(self, path: Path):
        self._args += ["--requirement", path.as_posix()]
        return self

    def local(self):
        self._args += ["--local"]
        return self

    def user(self):
        self._args += ["--user"]
        return self

    def path(self, path: Path):
        self._args += ["--path", path.as_posix()]
        return self

    def all(self):
        self._args += ["--all"]
        return self

    def exclude_editable(self):
        self._args += ["--exclude-editable"]
        return self

    def exclude(self, package: str):
        self._args += ["--exclude", package]
        return self
