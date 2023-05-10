from helpers.params import print_params
from .property_access import PropertyAccess

CLS = 'AttributeAccess'.upper()

print(f'{CLS:>25} | BEGIN class definition')
class AttributeAccess:
    def __getattribute__(self, item):
        """
        gets obj.attr
        """
        print_params()
        return super().__getattribute__(item)

    def __getattr__(self, item):
        """
        gets obj.attr if __getattribute__ does not find attr
        """
        print_params()
        return None

    def __setattr__(self, key, value):
        """
        sets obj.attr = value
        """
        print_params()
        return super().__setattr__(key, value)

    def __getitem__(self, item):
        """
        gets obj[key]
        raises KeyError
        """
        print_params()
        return self.__dict__[item]

    def __setitem__(self, key, value):
        """
        sets obj[key] = value
        """
        print_params()
        self.__dict__[key] = value

    print(f'{CLS:>25} | DECLARE prop = PropertyAccess() ...')
    prop = PropertyAccess()
print(f'{CLS:>25} | END class definition')
print()
