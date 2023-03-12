# https://realpython.com/inherit-python-list/#inheriting-from-pythons-built-in-list-class

# string_list.py

from collections import UserList


class StringList(UserList):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = str(item)

    def insert(self, index, item):
        self.data.insert(index, str(item))

    def append(self, item):
        self.data.append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(str(item) for item in other)


if __name__ == '__main__':
    data = StringList([1, 2, 2, 4, 5])
    print(data)

    data.append(6)
    print(data)

    data.insert(0, 0)
    print(data)

    data.extend([7, 8, 9])
    print(data)

    data[3] = 3
    print(data)
