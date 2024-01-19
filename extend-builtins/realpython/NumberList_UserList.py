# https://realpython.com/inherit-python-list/#inheriting-from-pythons-built-in-list-class

# number_list.py

from collections import UserList

class NumberList(UserList):
    def __init__(self, iterable):
        super().__init__(self._validate_number(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = self._validate_number(item)

    def insert(self, index, item):
        self.data.insert(index, self._validate_number(item))

    def append(self, item):
        self.data.append(self._validate_number(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(self._validate_number(item) for item in other)

    def _validate_number(self, value):
        if isinstance(value, (int, float, complex)):
            return value
        raise TypeError(
            f"numeric value expected, got {type(value).__name__}"
        )
<<<<<<< HEAD
=======


if __name__ == '__main__':
    numbers = NumberList([1.1, 2, 3j])
    print(numbers)

    try:
        numbers.append("4.2")
    except TypeError as te:
        print(te)

    try:
        numbers.append(4.2)
        print(numbers)
    except TypeError as te:
        print(te)

    try:
        numbers.insert(0, "0")
    except TypeError as te:
        print(te)

    numbers.insert(0, 0)
    print(numbers)

    try:
        numbers.extend(["5.3", "6"])
    except TypeError as te:
        print(te)

    numbers.extend([5.3, 6])
    print(numbers)
>>>>>>> 4d6ca05982cde937099bc6474b5ded44ef05898e
