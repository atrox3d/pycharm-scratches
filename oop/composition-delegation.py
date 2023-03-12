# composition

class A:
    a_prop1 = 1
    a_prop2 = 2

    def a_method(self):
        print(f"A| a_method()")


width = 25


class B:
    b_prop1 = 1
    b_prop2 = 2

    def __init__(self, a=None):
        who = '__init__'
        if a and isinstance(a, A):
            print(f"B|{who:>{width}}| assigning self.a")
            self.a = a
        else:
            print(f"B|{who:>{width}}| creating self.a")
            self.a = A()

    def b_method(self):
        print(f"B| b_method()")

    def __getattribute__(self, item):
        """called whenever an attribute is accessed: obj.attr"""
        who = '__getattribute__'
        print(f"B|{who:>{width}}| {item=}| return super().__getattribute__({item})")
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        """called when assigning attr: obj.attr = val"""
        pass
        who = '__setattr__'
        print(f"B|{who:>{width}}| {key=}, {value=}| )")
        return super().__setattr__(key, value)

    def __getattr__(self, item):
        """called when item is not found: val = obj.attr"""
        who = '__getattr__'
        print(f"B|{who:>{width}}| {item=} NOT FOUND")
        print(f"B|{who:>{width}}| delegating {item=} to self.a")
        delegate_item = getattr(self.a, item)
        print(f"B|{who:>{width}}| return {delegate_item=}")
        return delegate_item


if __name__ == '__main__':
    pass

    b = B()
    print("start TEST")
    print(b.a_prop1)
    # print(b.a_prop2)
    # b.a_method()
    #
    # print(b.b_prop1)
    # print(b.b_prop2)
    # b.b_method()
