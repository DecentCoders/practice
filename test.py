class Student:
    # Constructor: Initialize student attributes
    def __init__(self, name, age, grade):
        self.name = name  # Public attribute
        self.age = age
        self.grade = grade

    # Method to display student info
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    # Method to check if student passed
    def is_passed(self):
        return self.grade >= 60

# Test the class
student1 = Student("Alice", 18, 85)
student2 = Student("Bob", 17, 55)

student1.show_info()  # Output: Name: Alice, Age: 18, Grade: 85
print(f"{student1.name} Passed? {student1.is_passed()}")  # True

student2.show_info()  # Output: Name: Bob, Age: 17, Grade: 55
print(f"{student2.name} Passed? {student2.is_passed()}")  # False