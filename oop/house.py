from oop.property import Property


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom: {super().__str__()}, "
            f"powierzchnia działki: {self.plot} m²"
        )