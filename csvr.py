import argparse
from argument import Argument
from util import convert_key

parser = argparse.ArgumentParser(description="Lightweight Python3 based CSV reader")

required_args = parser.add_argument_group("required arguments")
optional_args = parser.add_argument_group("optional arguments")

arguments: list[Argument] = [
    Argument(
        name="--file",
        description="Path to CSV file",
        dest="file",
        nargs="+",
        required=True,
    ),
    Argument(
        name="--reverse",
        description="Reverse order of CSV file",
        dest="reverse",
        default=False,
        action="store_true",
    ),
    Argument(
        name="--key",
        description="Key to sort CSV file by",
        dest="key",
        default=1,
    ),
    Argument(
        name="--field-seperator",
        short="-t",
        dest="delimiter",
        description="Delimiter used in CSV file",
        default=",",
    ),
]

for argument in arguments:
    parser.add_argument(
        argument.name,
        argument.short,
        nargs=argument.nargs,
        dest=argument.dest,
        action=argument.action,
        type=argument.type.value,
        help=argument.description,
        default=argument.default,
    )


args = parser.parse_args()

file: str = args.file[0]
reverse: bool = args.reverse
key: int | tuple[int, ...] = convert_key(args.key)
delimiter: str = args.delimiter

print(f"file: {file}")
print(f"reverse: {reverse}")
print(f"key: {key}")
print(f"delimiter: {delimiter}")
