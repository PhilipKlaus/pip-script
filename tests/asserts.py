from typing import List

from pipscript.commands import Command


def assert_command_contains_args(cmd: Command, args: List[str]):
    assert all([(arg in cmd.args()) for arg in args])
