import statistics


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if statistics.mean(self.marks) > 50:
            return True
        else:
            return False


Adam = Student("Adam", [75, 20, 100, 80, 56, 72])
Marek = Student("Marek", [5, 2, 10, 8, 56, 7])

print(Adam.is_passed())
print(Marek.is_passed())
