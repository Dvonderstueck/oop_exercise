
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
        self.directors = []
        self.taught_disciplines = []

    def add_student(self, student):
        self.students.append(student)
        
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_Director(self, director):
        self.directors.append(director)

    def teach_discipline(self, discipline1, discipline2):
        self.taught_disciplines.extend([discipline1, discipline2])

    

    



        

    

school = School("Europa Schule köln")

# math_teacher = Teacher("Lukas", "Lukas@school.com", address_instance.generate_random_address())
# english_teacher = Teacher("Nina", "Nina@school.com", address_instance.generate_random_address())
# physics_teacher = Teacher("Tommy", "Tommy@school.com", address_instance.generate_random_address())
# school_secretary = sec_class.Secretary("Jenny", "secretary@school.com", address_instance.generate_random_address())  
# new_student1 = Student("Max", "max@example.com", address_instance.generate_random_address())
# new_student2 = Student("john", "max@example.com", address_instance.generate_random_address())
# director1 = Director("Schmidt", "Schmidt@school.com", address_instance.generate_random_address(), "Europaschule köln")


# school.add_teacher(math_teacher)

# school.add_student(new_student1)
# school.add_student(new_student2)

# math_discipline = Discipline("Mathematics")
# physics_discipline = Discipline("Physics")
# english_discipline = Discipline("English")

# math_teacher.teach_discipline(math_discipline,physics_discipline)
# english_teacher.teach_discipline(english_discipline,math_discipline)
# physics_teacher.teach_discipline(physics_discipline,physics_discipline)
