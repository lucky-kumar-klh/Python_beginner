def debug(func):
    def wrapper(*args, **kwargs):
        # .join gives a iteratable 
        args_values = ', '.join(str(arg) for arg in args)
        kwargs_values = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"Function {func.__name__} with args {args_values} and {kwargs_values}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting = "Hi"):
    print(F"{greeting}, {name}")

greet("Lucky", "Namaste")