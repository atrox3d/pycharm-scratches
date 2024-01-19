import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s | %(name)-15.15s | %(message)s')
logger = logging.getLogger(__name__)
# print(logging.getLogger().handlers[0].formatter._fmt)

from loggerdecorator import log_decorator

logger.info('********** MAIN ************ | BEGIN | import Property')
from classproperty import Property, getparams
logger.info('********** MAIN ************ | END   | import Property\n\n')

ENABLE_LOGGER = False

# @log_decorator(__name__, loggermethod='info', indentlevel=3, klass='TestProp', enable=ENABLE_LOGGER)
logger.info('********** MAIN ************ | BEGIN | declare TestProp\n')
class TestProp:

    # @log_decorator(__name__, loggermethod='info', indentlevel=4, klass='TestProp', enable=ENABLE_LOGGER)
    logger.info(f'TestProp | BEGIN | declare __init__')
    def __init__(self):
        logger.info(f'TestProp | BEGIN | __init__    | {getparams(**locals())}\n')
        self.x = 0
        logger.info(f'TestProp | END   | __init__')
    logger.info(f'TestProp | END   | declare __init__')

    logger.info(f'TestProp | BEGIN | declare @Property\n')
    @Property
    # @log_decorator(__name__, loggermethod='info', indentlevel=4, klass='TestProp', enable=ENABLE_LOGGER)
    def x(self):
        logger.info(f'TestProp | x.getter    | {getparams(**locals())}\n')
        return 'this is x'
    logger.info(f'TestProp | END   | declare @Property\n')

    logger.info(f'TestProp | BEGIN | declare @Property.setter\n')
    @x.setter
    # @log_decorator(__name__, loggermethod='info', indentlevel=4, klass='TestProp', enable=ENABLE_LOGGER)
    def x(self, value):
        logger.info(f'TestProp | x.setter    | {getparams(**locals())}')
        self.__x = 0
    logger.info(f'\nTestProp | END   | declare @Property.setter\n')
logger.info('\n********** MAIN ************ | END   | declare TestProp\n')


logger.info('\n\n********** MAIN ************ CREATING tp\n\n')
tp = TestProp()

logger.info('\n\n********** MAIN ************ ASSIGN x \n\n')
tp.x = 1
logger.info('\n\n********** MAIN ************ PRINT x \n\n')
print(tp.x)

