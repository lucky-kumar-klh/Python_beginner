
def debug(func):
    pass


@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet("Lucky")