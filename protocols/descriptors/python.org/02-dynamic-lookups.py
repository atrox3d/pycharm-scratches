import os

class DirectoryLength:

    def __get__(
            self,           # DirectoryLength instance
            obj,            # Directory instance, None if called from class
            objtype=None    # Directory class
        ):
        print(f'__get__({self=}, {obj=}, {objtype=} )')
        return len(os.listdir(obj.dirname))

class Directory:

    len = DirectoryLength()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute

s = Directory('c:/')
print(s.len)

print(Directory.len)
