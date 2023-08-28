
from Student_class import Student
from classes_class import classes   
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
import sec_class
from Adress_class import adress

address_instance = adress()
class School:
    def __init__(self, name,):
        self.name = name
        self.adress = address_instance
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to {self.name}")
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"{teacher.name} has been added to {self.name}")

    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.adress}"
    

school = School("Europa Schule köln")

math_teacher = Teacher("Lukas", "max@school.com", address_instance.generate_random_address())
school_secretary = sec_class.Secretary("Jenny", "secretary@school.com", address_instance.generate_random_address())  
new_student1 = Student("Max", "max@example.com", address_instance.generate_random_address())
new_student2 = Student("john", "max@example.com", address_instance.generate_random_address())
director1 = Director("Schmidt", "Schmidt@school.com", address_instance.generate_random_address(), "Europaschule köln")

# school.add_teacher(math_teacher)

# school.add_student(new_student1)
# school.add_student(new_student2)

math_discipline = Discipline("Mathematics")
physics_discipline = Discipline("Physics")
english_discipline = Discipline("English")

math_teacher.teach_discipline(math_discipline.name,)
math_teacher.teach_discipline(physics_discipline.name)

class1 = classes("class 1")
class2 = classes("class 2")  
class1.add_discipline(math_discipline.name)
class1.add_discipline(physics_discipline.name)
class2.add_discipline(english_discipline.name) 
