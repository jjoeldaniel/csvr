from enum import Enum


class ArgumentType(Enum):
    STRING = str
    INTEGER = int


class Argument:
    def __init__(
        self,
        name: str,
        description: str,
        dest: str,
        short: str | None = None,
        nargs: int | str = "?",
        type: ArgumentType = ArgumentType.STRING,
        help: str = "",
        required: bool = False,
        action: str = "store",
        default: str | int | tuple[int, ...] | bool | None = None,
        opt: dict[map, map] | None = None,
    ):
        self.name = name
        self.description = description
        self.dest = dest
        self.short = shorten(name) if short is None else short
        self.nargs = nargs
        self.type = type
        self.help = help
        self.required = required
        self.action = action
        self.default = (default,)
        self.opt = opt


def shorten(name: str) -> str:
    return "-" + name[2:][0]
