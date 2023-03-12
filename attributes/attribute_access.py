class Memo:
    def __setattr__(self, key, value):
        print(f"__setattr__({key=}, {value=})")
        return super().__setattr__(key, value)

    def __setitem__(self, key, value):
        print(f"__setitem__({key=}, {value=})")
        # vars(self)[key] = value
        self.__dict__[key] = value

    def __getitem__(self, item):
        print(f"__getitem__({item=})")
        # return vars(self)[item]
        return self.__dict__[item]


if __name__ == '__main__':
    m = Memo()
    print("m.x = 0")
    m.x = 0
    print(m.__dict__)

    print('m["x"] = 1')
    m["x"] = 1
    print(f"{m['x']=}")
    print(m.__dict__)
