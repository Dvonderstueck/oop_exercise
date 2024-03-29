import Exam_class
from Student_class import Student
import sec_class
from Teacher_class import Teacher
from Director_class import Director
from School_class import School
from classes_class import Classes 
from class_list import SchoolClassList
from Math_class import Math
from English_class import English
from Physics_class import Physics
import Parent_read_points
from Adress_class import Address
import logging
import ErrorHandling
from Person_class import Person

class MainPreparationClass:
    def __init__(self):
        self.school = School("Europa Schule Köln")
        self.school1 = School("Europa Sledasd Köln")
        self.math_teacher = Teacher("Lukas", "Lukas@school.com", Address.generate_random_address())
        #self.math_teacher.set_specific_attributes("New Name", "newemail@school.com", "456 Elm St")
        self.english_teacher = Teacher("Nina", "Nina@school.com", Address.generate_random_address())
        self.physics_teacher = Teacher("Tommy", "Tommy@school.com", Address.generate_random_address())
        self.school_secretary = sec_class.Secretary("Jenny", "secretary@school.com", Address.generate_random_address())
        self.new_student1 = Student("Max", "max@example.com", Address.generate_random_address())
        self.new_student2 = Student("john", "max@example.com", Address.generate_random_address())
        self.director1 = Director("Schmidt", "Schmidt@school.com", Address.generate_random_address())
        self.director2 = Director("Schmt", "Schmidt@school.com", Address.generate_random_address())

        self.school.add_person(self.math_teacher)
        self.school.add_person(self.english_teacher)
        self.school.add_person(self.physics_teacher)
        self.school.add_person(self.school_secretary)
        self.school.add_person(self.new_student1)
        self.school.add_person(self.new_student2,)
        #self.school.add_person(self.school)
        #self.school.add_person(self.director1)
       # self.school.add_person(self.director2)

        
        

        logging.basicConfig(filename='error.log', level=logging.ERROR)
        try:
            self.school.add_person(self.director1)
             #self.school.add_director(self.director1)
            # self.school.remove_director(self.director1)
           
        except ValueError as e:
            print(e)
            logging.error(e)
            raise ErrorHandling.Logged_Exception()

   
        self.exam_names_ = ["Mathematics_exam1", "Mathematics_exam2", "Mathematics_exam3", "english_exam1", "english_exam2", "Physics_exam1", "Physics_exam2", "Physics_exam3"]

        self.math_exam_list = Math("Mathematics")
        self.english_exam_list = English("English")
        self.physics_exam_list = Physics("Physics")

        self.math_teacher.teach_disciplines(self.math_exam_list, self.physics_exam_list)
        self.english_teacher.teach_disciplines(self.english_exam_list, self.math_exam_list)
        self.physics_teacher.teach_disciplines(self.physics_exam_list)
     
    def run(self):
        choice = input("What action would you like to perform?\n 1: Print students,teachers and the director of the school,\n 2: Print classes,\n 3: exam questions,\n 4: Run exam,\n 5: exam points student 1,\n 6: exam points student 2,\n 7: List of teachers with their disciplines,\n 8: Director permission,\n 9: Student1 full info,\n 10: Run exam where secretary gets the grade for students,\n 11: Exit: ")


        match choice:
            case "1":
                self.school.print_students_teachers_and_director()
            
            case "2":
                school_class_instance = SchoolClassList()
                school_class_instance.create_school_classes()  
                class_info = school_class_instance.classes  
                for class_obj in class_info:
                    class_info_str = school_class_instance.get_class_info(class_obj)
                    print(class_info_str)

            case "3":
                self.math_teacher.exam_quest_list_teacher([self.math_exam_list])
                self.english_teacher.exam_quest_list_teacher([self.english_exam_list])
                self.physics_teacher.exam_quest_list_teacher([self.physics_exam_list])
        
            case "4":
                self.new_student2 = Exam_class.exams_for_student(self.new_student2)

            case "5":
                self.new_student1.read_exam_data(self.exam_names_)  
                print(f"Exam data for {self.new_student1.name}:\n")
                for exam_name, data in self.new_student1.exam_data.items():
                    print(f"{exam_name}: {data}\n")

            case "6":
                print(f"Exam data for {self.new_student2.name}:\n")
                self.new_student2.read_exam_data(self.exam_names_) 
                for exam_name, data in self.new_student2.exam_data.items():
                    print(f"{exam_name}: {data}\n")

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
            
                final_grade_via_secretary = sec_class.Secretary.print_final_grade_via_secretary(self)

            case "11":
                print("Exiting the program.")
                return

if __name__ == "__main__":
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    
    try:
        main = MainPreparationClass()
        main.run()
    except ErrorHandling.Logged_Exception as e:
        pass
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"An unexpected error occurred: {e}")


