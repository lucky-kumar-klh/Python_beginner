class Pokemon:
    def __init__(self, name, XP, Health):
        self.name = name
        self.XP = XP
        self.Health = Health

    def list_details(self):
        print(f"Pokemon: {self.name}, XP: {self.XP}, Health: {self.Health}")

p1 = Pokemon("Charizard", XP = 40, Health = 100)
p1.list_details()


class Legendary_Pokemon(Pokemon):
    def __init__(self, name, XP, Health, special_ability):
        super().__init__(name, XP, Health)
        self.special_ability = special_ability 
    
    def list_details(self):
        return super().list_details()

l1 = Legendary_Pokemon("Giratina", 101, 200, "Physkik Power")
l1.list_details()
