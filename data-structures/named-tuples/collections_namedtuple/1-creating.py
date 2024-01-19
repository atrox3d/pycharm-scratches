"""
https://towardsdatascience.com/understand-how-to-use-namedtuple-and-dataclass-in-python-e82e535c3691
"""
import collections

Transaction = collections.namedtuple(
    'Transaction',                          # class name
    ['sender','amount','receiver','date']   # field names as list
)

Transaction = collections.namedtuple(
    'Transaction',                          # class name
    'sender amount receiver date'           # field names separated by whitespace
)

recordnamed = Transaction(                  # create obj with named args
    sender="jojo",
    receiver="xiaoxu",
    date="2020-06-08",
    amount=1.0
)
print(f'{recordnamed = }')
print(f'{recordnamed.receiver = }')

recordpositional = Transaction(             # create obj with positional args
    "jojo", 1.0, "xiaoxu", "2020-06-08"
)
print()
print(f'{recordpositional = }')
print(f'{recordpositional.receiver = }')

assert recordnamed == recordpositional      # same values
