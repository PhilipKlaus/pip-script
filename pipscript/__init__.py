def list():
    from pipscript.commands.list import ListCmd
    return ListCmd()


def show(pkt: str):
    from pipscript.commands.show import ShowCmd
    return ShowCmd(pkt)


def install(pkt: str):
    from pipscript.commands.install import InstallCmd
    return InstallCmd(pkt)
