from typing import List

import src.pipscript as pip
from src.pipscript.commands import Command


def assert_command_contains_args(cmd: Command, args: List[str]):
    return all([(arg in cmd.args()) for arg in args])


def test_list():
    cmd = pip.list().outdated().uptodate().editable().local().user().path("testpath").pre().not_required(). \
        exclude_editable().include_editable().exclude(["testpkg1", "testpkg2"])

    args = ["pip", "list", "--outdated", "--uptodate", "--editable", "--local", "--user", "--path testpath", "--pre",
            "--not-required", "--exclude-editable", "--include-editable", "--exclude testpkg1", "--exclude testpkg2"]
    assert assert_command_contains_args(cmd, args)


def test_show():
    cmd = pip.show("test").files()

    args = ["pip", "show", "--files", "test"]
    assert assert_command_contains_args(cmd, args)
