import argparse
import sys


def get_parser():
    # create parser
    parser = argparse.ArgumentParser(
        description="test parser"
    )

    # mandatory positional argument, stores the value into positional1
    parser.add_argument('positional1')

    # optional positional argument, stores the value into positional2
    # default = []
    parser.add_argument('positional2', nargs='*')

    # expects argument
    # default = None
    parser.add_argument('-o', '--option')

    # stores 42 into  storeconst, if specified, otherwise None
    # default = None
    parser.add_argument('-c', '--storeconst',
                        action='store_const',
                        const=42
                        )

    # stores True into storetrue, if specified, otherwise False
    # default = False
    parser.add_argument('-t', '--storetrue',
                        action='store_true'
                        )

    # stores False into storefalse, if specified, otherwise True
    # default = True
    parser.add_argument('-f', '--storefalse',
                        action='store_false'
                        )

    # appends the parameter into the list append everytime it is specified
    # default = None
    parser.add_argument('-a', '--append',
                        action='append'
                        )

    # appends the value of const to the list appendconst everytime it is specified
    # default = None
    parser.add_argument('-A', '--appendconst',
                        action='append_const',
                        const="const"
                        )

    # counts the repetitions of C or --count into count
    # default = 0
    parser.add_argument('-C', '--count',
                        action='count',
                        default=0
                        )

    # show program's version number and exit
    parser.add_argument('-v', '--version',
                        action='version',
                        version="1.0"
                        )
    # appends one or more values to extend
    # default = None
    parser.add_argument('-e', '--extend',
                        # dest='array',
                        action='extend',
                        nargs='+',
                        type=int,
                        default=[]
                        )

    return parser


def parse():
    return parser.parse_args()


def set_argv():
    sys.argv.append('positional_one')
    sys.argv.append('positional_two')
    sys.argv.append('-o')
    sys.argv.append('5')
    sys.argv.append('--option')
    sys.argv.append('6')
    sys.argv.append('-c')
    sys.argv.append('-t')
    sys.argv.append('--storetrue')
    sys.argv.append('-f')
    sys.argv.append('--storefalse')
    sys.argv.append('-a')
    sys.argv.append('item')
    sys.argv.append('--append')
    sys.argv.append('item')
    sys.argv.append('-A')
    sys.argv.append('--appendconst')
    sys.argv.append('-C')
    sys.argv.append('--count')
    sys.argv.append('-e1')
    sys.argv.append('--extend')
    sys.argv.append('2')


if __name__ == '__main__':
    parser = get_parser()

    set_argv()

    params = [
        'positional1',              # mandatory positional1 = 'positional1'

        'optional1',                # optional positional2 = ['optional1', 'optional2']
        'optional2',

        '-o1',                      # option = '1'
        '--option=2',               # option = '2'
        '--option',                 # option = '3'
        '3',

        '-c',                       # storeconst = 42
        '--storeconst',             # storeconst = 42

        '-t',                       # storetrue = True
        '--storetrue',              # storetrue = True

        '-f',                       # storefalse = False
        '--storefalse',             # storefalse = False

        '-a1',                      # append = ['1', '2', '3']
        '--append=2',
        '--append',
        '3',

        '-A',                       # appendconst = ['const', 'const']
        '--appendconst',

        '-C',                       # count = 1
        '--count',                  # count = 2

        '-e1',                      # extend = ['1']
        '--extend=2',               # extend = ['1', '2']
        '--extend',                 # extend = ['1', '2', '3']
        '3',
        '4',                        # extend = ['1', '2', '3', '4']
        '5'                         # extend = ['1', '2', '3', '4', '5']
    ]
    args: argparse.Namespace = parser.parse_args(params)

    # for x, y in args.__dict__.items():
    #     print(x, y)
    for k, v in vars(args).items():
        print(f'{k} = {v}')
