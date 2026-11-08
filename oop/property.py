class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Powierzchnia: {self.area} m², "
            f"liczba pokoi: {self.rooms}, "
            f"cena: {self.price} zł, "
            f"adres: {self.address}"
        )
