class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    def __str__(self):
        return (f"Powierzchnia: {self.area} m², "
                f"liczba pokoi: {self.rooms}, "
                f"cena: {self.price} zł, "
                f"adres: {self.address}")
class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address) 
        self.plot = plot
    def __str__(self):
        return f"Dom: {super().__str__()}, powierzchnia działki: {self.plot} m²"
class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address) 
        self.floor = floor
    def __str__(self):
        return f"Mieszkanie: {super().__str__()}, piętro: {self.floor}"
house = House(150, 5, 850000, "ul. Leśna 10", 600)
flat = Flat(55, 3, 450000, "ul. Kwiatowa 5", 2)
print(house)
print(flat)