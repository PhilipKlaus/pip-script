from dataclasses import dataclass
from email.parser import BytesParser
from typing import List, Optional

from src.pipscript.commands import Command


@dataclass
class _PackageInfo:
    """
    PacketInfo gathered by the 'pip show' command
    Source: https://github.com/pypa/pip/blob/main/src/pip/_internal/commands/show.py
    """
    name: str
    version: str
    location: str
    requires: List[str]
    required_by: List[str]
    summary: str
    homepage: str
    author: str
    author_email: str
    license: str
    files: Optional[List[str]] = None
    installer: str = None  # Gathered if '--verbose' specified
    metadata_version: str = None  # Gathered if '--verbose' specified
    classifiers: List[str] = None  # Gathered if '--verbose' specified
    entry_points: List[str] = None  # Gathered if '--verbose' specified


class ShowCmd(Command):

    def __init__(self, pkt: str):
        super().__init__(["show", pkt])

    def files(self):
        self._args.append("--files")
        return self

    def _process_output(self, output: bytes):
        parser = BytesParser().parsebytes(output)
        fields = {"Name": "name",
                  "Version": "version",
                  "Location": "location",
                  "Requires": "requires",
                  "Required-by": "required_by",
                  "Installer": "installer",
                  "Metadata-Version": "metadata_version",
                  "Classifiers": "classifiers",
                  "Summary": "summary",
                  "Home-page": "homepage",
                  "Author": "author",
                  "Author-email": "author_email",
                  "License": "license",
                  "Entry-points": "entry_points",
                  "Files": "files"}
        init_data = {}
        for key in parser.keys():
            init_data[fields[key]] = parser.get(key)

        # ToDo: apply appropriate 'Files' parsing

        return _PackageInfo(**init_data)
