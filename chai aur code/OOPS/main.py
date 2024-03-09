from Items import Item
from Phone import Phone

# item1 = Item("Laptop", 1000, 1)
# print(item1.pay_rate)

# item2 = Item("iPhone", 1000, 1)
# item2.pay_rate = 0.5    # To have diff value for pay_rate for particular instance
# print(item2.pay_rate)
# print(item1.calculate_total_price())
# print(Item.pay_rate)

# '__dict__' return a dictionary of all the attributes available for the object/class
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

# print(Item.is_integer(7.0))

phone1 = Phone("Samsung", 3000, 3, 1)

# print(Phone.all_items)

item_2 = Item("CPU", 2000, 3)
# item_2.__item = "i5_12550U"
item_2.set_item_name("i5_12550U")
print(item_2.get_item_name())