class Student:
    def __init__(self, name: str, marks: []):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if (sum(self.marks) / len(self.marks)) > 50:
            return True
        return False


s1 = Student("Adam", [62, 80, 25])
print(s1.is_passed())

s2 = Student("Jola", [15, 57, 43])
print(s2.is_passed())
