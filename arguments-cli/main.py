import sys
import argparse

from . import testparse
from . import sumormax
from . import subcommands

parsers = dict(
    testparse=testparse,
    sumormax=sumormax,
    subcommands=subcommands
)


mainparser = argparse.ArgumentParser(
    description="choose which parser use",
    epilog="choose your parser"
)
mainparser.add_argument("parser", choices=parsers.keys())
args, unknownargs = mainparser.parse_known_args()
print(f"{args=}, {unknownargs=}")

sys.argv.pop(0)
parsers[args.parser].parse()

# testparse.parse()
# sumormax.parse()


