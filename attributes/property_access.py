CLS = 'PropertyAccess'.upper()


print(f'{CLS:>20} | BEGIN class definition')
class PropertyAccess:
    def __getattribute__(self, item):
        """
        gets obj.attr
        """
        print(f'{CLS:>20} | __getattribute__(self, {item=})')
        return super().__getattribute__(item)

    def __getattr__(self, item):
        """
        gets obj.attr if __getattribute__ does not find attr
        """
        print(f'{CLS:>20} | __getattr__(self, {item=})')
        print(f'{CLS:>20} | __getattr__: returning None')
        return None

    def __setattr__(self, key, value):
        """
        sets obj.attr = value
        """
        print(f'{CLS:>20} | __setattr__({key=}, {value=})')
        return super().__setattr__(key, value)

    def __getitem__(self, item):
        """
        gets obj[key]
        raises KeyError
        """
        print(f'{CLS:>20} | __getitem__({item=})')
        # return vars(self)[item]
        return self.__dict__[item]

    def __setitem__(self, key, value):
        """
        sets obj[key] = value
        """
        print(f'{CLS:>20} | __setitem__({key=}, {value=})')
        # vars(self)[key] = value
        self.__dict__[key] = value

    def __set_name__(self, owner, name):
        """
        sets property name
        """
        print(f'{CLS:>20} | __set_name__({owner=}, {name=})')
        # self.name = name

    def __set__(self, instance, value):
        """
        not used
        """
        print(f'{CLS:>20} | __set__({instance=}, {value=})')
        self.value = value

    def __get__(self, instance, owner):
        """
        not used
        """
        print(f'{CLS:>20} | __get__({instance=}, {owner=})')
        return self.value
print(f'{CLS:>20} | END class definition')
print()
