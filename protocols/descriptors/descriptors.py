class VerboseAttribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

class Foo:
    attribute1 = VerboseAttribute()

foo = Foo()
x = foo.attribute1
print(x)
foo.attribute1 = 10
