def list():
    from src.pipscript.commands.list import ListCmd
    return ListCmd()


def show(pkt: str):
    from src.pipscript.commands.show import ShowCmd
    return ShowCmd(pkt)
