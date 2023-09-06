from Exam_question_class import ExamQuestion
import Exam_class
from Student_class import Student
from Discipline_class import Discipline
from Adress_class import Adress
import sec_class
from Teacher_class import Teacher
import Teacher_class
from Director_class import Director
from School_class import School
from classes_class import Classes 
from class_list import SchoolClassList
from info_class import Info
from Math_class import Math
from English_class import English
from Physics_class import Physics
from new_student1_parent_class import Student1ExamPoints
from new_student2_parent_class import Student2ExamPoints


class MainPreparationClass:
    
    def __init__(self):
        self.address_instance = Adress()
        self.school = School("Europa Schule köln")
        self.math_teacher = Teacher("Lukas", "Lukas@school.com", self.address_instance.generate_random_address())
        self.english_teacher = Teacher("Nina", "Nina@school.com", self.address_instance.generate_random_address())
        self.physics_teacher = Teacher("Tommy", "Tommy@school.com", self.address_instance.generate_random_address())
        self.school_secretary = sec_class.Secretary("Jenny", "secretary@school.com", self.address_instance.generate_random_address())
        self.new_student1 = Student("Max", "max@example.com", self.address_instance.generate_random_address())
        self.new_student2 = Student("john", "max@example.com", self.address_instance.generate_random_address())
        self.director1 = Director("Schmidt", "Schmidt@school.com", self.address_instance.generate_random_address(), self.school)

        self.math_exam_list = Math("Mathematics")
        self.english_exam_list = English("English")
        self.physics_exam_list = Physics("Physics")

        self.math_teacher.teach_discipline(self.math_exam_list, self.physics_exam_list)
        self.english_teacher.teach_discipline(self.english_exam_list, self.math_exam_list)
        self.physics_teacher.teach_discipline(self.physics_exam_list, self.physics_exam_list)
     

    def run(self):
        choice = input("What action would you like to perform?\n 1: Print students and teachers,\n 2: Print classes,\n 3: exam questions,\n 4: Run exam,\n 5: exam points student 1,\n 6: exam points student 2,\n 7: List of teachers with their disciplines,\n 8: Director permission,\n 9: Student1 full info,\n 10: Run exam where secretary gets the grade for students,\n 11: Exit: ")

        match choice:
            case "1":
                self.person_list = Classes.teachers_and_students(self)
                self.person = Classes.print_students_teachers_and_director(self)
            
            case "2":
                self.school_class_instance = SchoolClassList()
                class_info = self.school_class_instance.school_class_list()
                for class_obj in class_info:
                    class_info_str = self.school_class_instance.get_class_info(class_obj)
                    print(class_info_str)

            case "3":
                self.math_teacher.exam_quest_list_teacher([self.math_exam_list])
                self.english_teacher.exam_quest_list_teacher([self.english_exam_list])
                self.physics_teacher.exam_quest_list_teacher([self.physics_exam_list])
        
            case "4":
                self.new_student2 = Exam_class.exams_for_student(self.new_student1)

            case "5":
                self.student1_exam_points = Student1ExamPoints.read_student1_points(self)
                print(self.student1_exam_points1, "\n", self.student1_exam_points2, "\n", self.student1_exam_points3, "\n")

            case "6":
                self.student2_exam_points = Student2ExamPoints.read_student2_points(self)
                print(self.student2_exam_points1, "\n", self.student2_exam_points2, "\n", self.student2_exam_points3, "\n")


            case "7":
                teachers = [self.math_teacher, self.english_teacher, self.physics_teacher]
                for teacher in teachers:
                    teacher.list_teacher_disciplines()

            case "8":
                if self.director1.can_do_everything:
                    self.director1.teach_discipline(self.math_exam_list, self.english_exam_list, self.physics_exam_list)
                    self.director1.exam_quest_list_teacher(self.math_exam_list, self.english_exam_list, self.physics_exam_list)
                

            case "9":
                print(self.new_student1.get_full_info())

            case "10":
                self.new_student2 = Exam_class.exams_for_student(self.new_student2)
            
                self.final_grade_via_secretary = sec_class.Secretary.print_final_grade_via_secretary(self)

            case "11":
                print("Exiting the program.")
                return
