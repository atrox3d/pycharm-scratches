class Ten:
    def __get__(self, instance, objtype=None):
        print('returning 10...')
        return 10

class Tenx:
    def __get__(self, instance, objtype=None):
        print('returning 10...')
        return 10

    def __set__(self, instance, value):
        raise AttributeError


class A:
    x = 5
    y = Ten()
    z = Tenx()

a = A()
print(a.x)
print(a.y)

a.y = 6             # no error
print(a.y)          # descriptor is overwritten by 6

print(a.z)
try:
    a.z = 9         # AttributeError
except AttributeError:
    pass
A.z = 9             # no error
print(a.z)          # descriptor is overwritten by 9
