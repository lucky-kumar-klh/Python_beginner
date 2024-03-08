import csv

class Item:
    # Class Attributes
    # This will be same for all instances, So even objects can access it
    pay_rate = 0.8  # The pay rate after 20% discount
    all_items = []

    def __init__(self, item: str, price: float, quantity = 0):  # default value with data types
        # Run Validations on Arguments according to thier defined types
        # assert will raise an error message (given by us), if the condition is not true
        assert price >= 0, f"Price {price} should be greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} should be greater than or equal to zero"
        
        # Instance Attributes
        self.item = item
        self.price = price
        self.quantity = quantity

        # Storing all the items (as objects itself) in a list 'all_items'
        Item.all_items.append(self)
    
    def calculate_total_price(self):
        return f"Total Price: {self.price * self.quantity}"
    
    def apply_discount(self):
        return self.price * self.pay_rate  # OR 
        # return self.price * Item.pay_rate   # Since pay_rate is a class & instance level attribute
    
    @classmethod  # Decorator used to make this method a class method
    def instantiate_from_csv(cls):   # cls = class, self = object: Here, the cls itself is being passed as an argument
        with open("items.csv", 'r') as file:
            reader = csv.DictReader(file)
            items_list = list(reader)

        for i in items_list:
            # print(i)
            # Item(item, price, quantity)
            Item(   # Instantiating object from the csv file
                item = i.get("item"),   # return the value of the key from dictionary
                price = float(i.get("price")),
                quantity = int(i.get("quantity")),
            )

    # staticmethod is also equavalent to writing a function above class (irrespective of class)
    # As, it doesn't have 'self' or 'cls' arguments by default, it's just a regular def
    @staticmethod   # Allows us to use the method without creating an object
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()   # 1, 3.0, 10 are all integers - True, else False
        else:
            return False

    def __repr__(self):
        return f"['{self.item}', '{self.price}', '{self.quantity}']"

class Phone(Item):
    def __init__(self, item: str, price: float, quantity = 0, broken_phone = 0):
        super().__init__(item, price, quantity)
        assert broken_phone >= 0, f"Broken Phone {broken_phone} should be greater than or equal to zero"
        self.broken_phone = broken_phone

# item1 = Item("Laptop", 1000, 1)
# print(item1.pay_rate)

# item2 = Item("iPhone", 1000, 1)
# item2.pay_rate = 0.5    # To have diff value for pay_rate for particular instance
# print(item2.pay_rate)
# print(item1.calculate_total_price())
# print(Item.pay_rate)

# '__dict__' return a dictionary of all the attributes available for the oblject/class
# print(item1.__dict__)  # All the attributes at instance level
# print(Item.__dict__)  # All the attributes at class level
# print(item1.apply_discount())

# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all_items)

# for item in Item.all_items:
#     print(item.item)

Item.instantiate_from_csv()
print(Item.all_items)

print(Item.is_integer(7.0))

phone1 = Phone("Samsung", 3000, 3, 1)

print(Phone.all_items)