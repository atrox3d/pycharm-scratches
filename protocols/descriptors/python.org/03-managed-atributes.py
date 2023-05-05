import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class Person:

    age = LoggedAgeAccess()             # Descriptor instance

    def __init__(self, name, age):
        self.name = name                # Regular instance attribute
        self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1                   # Calls both __get__() and __set__()


logging.info('creating Mary M, 30')
mary = Person('Mary M', 30)             # The initial age update is logged
logging.info('creating David D, 40')
dave = Person('David D', 40)

logging.info(vars(mary))                # The actual data is in a private attribute
logging.info(vars(dave))

logging.info(mary.age)                  # Access the data and log the lookup
logging.info('mary.birthday()')           # Updates are logged as well
mary.birthday()

logging.info(dave.name)                   # Regular attribute lookup isn't logged
logging.info(dave.age)                   # Only the managed attribute is logged
