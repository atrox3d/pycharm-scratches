# https://towardsdatascience.com/python-tricks-inheriting-from-built-in-data-types-f6cbeb8d88a5

# Create a list that can only accept integers and floats

class CustomIntFloatError(Exception):
    def __init__(self, if_obj, element):
        self.IF_obj = if_obj
        self.element = element

    def __str__(self):
        return repr(self.element) + ' is not an integer or a float'


class IntFloatList(list):
    def append(self, element):
        if not isinstance(element, (int, float)):
            raise CustomIntFloatError(self, element)
        return list.append(self, element)


ifl = IntFloatList()
print(ifl)
ifl.append(1.5)
print(ifl)
ifl.append(1)
print(ifl)
# ifl.append('1')
# print(ifl)


class MyDictError(Exception):
    def __init__(self, my_dicy_obj, key, value):
        self.my_dict_obj = my_dicy_obj
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value) + ' cannot be added. \nValue has to be an integer less than 50'


class MyDict(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, int) or value > 50:
            raise MyDictError(self, key, value)
        return dict.__setitem__(self, key, value)


my_dict_object = MyDict([('a', 1), ('b', 2)])
my_dict_object = MyDict(a=1, b=2, c='x')
print(my_dict_object)
