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

        # Storing all the items in a list 'all_items'
        Item.all_items.append(self)
    
    def calculate_total_price(self):
        return f"Total Price: {self.price * self.quantity}"
    
    def apply_discount(self):
        return self.price * self.pay_rate  # OR 
        # return self.price * Item.pay_rate   # Since pay_rate is a class & instance level attribute
    
    def __repr__(self):
        return f"['{self.item}', '{self.price}', '{self.quantity}']"


item1 = Item("Laptop", 1000, 1)
print(item1.pay_rate)

item2 = Item("iPhone", 1000, 1)
item2.pay_rate = 0.5    # To have diff value for pay_rate for particular instance
print(item2.pay_rate)
# print(item1.calculate_total_price())
# print(Item.pay_rate)

# '__dict__' return a dictionary of all the attributes available for the oblject/class
# print(item1.__dict__)  # All the attributes at instance level
# print(Item.__dict__)  # All the attributes at class level
# print(item1.apply_discount())

item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all_items)

# for item in Item.all_items:
#     print(item.item)