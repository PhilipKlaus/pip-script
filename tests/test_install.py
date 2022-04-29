from pathlib import Path

import pipscript as pip
from tests.asserts import assert_command_contains_args


def test_install_args():
    cmd = pip.install("dummypkg").requirement([Path("testrequirement")]).constraint(
        [Path("constraint1"), Path("constraint2")]).no_deps().pre().editable(Path("testeditable")).target(
        Path("testtarget")).platform("testplatform").python_version("3.9.0").implementation("testimpl").abi(
        "testabi").user().root(Path("testroot")).prefix(Path("testprefix")).src(
        Path("testsrc")).upgrade().upgrade_strategy(
        "teststrategy").force_reinstall().ignore_installed().ignore_requires_python().no_build_isolation().use_pep517(
    ).no_use_pep517().install_option(["installoption1", "installoption2"]).global_option(
        ["globaloption1",
         "globaloption2"]).compile().no_compile().no_warn_script_location().no_warn_conflicts().no_binary(
        "testnobinary").only_binary("testonlybinary").prefer_binary().require_hashes().no_clean()

    args = ["-m", "pip", "install", "dummypkg", "--requirement", "testrequirement", "--constraint", "constraint1",
            "constraint2", "--no-deps", "--pre", "--editable", "testeditable", "--target", "testtarget", "--platform",
            "testplatform", "--python-version", "3.9.0", "--implementation", "testimpl", "--abi", "testabi", "--user",
            "--root", "testroot", "--prefix", "testprefix", "--src", "testsrc", "--upgrade", "--upgrade-strategy",
            "teststrategy", "--force-reinstall", "--ignore-installed", "--ignore-requires-python",
            "--no-build-isolation", "--use-pep517", "--no-use-pep517", "--install-option", "\"installoption1\"",
            "\"installoption2\"", "--global-option", "\"globaloption1\"", "\"globaloption2\"", "--compile",
            "--no-compile", "--no-warn-script-location", "--no-warn-conflicts", "--no-binary", "testnobinary",
            "--only-binary", "testonlybinary", "--prefer-binary", "--require-hashes", "--no-clean"]
    assert_command_contains_args(cmd, args)
