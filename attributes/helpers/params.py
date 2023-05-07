import inspect

def process_stack(upby=2):
    finfo = inspect.stack()[upby]
    frame = finfo.frame
    function = finfo.function
    arginfo = inspect.getargvalues(frame)

    classname = ''
    try:
        if arginfo.args[0] == 'self':
            self = arginfo.locals['self']
            try:
                getattr(self, function)
                classname = self.__class__.__name__
            except AttributeError:
                pass
    except IndexError:
        pass

    modulename = inspect.getmodule(frame).__name__
    del frame, finfo

    return modulename, classname, function, arginfo

def format_header(modulename, classname, spaces=''):
    header = f'{modulename} | {classname and f"{classname} | "}{spaces}'
    return header

def print_params():
    """
    """
    modulename, classname, function, arginfo = process_stack()
    header = format_header(modulename, classname)

    print(f'{header}{classname and f"{classname}." or classname}{function}(')
    for arg in arginfo.args:
        print(f'{header}    {arg}={arginfo.locals[arg]!r},')
    for vararg in arginfo.varargs and arginfo.locals[arginfo.varargs] or []:
        print(f'{header}    {vararg!r},')
    for name, value in arginfo.keywords and arginfo.locals[arginfo.keywords].items() or []:
        print(f'{header}    {name}={value!r}')
    print(f'{header} )')


if __name__ == '__main__':
    class Testing:
        def m_test_all(self, a, *args, b='b', **kwargs):
            print_params()

        def m_test_none(self):
            print_params()

    def test_all(a, *args, b='b', **kwargs):
        print_params()

    def test_none():
        print_params()

    t = Testing()
    t.m_test_all('a', 2, 3, 4, b='b', extra='extra')
    t.m_test_all('a')
    t.m_test_none()

    test_all('a', 2, 3, 4, b='b', extra='extra')
    test_all('a')
    test_none()

    print_params()
