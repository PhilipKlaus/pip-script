import dataclasses
import json
from dataclasses import dataclass
from json import JSONDecodeError
from pathlib import Path
from typing import List, Optional

from pipscript.commands import Command
from pipscript.errors import PipMalformedOutputError, PipUnexpectedError


@dataclass(init=False)
class PackageListInfo:
    """
    The package information gathered by the 'pip list' command.
    """
    name: str
    version: str
    latest_version: Optional[str] = None  # Only gathered if e.g. '--outdated' specified
    latest_filetype: Optional[str] = None  # Only gathered if e.g. '--outdated' specified
    location: Optional[str] = None  # Only gathered if '--verbose' specified
    installer: Optional[str] = None  # Only gathered if '--verbose' specified

    def __init__(self, **kwargs):
        """
        Custom constructor to ignore additional fields (e.g. from future unsupported pip versions).
        :param kwargs:  The fields to set.
        """
        names = set([f.name for f in dataclasses.fields(self)])
        for k, v in kwargs.items():
            if k in names:
                setattr(self, k, v)


class ListCmd(Command):

    def __init__(self):
        super().__init__(["list", "--format=json"])

    def run(self) -> PackageListInfo:
        return self._run()

    def _process_output(self, output: bytes) -> List[PackageListInfo]:
        try:
            pkgs = []
            for entry in json.loads(output):
                pkgs.append(PackageListInfo(**entry))
            return pkgs

        except (TypeError, JSONDecodeError) as e:
            raise PipMalformedOutputError("Error parsing 'pip list' output. Check installed pip version.") from e
        except Exception as e:
            raise PipUnexpectedError("An unexpected error occurred while parsing 'list' output.") from e

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

    def path(self, path: Path):
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
