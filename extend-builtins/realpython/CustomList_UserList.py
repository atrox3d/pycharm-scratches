# https://realpython.com/inherit-python-list/#inheriting-from-pythons-built-in-list-class

# custom_list.py

from collections import UserList

class CustomList(UserList):
    def join(self, separator=" "):
        return separator.join(str(item) for item in self)

    def map(self, action):
        return type(self)(action(item) for item in self)

    def filter(self, predicate):
        return type(self)(item for item in self if predicate(item))

    def for_each(self, func):
        for item in self:
            func(item)


if __name__ == '__main__':
    words = CustomList(
        [
            "Hello,",
            "Pythonista!",
            "Welcome",
            "to",
            "Real",
            "Python!"
        ]
    )

    print(words.join())

    print(words.map(str.upper))

    print(words.filter(lambda word: word.startswith("Py")))

    words.for_each(print)
