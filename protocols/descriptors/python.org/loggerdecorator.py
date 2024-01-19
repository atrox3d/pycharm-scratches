import logging

def log_decorator(
        loggername,
        klass=None,
        loggermethod='info',
        indentlevel=0,
        indentchar='\t',
        enable=True
):
    """

    :param loggername:
    :param loggermethod:
    :return:
    """
    def log_this(function):
        logger = logging.getLogger(loggername)      # get logger instance
        log = getattr(logger, loggermethod)         # get logger method by name
        def wrapper(*args,**kwargs):
            if enable:
                # log(f"{tab * indent}BEGIN | {function.__name__} - {args} - {kwargs}")
                if klass:
                    fname = f'{klass}.{function.__name__}'
                else:
                    fname = function.__name__
                params = ', '.join(map(str, args))
                kwparams = ', '.join([f'{key}={value}' for key, value in kwargs.items()])
                indent = indentchar * indentlevel
                log(f"{indent}BEGIN | {fname}")
                log(f"{indent}ARGS  | {params}")
                log(f"{indent}KWARGS| {kwparams}")

            output = function(*args,**kwargs)

            if enable:
                # log(f"{tab * indent}END   | {function.__name__} returned: {output}")
                log(f"{indent}END   | {fname}")
            return output
        return wrapper
    return log_this

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # info = getattr(logger, 'info')
    # info = logger.info
    # print(info)
    # info('hello')

    @log_decorator(__name__, loggermethod='info', indentlevel=1)
    def test(*args, **kwargs):
        pass
    #
    #   OR
    #
    # param_decorator = log_decorator(__name__, 'debug')
    # test = param_decorator(test)

    test(1, 2, 3, name='name', color='blue')

