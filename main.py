# Zadanie 1
from magazine import Product


product = Product.Product()
product.show()

# Zadanie 2
from oop.student import Student
from oop.library import Library
from oop.employee import Employee
from oop.book import Book
from oop.order import Order
from oop.house import House
from oop.flat import Flat


# Studenci
student1 = Student("Adam", [75, 20, 100, 80, 56, 72])
student2 = Student("Marek", [5, 2, 10, 8, 56, 7])
student3 = Student("Ewa", [40, 45, 50])

print(student1.is_passed())
print(student2.is_passed())


# Biblioteki
library1 = Library(
    "Warszawa", "Marszałkowska 10", "00-001", "08:00-18:00", "123456789"
)
library2 = Library(
    "Kraków", "Floriańska 15", "31-019", "09:00-17:00", "987654321"
)


# Pracownicy
employee1 = Employee(
    "Jan", "Kowalski", "2022-01-10", "1990-05-15",
    "Warszawa", "Polna 1", "00-001", "111111111"
)
employee2 = Employee(
    "Anna", "Nowak", "2023-03-20", "1995-08-22",
    "Kraków", "Długa 5", "31-019", "222222222"
)


# Książki
book1 = Book(library1, "2020-05-12", "Adam", "Mickiewicz", 300)
book2 = Book(library1, "2022-03-20", "Henryk", "Sienkiewicz", 250)
book3 = Book(library1, "2019-07-15", "Bolesław", "Prus", 400)
book4 = Book(library2, "2018-02-10", "Juliusz", "Słowacki", 220)
book5 = Book(library2, "2021-09-01", "Stanisław", "Lem", 350)


# Zamówienia
order1 = Order(employee1, student1, [book1, book2], "2026-10-20")
order2 = Order(employee2, student3, [book3, book4, book5], "2026-10-21")

print(order1)
print(order2)


#nieruchomości
house = House(150, 5, 850000, "ul. Leśna 10", 600)
flat = Flat(55, 3, 450000, "ul. Kwiatowa 5", 2)

print(house)
print(flat)