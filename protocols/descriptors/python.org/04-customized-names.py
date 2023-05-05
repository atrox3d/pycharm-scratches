import logging

logging.basicConfig(level=logging.INFO)

logging.info('----> declare class LoggedAccess')
class LoggedAccess:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name
        logging.info(f'{self.public_name = }')
        logging.info(f'{self.private_name = }\n')

    def __get__(self, obj, objtype=None):
        logging.info(f'getattr: {self.private_name = }')
        value = getattr(obj, self.private_name)
        logging.info(f'getattr: {value = }')
        logging.info('Accessing %r giving %r\n', self.public_name, value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', self.public_name, value)
        logging.info(f'setattr: {self.private_name = }')
        logging.info(f'setattr: {value = }\n')
        setattr(obj, self.private_name, value)

logging.info('----> declare class Person')
class Person:
    logging.info('----> create name')
    name = LoggedAccess()                # First descriptor instance
    logging.info('----> after create name')

    logging.info('----> create age')
    age = LoggedAccess()                 # Second descriptor instance
    logging.info('----> after create age')

    def __init__(self, name, age):
        logging.info('----> init name')
        self.name = name                 # Calls the first descriptor
        logging.info('----> init age')
        self.age = age                   # Calls the second descriptor

    def birthday(self):
        logging.info('----> increment age')
        self.age += 1


"""
An interactive session shows that the Person class has called __set_name__() 
so that the field names would be recorded. 
Here we call vars() to look up the descriptor without triggering it:
"""
logging.info('----> lookup descriptors')
logging.info(vars(vars(Person)['age']))
logging.info(vars(vars(Person)['name']))
logging.info('\n')
"""
The new class now logs access to both name and age:
"""
logging.info('----> creating Peter P, 10')
pete = Person('Peter P', 10)
logging.info('----> creating Catherine C, 20')
kate = Person('Catherine C', 20)
logging.info('\n')
"""
The two Person instances contain only the private names:
"""
logging.info('----> log vars(person object)')
logging.info(vars(pete))
logging.info(vars(kate))
logging.info('')
"""
just checking, but no autocomplete
"""
logging.info('----> log vars(person object)')
logging.info(f'{pete._name = }')
logging.info(f'{pete._age = }')
logging.info(f'{kate._name = }')
logging.info(f'{kate._age = }')
