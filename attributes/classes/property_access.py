from helpers.params import print_params

CLS = 'PropertyAccess'.upper()
INDENT = 4
SPACES = INDENT * ' '

print(f'{CLS:>20} | {SPACES}BEGIN class definition')
class PropertyAccess:
    def __getattribute__(self, item):
        """
        gets obj.attr
        """
        print_params()
        exit()

        print(f'{CLS:>20} | {SPACES}__getattribute__(')
        print(f'{CLS:>20} | {SPACES}       {self = },')
        print(f'{CLS:>20} | {SPACES}       {item=}')
        print(f'{CLS:>20} | {SPACES})')
        return super().__getattribute__(item)

    def __getattr__(self, item):
        """
        gets obj.attr if __getattribute__ does not find attr
        """
        print(f'{CLS:>20} | {SPACES}__getattr__(self, {item=})')
        print(f'{CLS:>20} | {SPACES}__getattr__: returning None')
        return None

    def __setattr__(self, key, value):
        """
        sets obj.attr = value
        """
        print(f'{CLS:>20} | {SPACES}__setattr__({key=}, {value=})')
        return super().__setattr__(key, value)

    def __getitem__(self, item):
        """
        gets obj[key]
        raises KeyError
        """
        print(f'{CLS:>20} | {SPACES}__getitem__({item=})')
        # return vars(self)[item]
        return self.__dict__[item]

    def __setitem__(self, key, value):
        """
        sets obj[key] = value
        """
        print(f'{CLS:>20} | {SPACES}__setitem__({key=}, {value=})')
        # vars(self)[key] = value
        self.__dict__[key] = value

    def __set_name__(self, owner, name):
        """
        sets property name
        """
        print(f'{CLS:>20} | {SPACES}__set_name__({owner=}, {name=})')
        # self.name = name

    def __set__(self, instance, value):
        """
        not used
        """
        print(f'{CLS:>20} | {SPACES}__set__({instance=}, {value=})')
        self.value = value

    def __get__(self, instance, owner):
        """
        not used
        """
        print(f'{CLS:>20} | {SPACES}__get__({instance=}, {owner=})')
        return self.value
print(f'{CLS:>20} | {SPACES}END class definition')
print()
