import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            print("Value Taken from cache")
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        print("New Entry")
        return result
    return wrapper 


@cache
def long_running_func(a, b):
    time.sleep(4)
    return a + b

print(long_running_func(2, 3))
print(long_running_func(2, 3))
print(long_running_func(1, 9))
