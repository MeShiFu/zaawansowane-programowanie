class Library:
    def __init__(self, city, street, zip_code, open_hrs: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hrs = open_hrs
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka: {self.city}, {self.street}, "
            f"{self.zip_code}, godziny otwarcia: {self.open_hrs}, "
            f"telefon: {self.phone}"
        )