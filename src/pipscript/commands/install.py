from pathlib import Path

from src.pipscript.commands import Command


class InstallCmd(Command):

    def __init__(self):
        super().__init__(["install"])

    # Todo return type
    def run(self):
        return self._run()

    def _process_output(self, output: bytes):
        return None

    def no_clean(self):
        self._args.append("--no-clean")
        return self

    def requirement(self, file_path: Path):
        self._args.append("--requirement")
        self._args.append(file_path.as_posix())
        return self
