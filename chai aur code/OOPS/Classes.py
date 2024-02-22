class Car:
    # __init__ is a constructor
    def __init__(self, brand, model):
        # Using '__' before attribute makes it private 
        self.__brand = brand  # self.brand => class member
        self.model = model  # self.model => class member

    # getter method
    def get_brand(self):
        return self.__brand
    
    # Polymorphism
    def fuel_type(self):
        return "Petrol or Diseil"

    # Adding feature to this class
    def fullname(self):
        return f"{self.__brand} {self.model}"

my_car = Car("Renault", "Duster")

print(isinstance(my_car, Car))
print(my_car.fullname())
print(my_car.fuel_type())
# print(my_car.__brand)  # Private attrites can't be accessed directly
print(my_car.model)
print(my_car.get_brand())