import requests


class Brewery:
    def __init__(self, data):
        # Przypisujemy wszystkie standardowe pola z API Open Brewery DB
        self.id = data.get("id")
        self.name = data.get("name")
        self.brewery_type = data.get("brewery_type")
        self.address_1 = data.get("address_1")
        self.address_2 = data.get("address_2")
        self.address_3 = data.get("address_3")
        self.city = data.get("city")
        self.state_province = data.get("state_province")
        self.postal_code = data.get("postal_code")
        self.country = data.get("country")
        self.longitude = data.get("longitude")
        self.latitude = data.get("latitude")
        self.phone = data.get("phone")
        self.website_url = data.get("website_url")
        self.state = data.get("state")
        self.street = data.get("street")

    def __str__(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Type: {self.brewery_type}\n"
            f"Address: {self.address_1}\n"
            f"City: {self.city}\n"
            f"State/Province: {self.state_province}\n"
            f"Postal code: {self.postal_code}\n"
            f"Country: {self.country}\n"
            f"Phone: {self.phone}\n"
            f"Website: {self.website_url}"
        )


url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
response = requests.get(url)
dane_json = response.json()

lista_browarow = []
for item in dane_json:
    browar = Brewery(item)
    lista_browarow.append(browar)

for browar in lista_browarow:
    print(browar)
    print("-" * 40)
