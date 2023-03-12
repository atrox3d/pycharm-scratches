import argparse


class ListAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        print("list of commands:")



def parse():
    parser = argparse.ArgumentParser(
        description="main parser"
    )
    parser.add_argument('-l', '--list', action=ListAction, nargs=0)

    git = parser.add_subparsers(help="git help")
    commit = git.add_parser("commit", help="git commit help")
    commit.add_argument("-m", "--message", dest="commit_message")
    commit.add_argument("-A", '--all', dest="commit_all", action="store_true")
    print(commit)

    args = parser.parse_args()
    print(f"{args=}")
