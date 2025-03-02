class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Average Grade: {self.average_grade():.2f}"

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_student_list(self):
        print(f"Danh sách sinh viên do giảng viên {self.name} quản lý:")
        for student in self.students:
            print(student)
    
    def average_class_grade(self):
        if self.students:
            return sum(student.average_grade() for student in self.students) / len(self.students)
        return 0

teacher = Teacher("Nguyễn Văn A")

student1 = Student("Trần Thị B", 20, [8.0, 7.5, 8.5])
student2 = Student("Lê Văn C", 21, [5.5, 6.0, 4.5])
student3 = Student("Phạm Minh D", 22, [9.5, 9.0, 9.0])

teacher.add_student(student1)
teacher.add_student(student2)
teacher.add_student(student3)

teacher.print_student_list()
print(f"Điểm trung bình của lớp: {teacher.average_class_grade():.2f}")
