# The name of the input function in a Decorator can be anything
def login(function):
    '''
    This modified function should recieve arguments that were initially passed  
    in the original function. In this situation, it's function
    Hence, we use *args (proffesionally), Although we can use 
    the default paraters also like (a, b) in line 24
    '''
    def decorate_function(*args):

        print("Login Successful !\n",)
        # This is our original function that has all those arguments, that 
        # were passed initially 
        function(*args)
        print("Thank You for your time",)

    return decorate_function

# Decorator is a function that modifies / decorates
# the input function and returns the modified / decorated function

@login
def learn(a, b):
    print("Learn Something Useful")
    print(f"Sum of {a} and {b} is", a+b)
    print()


#----------------------------------------------------------------------------------

learn(2, 3)