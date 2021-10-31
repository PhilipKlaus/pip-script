import json
from dataclasses import dataclass
from typing import List, Optional

from src.pipscript._executor import run_cmd
from src.pipscript.commands import Command


@dataclass
class _Package:
    """
    The package information gathered by the 'pip list' command.
    """
    name: str
    version: str
    latest_version: Optional[str] = None
    latest_filetype: Optional[str] = None
    location: Optional[str] = None  # Gathered if '--verbose' specified
    installer: Optional[str] = None  # Gathered if '--verbose' specified


class ListCmd(Command):
    def __init__(self):
        self._args = ["pip", "list", "--format=json"]

    def __str__(self):
        return " ".join(self._args)

    def args(self):
        return self._args

    def outdated(self):
        self._args.append("--outdated")
        return self

    def uptodate(self):
        self._args.append("--uptodate")
        return self

    def editable(self):
        self._args.append("--editable")
        return self

    def local(self):
        self._args.append("--local")
        return self

    def user(self):
        self._args.append("--user")
        return self

    def path(self, path: str):
        self._args.append(f"--path {path}")
        return self

    def pre(self):
        self._args.append("--pre")
        return self

    def not_required(self):
        self._args.append("--not-required")
        return self

    def exclude_editable(self):
        self._args.append("--exclude-editable")
        return self

    def include_editable(self):
        self._args.append("--include-editable")
        return self

    def exclude(self, pkgs: List[str]):
        [self._args.append(f"--exclude {pkg}") for pkg in pkgs]
        return self

    def run(self) -> List[_Package]:
        pkgs = []
        for entry in json.loads(run_cmd(str(self))):
            pkgs.append(_Package(**entry))
        return pkgs
