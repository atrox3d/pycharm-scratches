from functools import wraps, partial

def debug(func=None, *, prefix=''):
    if func is None:
        # wasn't passed
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

@debug
def no_prefix():
    print('noprefix here')

@debug(prefix='PREFIX')
def prefix():
    print('prefix here')

no_prefix()
prefix()
