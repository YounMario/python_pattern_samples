class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls
                                ).__new__(cls, *args, **kwargs)
        return cls._logger

    def print_log(self):
        print str(self.__class__) + " logging.."


loger = Logger()
aLoger = Logger()

print str(loger == aLoger)

print aLoger.__hash__()
print loger.__hash__()
