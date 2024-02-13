def print_kwargs(name, power):
    print("Name:", name, " Power:", power)


# Named Arguments will pass according to the function parameters -> order dosen't matters
print_kwargs(name = "Lucky", power = "Silent Killer")
print_kwargs(power = "Silent Killer", name = "Lucky") 

# But for custom arguments like
# print_kwargs(name = "shaktiman", power = "laser", enemy = "Jackol")

# **kwargs accepts key & value like pairs
def use_kwargs(**kwargs):
    for key, val in kwargs.items():
        print(key, ":", val)

use_kwargs(name = "shaktiman", power = "laser", enemy = "Jackol")
print_kwargs(name = "Lucky", power = "Silent Killer")