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
from new_student1_parent_class import student1_par
from new_student2_parent_class import student2_par


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
        self.Max_par = student1_par()


        
        self.math_exam1 = self.Max_par.read_file("max_Mathematics_exam1_saved_points.txt")
        # math_exam2 = Max_par.read_file("max_Mathematics_exam2_saved_points.txt")
        # math_exam3 = Max_par.read_file("max_Mathematics_exam3_saved_points.txt")

        # english_exam1 = Max_par.read_file("max_english_exam1_saved_points.txt")
        # english_exam2 = Max_par.read_file("max_english_exam2_saved_points.txt")

        # physics_exam1 = Max_par.read_file("max_Physics_exam1_saved_points.txt")
        # physics_exam2 = Max_par.read_file("max_Physics_exam2_saved_points.txt")
        # physics_exam3 = Max_par.read_file("max_Physics_exam3_saved_points.txt")

       

    

    def run(self):
        choice = input("What action would you like to perform? (1: Print students and teachers, 2: Print classes, 3: exam questions, 4: Run exam , 5: exam points student 1 , 6: Exit): ")

        if choice == "1":
            self.school.add_teacher(self.math_teacher)
            self.school.add_teacher(self.english_teacher)
            self.school.add_teacher(self.physics_teacher)
            self.school.add_student(self.new_student1)
            self.school.add_student(self.new_student2)
            self.person = classes.print_students_and_teachers(self)
            
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
             print(self.math_exam1)
        
        elif choice == "6":
            print("Exiting the program.")
            return
        

if __name__ == "__main__":
    main = Main_preparation_class()
    main.run()
