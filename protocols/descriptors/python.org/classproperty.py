import logging
logger = logging.getLogger(__name__)
# from loggerdecorator import log_decorator

# ENABLE_LOGGER = True
# @log_decorator(
#     __name__,
#     loggermethod='info',
#     indentlevel=1,
#     klass='Property',
#     enable=False
# )

def getparams(*args, exclude=None, **kwargs):
    exclude = exclude or []
    sargs = list(map(str, args))
    skwargs = [f'{name}={value}' for name, value in kwargs.items() if name not in exclude]
    return ', '.join(sargs + skwargs)

class Property:
    """Emulate PyProperty_Type() in Objects/descrobject.c"""

    # @log_decorator(__name__, loggermethod='info', indentlevel=2, klass='Property', enable=ENABLE_LOGGER)
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        logger.info(f'Property | __init__   | {getparams(**locals())}')
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc
        self._name = ''

    # @log_decorator(__name__, loggermethod='info', indentlevel=2, klass='Property', enable=ENABLE_LOGGER)
    def __set_name__(self, owner, name):
        logger.info(f'Property | __setname__ | {getparams(**locals())}')
        self._name = name

    # @log_decorator(__name__, loggermethod='info', indentlevel=2, klass='Property', enable=ENABLE_LOGGER)
    def __get__(self, obj, objtype=None):
        logger.info(f'Property | __get__     | {getparams(**locals())}')
        if obj is None:
            logger.info(f'Property | __get__     | RETURN |  self')
            return self
        if self.fget is None:
            raise AttributeError(f"property '{self._name}' has no getter")
        logger.info(f'Property | __get__     | RETURN |  self.fget({obj=})')
        return self.fget(obj)

    # @log_decorator(__name__, loggermethod='info', indentlevel=2, klass='Property', enable=ENABLE_LOGGER)
    def __set__(self, obj, value):
        logger.info(f'Property | __set__     | {getparams(**locals())}')
        if self.fset is None:
            raise AttributeError(f"property '{self._name}' has no setter")
        logger.info(f'Property | __set__     | self.fset({obj=}, {value=})')
        self.fset(obj, value)

    # @log_decorator(__name__, loggermethod='info', indentlevel=2, klass='Property', enable=ENABLE_LOGGER)
    def __delete__(self, obj):
        logger.info(f'Property | __delete__  | {getparams(**locals())}')
        if self.fdel is None:
            raise AttributeError(f"property '{self._name}' has no deleter")
        self.fdel(obj)

    # @log_decorator(__name__, loggermethod='info', indentlevel=2, klass='Property', enable=ENABLE_LOGGER)
    def getter(self, fget):
        logger.info(f'Property | getter      | {getparams(**locals())}')
        prop = type(self)(fget, self.fset, self.fdel, self.__doc__)
        prop._name = self._name
        logger.info(f'Property | getter      | RETURN |  {prop=}')
        return prop

    # @log_decorator(__name__, loggermethod='info', indentlevel=2, klass='Property', enable=ENABLE_LOGGER)
    def setter(self, fset):
        logger.info(f'Property | setter      | {getparams(**locals())}')
        prop = type(self)(self.fget, fset, self.fdel, self.__doc__)
        prop._name = self._name
        logger.info(f'Property | setter      | RETURN |  {prop=}')
        return prop

    # @log_decorator(__name__, loggermethod='info', indentlevel=2, klass='Property', enable=ENABLE_LOGGER)
    def deleter(self, fdel):
        logger.info(f'Property | deleter     | {getparams(**locals())}')
        prop = type(self)(self.fget, self.fset, fdel, self.__doc__)
        prop._name = self._name
        return prop

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # p = Property()
    class X:
        @Property
        def a(self):
            return 5

        def get5(self):
            return 5

        b = Property(get5)

    x = X()
    # print(x.a)
    # x.b = 5
