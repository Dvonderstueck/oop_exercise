from Exam_question_class import exam_question
import test123
from Student_class import Student
from Discipline_class import Discipline
from Adress_class import adress
import sec_class
from Teacher_class import Teacher
import Teacher_class
from Director_class import Director
from School_class import School
from classes_class import classes 
from class_list import school_class_list
from info_class import info
from Math_class import Math
from English_class import English
from Physics_class import Physics
from new_student1_parent_class import Student1_exam_points
from new_student2_parent_class import Student2_exam_points



class Main_preparation_class:
    def __init__(self):
        self.address_instance = adress()
        self.school = School("Europa Schule köln")
        self.math_teacher = Teacher("Lukas", "Lukas@school.com", self.address_instance.generate_random_address())
        self.english_teacher = Teacher("Nina", "Nina@school.com", self.address_instance.generate_random_address())
        self.physics_teacher = Teacher("Tommy", "Tommy@school.com", self.address_instance.generate_random_address())
        self.school_secretary = sec_class.Secretary("Jenny", "secretary@school.com", self.address_instance.generate_random_address())
        self.new_student1 = Student("Max", "max@example.com", self.address_instance.generate_random_address())
        self.new_student2 = Student("john", "max@example.com", self.address_instance.generate_random_address())
        self.director1 = Director("Schmidt", "Schmidt@school.com", self.address_instance.generate_random_address(), "")

        self.math_exam_list = Math("Mathematics")
        self.english_exam_list = English("English")
        self.physics_exam_list = Physics("Physics")

        self.math_teacher.teach_discipline(self.math_exam_list, self.physics_exam_list)
        self.english_teacher.teach_discipline(self.english_exam_list, self.math_exam_list)
        self.physics_teacher.teach_discipline(self.physics_exam_list, self.physics_exam_list)
     


    def run(self):
        choice = input("What action would you like to perform?\n 1: Print students and teachers,\n 2: Print classes,\n 3: exam questions,\n 4: Run exam,\n 5: exam points student 1,\n 6: exam points student 2,\n 7: List of teachers with their disciplines,\n 8: Director permission,\n 9: Student1 full info,\n 10: Exit: ")

        if choice == "1":
            self.school.add_teacher(self.math_teacher)
            self.school.add_teacher(self.english_teacher)
            self.school.add_teacher(self.physics_teacher)
            self.school.add_Director(self.director1)
            self.school.add_student(self.new_student1)
            self.school.add_student(self.new_student2)
            self.person = classes.print_students_teachers_and_director(self)
            
        elif choice == "2":
            self.school_class_instance = school_class_list()
            class_info = self.school_class_instance.school_class_list()
            for class_obj in class_info:
                class_info_str = self.school_class_instance.get_class_info(class_obj)
                print(class_info_str)

        elif choice == "3":
            self.math_teacher.exam_quest_list_teacher(self.math_exam_list)
            self.english_teacher.exam_quest_list_teacher(self.english_exam_list)
            self.physics_teacher.exam_quest_list_teacher(self.physics_exam_list)
        elif choice == "4":
            self.new_student2 = test123.exams_for_student(self.new_student1)

        elif choice == "5":
             self.student1_exam_points1 = Student1_exam_points.math_exam_data
             self.student1_exam_points2 = Student1_exam_points.english_exam_data
             self.student1_exam_points3 = Student1_exam_points.physics_exam_data
             print(self.student1_exam_points1, "\n", self.student1_exam_points2, "\n", self.student1_exam_points3, "\n")

        elif choice == "6":
            self.Student2_exam_points1 = Student2_exam_points.math_exam_data
            self.Student2_exam_points2 = Student2_exam_points.english_exam_data
            self.Student2_exam_points3 = Student2_exam_points.physics_exam_data
            print(self.Student2_exam_points1, "\n", self.Student2_exam_points2, "\n", self.Student2_exam_points3, "\n")


        elif choice == "7":
            teachers = [self.math_teacher, self.english_teacher, self.physics_teacher]
            for teacher in teachers:
                teacher.list_teacher_disciplines()

        elif choice == "8":
         if self.director1.can_do_everything:
                self.director1.teach_discipline(self.math_exam_list, self.english_exam_list, self.physics_exam_list)
                self.director1.exam_quest_list_teacher(self.math_exam_list, self.english_exam_list, self.physics_exam_list)

        elif choice == "9":
            print(self.new_student1.get_full_info())


        elif choice == "10":
            print("Exiting the program.")
            return

    
