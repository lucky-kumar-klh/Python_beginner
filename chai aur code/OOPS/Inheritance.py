from Classes import Car

class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    # Polymorphism : Same method is used in different classes
    def fuel_type(self):
        return "Electric Fuel"


my_electric_car = Electric_car("Tesla", "Model S", "100 KWH")
print(my_electric_car.fullname())
print(my_electric_car.fuel_type())
print(my_electric_car.battery_size)