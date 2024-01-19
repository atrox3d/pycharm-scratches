from dataclasses import dataclass
import datetime

@dataclass
class Transaction:
  sender: str
  receiver: str
  date: str
  amount: float = 0.0


@dataclass
class TransactionWithTimeStamp(Transaction):
    # needs default value because of Transaction,amount
    timestamp: str = datetime.datetime.now().__str__()

record = TransactionWithTimeStamp(
    sender='sender', receiver='receiver', date='today'
)
print(f'{record = }')
print(f'{record.sender = }')
