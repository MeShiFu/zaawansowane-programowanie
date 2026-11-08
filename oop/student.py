import statistics


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return statistics.mean(self.marks) > 50

    def __str__(self):
        return (
            f"Student: {self.name}, "
            f"oceny: {self.marks}, "
            f"zaliczył: {self.is_passed()}"
        )
