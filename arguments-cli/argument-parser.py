import argparse

parser = argparse.ArgumentParser(description='arg parser')
# adding arguments
parser.add_argument(
    # '-o'
    '-offset',
    '--offset',
    metavar='',
    type=str,
    help='offset',
    required=True
)

args = parser.parse_args(["-o", "aaaax"])

print(args)