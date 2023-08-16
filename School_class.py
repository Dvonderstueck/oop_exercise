
from Student_class import Student
from classes_class import classes   
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
from Secretary_class import Secretary
from Exam_question_class import exam_question

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to {self.name}")

    

school = School("Europa Schule köln")


new_student = Student("Max", "max@example.com", "123 Main St")
school.add_student(new_student)
