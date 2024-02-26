import math

class Basic_Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return f"{self.a} + {self.b} = {self.a + self.b}"
    
    def subtract(self):
        return f"{self.a} - {self.b} = {self.a - self.b}"
    
    def multiply(self):
        return f"{self.a} x {self.b} = {self.a * self.b}"
    
    def divide(self):
        if self.b == 0:
            print("Division by 0 Not Possible")
        else:
            return f"{self.a} / {self.b} = {self.a / self.b}"
        
Scientific_Operators = ['!', 'nCr', 'nPr', 'log', 'exponent']
        
class Scientific_Calc(Basic_Calc):
    def __init__(self, a, b, operator):
        super().__init__(a, b)
