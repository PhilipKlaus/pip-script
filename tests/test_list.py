import pytest

import src.pipscript as pip
from src.pipscript.errors import PipMalformedOutputError
from tests.asserts import assert_command_contains_args


def get_binary_list_output():
    return b'[{"name": "test-a", "version": "1.0.0", "location": "c:\\\\packages", "installer": "pip",' \
           b'"latest_version": "1.1.0", "latest_filetype": "wheel"},' \
           b'{"name": "test-b", "version": "2.0.0", "location": "c:\\\\packages", "installer": "pip",' \
           b'"latest_version": "2.1.0", "latest_filetype": "wheel"},' \
           b'{"name": "test-c", "version": "3.0.0", "location": "c:\\\\packages", "installer": "pip",' \
           b'"latest_version": "3.1.0", "latest_filetype": "wheel"}]\r\n'


def assert_packet_info_equals(info, name: str, vers: str, location: str, installer: str, latest_v: str, latest_f: str):
    assert info.name == name
    assert info.version == vers
    assert info.location == location
    assert info.installer == installer
    assert info.latest_version == latest_v
    assert info.latest_filetype == latest_f


def test_list_args():
    cmd = pip.list().outdated().uptodate().editable().local().user().path("testpath").pre().not_required(). \
        exclude_editable().include_editable().exclude(["testpkg1", "testpkg2"])

    args = ["pip", "list", "--outdated", "--uptodate", "--editable", "--local", "--user", "--path testpath", "--pre",
            "--not-required", "--exclude-editable", "--include-editable", "--exclude testpkg1", "--exclude testpkg2"]
    assert_command_contains_args(cmd, args)


def test_list_raises_when_parsing_malformed_package():
    list_cmd = pip.list()

    # Test missing keys
    with pytest.raises(PipMalformedOutputError):
        list_cmd._process_output(b"")

    # Test invalid keys
    with pytest.raises(PipMalformedOutputError):
        list_cmd._process_output(b"Foo: bar")


def test_list_parses_non_verbose_package():
    list_cmd = pip.list()
    info = list_cmd._process_output(get_binary_list_output())
    assert len(info) == 3
    assert_packet_info_equals(info[0], "test-a", "1.0.0", "c:\\packages", "pip", "1.1.0", "wheel")
    assert_packet_info_equals(info[1], "test-b", "2.0.0", "c:\\packages", "pip", "2.1.0", "wheel")
    assert_packet_info_equals(info[2], "test-c", "3.0.0", "c:\\packages", "pip", "3.1.0", "wheel")
