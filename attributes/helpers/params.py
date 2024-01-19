import inspect

def process_stack(upby=2):
    finfo = inspect.stack()[upby]
    frame = finfo.frame
    function = finfo.function
    arginfo = inspect.getargvalues(frame)

    classname = ''
    try:
        first_param = arginfo.args[0]
        if first_param in ['self', 'cls']:
            self_or_cls = arginfo.locals[first_param]
            try:
                # getattr(self_or_cls, function)
                if first_param == 'self':
                    #
                    # fix recursion
                    #
                    # classname = self_or_cls.__class__.__name__
                    klass = object.__getattribute__(self_or_cls, '__class__')
                    classname = object.__getattribute__(klass, '__name__')
                else:
                    #
                    # fix recursion
                    #
                    # classname = self_or_cls.__name__
                    classname = object.__getattribute__(self_or_cls, '__name__')
            except AttributeError:
                pass
    except IndexError:
        pass

    modulename = inspect.getmodule(frame).__name__
    del frame, finfo
    return modulename, classname, function, arginfo

def format_header(modulename, classname, spaces='', header_format:str=None):
    if header_format:
        header = header_format.format(modulename=modulename, classname=classname, spaces=spaces)
    else:
        if classname:
            header = f'{classname.upper():>25} | {spaces}'
        else:
            header = f'{modulename.upper():25} | {spaces}'
    return header

def print_params(log=print, spaces='', header_format=None):
    """
    """
    modulename, classname, function, arginfo = process_stack()
    header = format_header(modulename, classname, spaces=spaces, header_format=header_format)

    # print function/method name with open (
    log(f'{header}{classname and f"{classname}." or classname}{function}(')
    # print all positional arguments
    for arg in arginfo.args:
        log(f'{header}    {arg}={arginfo.locals[arg]!r},')
    # print all *args
    for vararg in arginfo.varargs and arginfo.locals[arginfo.varargs] or []:
        log(f'{header}    {vararg!r},')
    # print all **kwargs
    for name, value in arginfo.keywords and arginfo.locals[arginfo.keywords].items() or []:
        log(f'{header}    {name}={value!r}')
    # print closing (
    log(f'{header} )')


if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info('test')

    class Testing:
        def m_test_all(self, a, *args, b='b', **kwargs):
            print_params(log=logging.info)

        def m_test_none(self):
            print_params()

        @classmethod
        def test_classmethod(cls, *args, **kwargs):
            print_params()

        @staticmethod
        def test_static_method( *args, **kwargs):
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

    Testing.test_classmethod(1, extra='extra')
    Testing.test_static_method(1, extra='extra')
    print_params()
