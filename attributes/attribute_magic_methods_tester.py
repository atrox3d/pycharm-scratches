class Tester:
    def __init__(self):
        super(Tester, self).__init__()
        self.prop = 1
        self.innerdict = dict()

    def __setattr__(self, key, value):
        print(f"__setattr__({key=}, {value=})")
        return super(Tester, self).__setattr__(key, value)

    def __getattr__(self, item):
        print(f"__getattr__({item=})")
        return f"{item} NOT FOUND"

    def __getattribute__(self, item):
        print(f"__getattribute__({item=})")
        return super(Tester, self).__getattribute__(item)

    def __setitem__(self, key, value):
        print(f"__setitem__({key=}, {value=})")
        return self.innerdict.__setitem__(key, value)

    def __getitem__(self, item):
        print(f"__getitem__({item=})")
        return self.innerdict.__getitem__(item)
        # return super(Tester, self).__getitem__(item)


class Empty: pass


t = Tester()
t.prop
print(t.x)
t[1] = 2
print(t[1])
print(t.__dict__)
print(Tester.__dict__)

e = Empty()
print(e.__dict__)
print(Empty.__dict__)



