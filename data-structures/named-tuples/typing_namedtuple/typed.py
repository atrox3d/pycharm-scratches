from typing import NamedTuple, Any

class Transaction(NamedTuple):
  sender: str
  receiver: str
  date: str
  amount: float

record = Transaction(
    sender="jojo", receiver="xiaoxu", date="2020-06-08", amount=1.0
)
print(f'{record = }')
print(f'{record.sender = }')            # autocompletion works

class GenericTransaction(NamedTuple):
  sender: Any
  receiver: Any
  date: Any
  amount: Any

record = Transaction(
    sender="jojo", receiver="xiaoxu", date="2020-06-08", amount=1.0
)
print()
print(f'{record = }')
print(f'{record.receiver = }')            # autocompletion works

class DefaultTransaction(NamedTuple):
  sender: str = None
  receiver: str = None
  date: str = None
  amount: float = 0.0

record = DefaultTransaction()
print()
print(f'{record = }')
print(f'{record.receiver = }')            # autocompletion works





