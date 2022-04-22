import pytest

import pipscript as pip
from pipscript.errors import PipMalformedOutputError
from tests.asserts import assert_command_contains_args


def get_binary_show_output():
    return b"""Name: test
Version: 1.0.0
Summary: Just a test.
Home-page: https://www.test.org
Author: Max Mustermann.
Author-email: max@mustermann.org
License: MIT
Location: c:\packages
Requires: testa, testb
Required-by: test2, test3
Metadata-Version: 2.0.0
Installer: pip
Classifiers:
  Topic :: Software Development
  Intended Audience :: Developers
Entry-points:
  [console_scripts]
  test = test:main
  
Files: 
  pkg-a
  pkg-b
  pkg-c"""


def assert_packet_info_equals(info):
    assert info.name == "test"
    assert info.version == "1.0.0"
    assert info.summary == "Just a test."
    assert info.homepage == "https://www.test.org"
    assert info.author == "Max Mustermann."
    assert info.author_email == "max@mustermann.org"
    assert info.license == "MIT"
    assert info.location == "c:\packages"
    assert info.requires == ["testa", "testb"]
    assert info.required_by == ["test2", "test3"]
    assert info.metadata_version == "2.0.0"
    assert info.installer == "pip"
    assert info.classifiers == ["Topic :: Software Development", "Intended Audience :: Developers"]
    assert info.entry_points == ["[console_scripts]", "test = test:main"]
    assert info.files == ["pkg-a", "pkg-b", "pkg-c"]


def test_show_args():
    cmd = pip.show("test").files()

    args = ["pip", "show", "--files", "test"]
    assert_command_contains_args(cmd, args)


def test_show_raises_when_parsing_malformed_package():
    show = pip.show("test")

    # Test missing keys
    with pytest.raises(PipMalformedOutputError):
        show._process_output(b"")

    # Test invalid keys
    with pytest.raises(PipMalformedOutputError):
        show._process_output(b"Foo: bar")


def test_show_parses_non_verbose_package():
    show = pip.show("test")
    info = show._process_output(get_binary_show_output())
    assert_packet_info_equals(info)
