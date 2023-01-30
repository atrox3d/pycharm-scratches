import zlib
from pathlib import Path

path = Path('~/code/git/udemy/the-complete-git-guide-understand-and-master-git-and-github').expanduser()
path = path / Path('first-project/.git/objects/44')
blobpath = list(path.glob('*'))[0]

with open(blobpath, 'rb') as blobfile:
    blob = blobfile.read()
    print(blob)

x = zlib.decompress(blob)
print(x)

# with open('')
# zlib.
