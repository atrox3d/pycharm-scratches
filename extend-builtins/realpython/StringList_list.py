# https://realpython.com/inherit-python-list/#inheriting-from-pythons-built-in-list-class

# string_list.py

class StringList(list):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, str(item))

    def insert(self, index, item):
        super().insert(index, str(item))

    def append(self, item):
        super().append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(str(item) for item in other)
<<<<<<< HEAD
=======


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
>>>>>>> 4d6ca05982cde937099bc6474b5ded44ef05898e
