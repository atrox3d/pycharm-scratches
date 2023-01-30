class A:
    d = dict()

    def __getattr__(self, item):
        print(f"__getattr__({item})")
        return getattr(self.d, item)

    def __getitem__(self, item):
        print(f"__getitem__({item})")
        return self.d.get(item)

    def __setitem__(self, key, value):
        print(f"__setitem__({key}, {value})")
        # self.d.update(dict([(key, value)]))
        self.d.update({key: value})


a = A()

print(a[1])
a[2] = "two"
print(a[2])
print(a.items())

