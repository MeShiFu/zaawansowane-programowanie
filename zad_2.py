import statistics


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


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik: {self.first_name} {self.last_name}, "
            f"data zatrudnienia: {self.hire_date}, "
            f"data urodzenia: {self.birth_date}, "
            f"adres: {self.city}, {self.street}, {self.zip_code}, "
            f"telefon: {self.phone}"
        )


class Book:
    def __init__(
        self,
        library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka: {self.author_name} {self.author_surname}, "
            f"data publikacji: {self.publication_date}, "
            f"liczba stron: {self.number_of_pages}, "
            f"biblioteka: [{self.library}]"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_description = "\n".join(f"  - {book}" for book in self.books)

        return (
            f"Zamówienie z dnia: {self.order_date}\n"
            f"Pracownik: {self.employee}\n"
            f"Student: {self.student}\n"
            f"Książki:\n{books_description}"
        )


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if statistics.mean(self.marks) > 50:
            return True
        else:
            return False

    def __str__(self):
        return (
            f"Student: {self.name}, "
            f"oceny: {self.marks}, "
            f"zaliczył: {self.is_passed()}"
        )


library1 = Library(
    "Warszawa", "Marszałkowska 10", "00-001", "08:00-18:00", "123456789"
)
library2 = Library(
    "Kraków", "Floriańska 15", "31-019", "09:00-17:00", "987654321"
)
employee1 = Employee(
    "Jan",
    "Kowalski",
    "2022-01-10",
    "1990-05-15",
    "Warszawa",
    "Polna 1",
    "00-001",
    "111111111",
)
employee2 = Employee(
    "Anna",
    "Nowak",
    "2023-03-20",
    "1995-08-22",
    "Kraków",
    "Długa 5",
    "31-019",
    "222222222",
)
employee3 = Employee(
    "Piotr",
    "Wiśniewski",
    "2021-06-01",
    "1988-11-12",
    "Warszawa",
    "Leśna 7",
    "00-002",
    "333333333",
)
student1 = Student("Adam", [60, 70, 80])
student2 = Student("Ewa", [40, 45, 50])
student3 = Student("Tomek", [80, 90, 75])
book1 = Book(library1, "2020-05-12", "Adam", "Mickiewicz", 300)
book2 = Book(library1, "2022-03-20", "Henryk", "Sienkiewicz", 250)
book3 = Book(library1, "2019-07-15", "Bolesław", "Prus", 400)
book4 = Book(library2, "2018-02-10", "Juliusz", "Słowacki", 220)
book5 = Book(library2, "2021-09-01", "Stanisław", "Lem", 350)
order1 = Order(employee1, student1, [book1, book2], "2026-10-20")

order2 = Order(employee2, student2, [book3, book4, book5], "2026-10-21")
print(order1)
print(order2)
