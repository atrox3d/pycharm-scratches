"""
https://towardsdatascience.com/understand-how-to-use-namedtuple-and-dataclass-in-python-e82e535c3691
"""
import collections


TransactionDefault = collections.namedtuple(
    'TransactionDefault',                   # class name
    'sender amount receiver date',          # field names separated by whitespace
    defaults=['jojo', 'xiaoxu', None, None] # default arguments
)
print()
print(f'{TransactionDefault() = }')

PartialDefault = collections.namedtuple(
    'TransactionDefault',                   # class name
    'sender receiver date amount',          # field names separated by whitespace
    defaults=['second-last', 'last']        # default arguments from the end
)
print(f'{PartialDefault("sender", "receiver") = }')


