import logging

logging.basicConfig(level=logging.INFO)

print('-> MAIN: declare class LoggedAccess')
class LoggedAccess:

    def __set_name__(self, owner, name):
        print(f'\tLoggedAccess::__set_name__({self=}, {owner=}, {name=})')
        self.public_name = name
        print(f'\tLoggedAccess::__set_name__: {self.public_name = }')
        self.private_name = '_' + name
        print(f'\tLoggedAccess::__set_name__: {self.private_name = }')
        print(f'-> AFTER LoggedAccess::__set_name__\n')

    def __get__(self, obj, objtype=None):
        print(f'\tLoggedAccess::__get__: getattr: {self.private_name = }')
        value = getattr(obj, self.private_name)
        print(f'\tLoggedAccess::__get__: getattr: {value = }')
        print(f'\tLoggedAccess::__get__: Accessing %r giving %r\n', self.public_name, value)
        print(f'-> AFTER LoggedAccess::__get__\n')
        return value

    def __set__(self, obj, value):
        print(f'\tLoggedAccess::__set__: Updating %r to %r', self.public_name, value)
        print(f'\tLoggedAccess::__set__: setattr: {self.private_name = }')
        print(f'\tLoggedAccess::__set__: setattr: {value = }\n')
        setattr(obj, self.private_name, value)
        print(f'-> AFTER LoggedAccess::__get__\n')
print('-> MAIN: AFTER declare class LoggedAccess\n')


print('-> MAIN: declare class Person')
class Person:
    print('-> Person: create name')
    name = LoggedAccess()                # First descriptor instance
    print('-> Person: AFTER create name\n')

    print('-> Person: create age')
    age = LoggedAccess()                 # Second descriptor instance
    print('-> Person: AFTER create age\n')

    print('-> Person: declare __init__')
    def __init__(self, name, age):
        print('\tPerson: __init__ name')
        self.name = name                 # Calls the first descriptor
        print('\tPerson: __init__ age')
        self.age = age                   # Calls the second descriptor
    print('-> Person: AFTER __init__ \n')

    print('-> Person: declare birthday')
    def birthday(self):
        print('-> Person: birthday: increment age')
        self.age += 1
        print('-> Person: AFTER birthday: increment age')
    print('-> Person: AFTER declare birthday \n')
print('-> MAIN: AFTER declare class Person\n\n')


"""
An interactive session shows that the Person class has called __set_name__() 
so that the field names would be recorded. 
Here we call vars() to look up the descriptor without triggering it:
"""
print('-> MAIN: lookup descriptors')
print(vars(vars(Person)['age']))
print(vars(vars(Person)['name']))
print('-> MAIN: AFTER lookup descriptors\n')
"""
The new class now logs access to both name and age:
"""
print('-> MAIN: creating Peter P, 10')
pete = Person('Peter P', 10)
print('-> MAIN: AFTER creating Peter P, 10\n\n')

print('-> MAIN: creating Catherine C, 20')
kate = Person('Catherine C', 20)
print('-> MAIN: AFTER creating Catherine C, 20\n\n')

"""
The two Person instances contain only the private names:
"""
print('-> MAIN: log vars(person object)')
print(vars(pete))
print(vars(kate))
print('\n')
"""
just checking, but no autocomplete
"""
print('-> MAIN: log vars(person object)')
print(f'{pete._name = }')
print(f'{pete._age = }')
print(f'{kate._name = }')
print(f'{kate._age = }')
