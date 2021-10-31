import subprocess
import sys


def run_cmd(cmd):
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        return subprocess.check_output(cmd, stdin=subprocess.DEVNULL, startupinfo=startupinfo)
    else:
        return subprocess.check_output(cmd, stdin=subprocess.DEVNULL)
