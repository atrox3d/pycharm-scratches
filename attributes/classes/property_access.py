from helpers.params import print_params

CLS = 'PropertyAccess'.upper()
INDENT = 4
SPACES = INDENT * ' '

print(f'{CLS:>25} | {SPACES}BEGIN class definition')
class PropertyAccess:
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

    def __set_name__(self, owner, name):
        """
        sets property name
        """
        print_params()

    def __set__(self, instance, value):
        """
        sets property value
        """
        print_params()
        self.value = value

    def __get__(self, instance, owner):
        """
        not used
        """
        print_params()
        return self.value
print(f'{CLS:>25} | {SPACES}END class definition')
print()
