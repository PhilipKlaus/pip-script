from pathlib import Path
from typing import List, Union

from pipscript.commands import Command


class InstallCmd(Command):

    def __init__(self, package: Union[str, Path] = None):
        super().__init__(["install"])
        if package:
            package = package if type(package) == str else package.as_posix()
            self._args.append(package)

    # Todo return type
    def run(self):
        return self._run()

    def _process_output(self, output: bytes):
        return None

    def requirement(self, file_paths: List[Path]):
        for path in file_paths:
            self._args += ["--requirement", path.as_posix()]
        return self

    def constraint(self, file_paths: List[Path]):
        for path in file_paths:
            self._args += ["--constraint", path.as_posix()]
        return self

    def no_deps(self):
        self._args.append("--no-deps")
        return self

    def pre(self):
        self._args.append("--pre")
        return self

    def editable(self, package: Union[str, Path]):
        package = package if isinstance(package, str) else package.as_posix()
        self._args += ["--editable", package]
        return self

    def target(self, path: Path):
        self._args += ["--target", path.as_posix()]
        return self

    def platform(self, platform: str):
        self._args += ["--platform", platform]
        return self

    def python_version(self, version: str):
        self._args += ["--python-version", version]
        return self

    def implementation(self, implementation: str):
        self._args += ["--implementation", implementation]
        return self

    def abi(self, abi: str):
        self._args += ["--abi", abi]
        return self

    def user(self):
        self._args += ["--user"]
        return self

    def root(self, path: Path):
        self._args += ["--root", path.as_posix()]
        return self

    def prefix(self, path: Path):
        self._args += ["--prefix", path.as_posix()]
        return self

    def src(self, path: Path):
        self._args += ["--src", path.as_posix()]
        return self

    def upgrade(self):
        self._args += ["--upgrade"]
        return self

    def upgrade_strategy(self, strategy: str):
        self._args += ["--upgrade-strategy", strategy]
        return self

    def force_reinstall(self):
        self._args += ["--force-reinstall"]
        return self

    def ignore_installed(self):
        self._args += ["--ignore-installed"]
        return self

    def ignore_requires_python(self):
        self._args += ["--ignore-requires-python"]
        return self

    def no_build_isolation(self):
        self._args += ["--no-build-isolation"]
        return self

    def use_pep517(self):
        self._args += ["--use-pep517"]
        return self

    def no_use_pep517(self):
        self._args += ["--no-use-pep517"]
        return self

    def install_option(self, options: List[str]):
        for option in options:
            self._args += ["--install-option", f"\"{option}\""]
        return self

    def global_option(self, options: List[str]):
        for option in options:
            self._args += ["--global-option", f"\"{option}\""]
        return self

    def compile(self):
        self._args += ["--compile"]
        return self

    def no_compile(self):
        self._args += ["--no-compile"]
        return self

    def no_warn_script_location(self):
        self._args += ["--no-warn-script-location"]
        return self

    def no_warn_conflicts(self):
        self._args += ["--no-warn-conflicts"]
        return self

    def no_binary(self, format_control: str):
        self._args += ["--no-binary", format_control]
        return self

    def only_binary(self, format_control: str):
        self._args += ["--only-binary", format_control]
        return self

    def prefer_binary(self):
        self._args.append("--prefer-binary")
        return self

    def require_hashes(self):
        self._args.append("--require-hashes")
        return self

    def no_clean(self):
        self._args.append("--no-clean")
        return self

