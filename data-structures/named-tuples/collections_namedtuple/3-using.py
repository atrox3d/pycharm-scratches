"""
https://towardsdatascience.com/understand-how-to-use-namedtuple-and-dataclass-in-python-e82e535c3691
"""
import collections


Transaction = collections.namedtuple(
    'Transaction',                          # class name
    'sender receiver date amount'           # field names separated by whitespace
)
record = Transaction(sender="jojo",receiver="xiaoxu",date="2020-06-08",amount=1.0)
print()
print(f'{record.receiver = }')              # use field name
print(f'{record[1] = }')                    # use tuple field index
sender, receiver, date, amount = record     # unpack as a tuple
print(f'{record.receiver = }')
