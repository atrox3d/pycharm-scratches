import argparse


def parse():
    parser = argparse.ArgumentParser(
        description="sum or max"
    )

    parser.add_argument(
        "integers",
        # metavar='N',
        type=int,
        nargs='+',
        help="an integer for the accumulator"
    )

    parser.add_argument(
        "--sum",
        dest="accumulate",
        action="store_const",
        const=sum,
        default=max
    )

    # parser.print_help()
    args = parser.parse_args()
    print(f"{args=}")
    print(args.accumulate(args.integers))
