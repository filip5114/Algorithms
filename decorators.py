import time


def time_it(func):
    """Decorator to check method/function execution time"""
    def wrapper(*args, **kwargs):
        t = time.time()
        print(f'{func.__name__} started. {time.ctime()}')
        result = func(*args, **kwargs)
        print(f'Done. Duration: {time.time() - t}')
        return result
    return wrapper
