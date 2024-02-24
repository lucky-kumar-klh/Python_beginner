import time

def timer(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        end = time.time()
        # __name__ is used to determine the current running module
        # here inside wrapper module, example module will be current running module
        # Therefore, func.__name__ = example
        print(f"function {func.__name__} ran in {end-start} seconds")
        return result
    return wrapper

@timer
def example(sec):
    time.sleep(sec)

example(3)