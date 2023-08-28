
from Exam_question_class import exam_question
import test123
from Student_class import Student
from Discipline_class import Discipline
from Adress_class import adress
import sec_class
from Teacher_class import Teacher
from Director_class import Director
from School_class import School
from classes_class import classes 
from class_list import school_class_list
from info_class import info
from Math_class import Math
from English_class import English
from Physics_class import Physics

class Main_class:
    def __init__(self):
        self.address_instance = adress()
        self.school = School("Europa Schule köln")
        self.math_teacher = Teacher("Lukas", "max@school.com", self.address_instance.generate_random_address())
        self.school_secretary = sec_class.Secretary("Jenny", "secretary@school.com", self.address_instance.generate_random_address())
        self.new_student1 = Student("Max", "max@example.com", self.address_instance.generate_random_address())
        self.new_student2 = Student("john", "max@example.com", self.address_instance.generate_random_address())
        self.director1 = Director("Schmidt", "Schmidt@school.com", self.address_instance.generate_random_address(), "")

    def print_students_and_teachers(self):
        print("List of Students:")
        for student in self.school.students:
            print(student.name)

        print("\nList of Teachers:")
        for teacher in self.school.teachers:
            print(teacher.name)

    def run(self):

        self.school_class_instance = school_class_list()
        self.school_class_instance.school_class_list()

        self.math_exam_list = Math("Mathematics")
        self.english_exam_list = English("English")
        self.physics_exam_list = Physics("Physics")

        self.school.add_teacher(self.math_teacher)
        self.school.add_student(self.new_student1)
        self.school.add_student(self.new_student2)

        self.math_teacher.exam_quest_list_teacher(self.math_exam_list, self.english_exam_list, self.physics_exam_list)

        self.print_students_and_teachers()

        print("Finished running.")

        self.new_student2 = test123.exams_for_student(self.new_student2)

if __name__ == "__main__":
    main = Main_class()
    main.run()
