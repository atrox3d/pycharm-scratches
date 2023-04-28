from dataclasses import dataclass
import datetime

@dataclass
class Transaction:
  sender: str
  receiver: str
  date: str
  amount: float = 0.0

record = Transaction(
    sender='sender', receiver='receiver', date='today'
)
print(f'{record = }')
print(f'{record.sender = }')
