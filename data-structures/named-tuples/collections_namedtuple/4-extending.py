import collections
import datetime


Transaction = collections.namedtuple(
    'Transaction',                          # class name
    'sender receiver date amount'           # field names separated by whitespace
)

class TransactionWithTimeStamp(Transaction):
    @property
    def timestamp(self):
        return datetime.datetime.now()
    
    def __repr__(self):
        # return 'xxx' + super().__repr__()
        # return f"TransactionWithTimestamp: {self.timestamp}, {self.date}"
        repr = super().__repr__()
        timestamp =  str(self.timestamp)
        return ', '.join( [f'{repr.rstrip(")")}', f'{timestamp=}'])

record = TransactionWithTimeStamp(
    sender="jojo", receiver="xiaoxu", date="2020-06-08", amount=1.0
)

print(f'{record = }')
