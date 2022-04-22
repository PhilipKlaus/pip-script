from dataclasses import dataclass
from email.parser import BytesParser
from typing import List, Optional

from pipscript.commands import Command
from pipscript.errors import PipMalformedOutputError, PipUnexpectedError


@dataclass
class PackageShowInfo:
    """
    Package info gathered by the 'pip show' command
    Source: https://github.com/pypa/pip/blob/29ddc93ee8f33f4e1c7402a16b32bdf5b61c7369/src/pip/_internal/commands/show.py
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
    installer: str = None  # Gathered if '--verbose' specified
    metadata_version: str = None  # Gathered if '--verbose' specified
    classifiers: List[str] = None  # Gathered if '--verbose' specified
    entry_points: List[str] = None  # Gathered if '--verbose' specified
    files: Optional[List[str]] = None


class ShowCmd(Command):

    def __init__(self, pkt: str):
        super().__init__(["show", pkt])

    def files(self):
        self._args.append("--files")
        return self

    def run(self) -> PackageShowInfo:
        return self._run()

    def _process_output(self, output: bytes) -> PackageShowInfo:
        try:
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
                data = parser.get(key)

                if key == "Requires" or key == "Required-by":
                    data = data.split(", ")
                elif key == "Classifiers" or key == "Entry-points" or key == "Files":
                    data = data.splitlines()
                    items = data[1:-1] if key == "Entry-points" else data[1:]
                    data = [item.strip() for item in items]
                init_data[fields[key]] = data

            return PackageShowInfo(**init_data)

        except (KeyError, TypeError) as e:
            raise PipMalformedOutputError("Error parsing 'pip show' output. Check installed pip version.") from e
        except Exception as e:
            raise PipUnexpectedError("An unexpected error occurred while parsing 'show' output.") from e
