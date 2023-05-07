def printer(
        klass=None,
        module='',
        main='MAIN',
        headerformat='{mname:>20} | ',
        functionformat='{mname:>20} | {cname}.{fname}',
):
    """
    adds arguments to decorator
    """
    def decorator(func):
        """
        decorates method/function
        """
        def wrapper(*args, **kwargs):
            """
            wraps function/method
            """
            fname = func.__name__
            cname = klass and (isinstance(klass, type) and f'{klass.__name__}' or f'{klass}') or ''
            mname = (main and module == '__main__') and main or module
            fheader = functionformat.format(mname=mname, cname=cname, fname=fname)
            header = headerformat.format(mname=mname)
            print(f'{fheader}(')
            for arg in args:
                print(f'{header}    {arg},')
            for k, v in kwargs.items():
                print(f'{header}    {k}={v},')
            print(f'{header})')
            value = func(*args, **kwargs)
            return value
        # end wrapper
        return wrapper
    # end decorator
    return decorator
# end parametric

if __name__ == '__main__':

    @printer('str')
    def test(a, b='b', **kwargs):
        pass

    test(1, b='b', extra='extra')
