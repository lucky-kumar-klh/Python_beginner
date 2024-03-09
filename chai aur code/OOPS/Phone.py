from Items import Item

class Phone(Item):
    def __init__(self, item: str, price: float, quantity = 0, broken_phone = 0):
        super().__init__(item, price, quantity)
        assert broken_phone >= 0, f"Broken Phone {broken_phone} should be greater than or equal to zero"
        self.broken_phone = broken_phone