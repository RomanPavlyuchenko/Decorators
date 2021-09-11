import datetime


def logger(function):
    def new_function(*args, **kwargs):
        date_time = datetime.datetime.now()
        result = function(*args, **kwargs)
        with open('logs.txt', 'a') as log:
            log.write(f'{date_time} - {function.__name__} - {args}, {kwargs} - {result}\n')
        return result

    return new_function


def logger_filename(filename='logs.txt'):
    def _logger(function):
        def new_function(*args, **kwargs):
            date_time = datetime.datetime.now()
            result = function(*args, **kwargs)
            with open(filename, 'a') as log:
                log.write(f'{date_time} - {function.__name__} - {args}, {kwargs} - {result}\n')
            return result

        return new_function

    return _logger
