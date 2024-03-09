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
