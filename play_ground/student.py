class Student:

    class_year = 2024
    class_students = 0

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Student.class_students += 1


student1 = Student("Amirofcodes", 37)
student2 = Student("JD", 30)
student3 = Student("YOYOI", 35)
student4 = Student("gojo", 47)

print(
    f"My graduating class of {Student.class_year} has {Student.class_students} students")
