from Student_class import Student
from classes_class import Classes   
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
import sec_class
from Adress_class import Adress

address_instance = Adress()


class School:
    
    def __init__(self, name):
        self.name = name
        self.adress = address_instance
        self.students = []
        self.teachers = []
        self.directors = []
        self.taught_disciplines = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"{self.name}"
        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_Director(self, director):
        self.directors.append(director)

    def teach_discipline(self, discipline1, discipline2):
        self.taught_disciplines.extend([discipline1, discipline2])

school = School("Europa Schule köln")
