from School_class import school
from classes_class import classes 
from Student_class import Student
from Teacher_class import Teacher
from Adress_class import adress
from Discipline_class import Discipline
class school_class_list:



    def school_class_list(self):

        address_instance = adress()

        class1 = classes("class 1")
        class2 = classes("class 2") 

        math_discipline = Discipline("Mathematics")
        physics_discipline = Discipline("Physics")
        english_discipline = Discipline("English")

        class1.add_discipline(math_discipline.name)
        class1.add_discipline(physics_discipline.name)
        class2.add_discipline(english_discipline.name) 


        math_teacher = Teacher("Lukas", "max@school.com", address_instance.generate_random_address())
        new_student1 = Student("Max", "max@example.com", address_instance.generate_random_address())
        new_student2 = Student("john", "max@example.com", address_instance.generate_random_address())


        selected_students = [new_student1]
        selected_teachers = [math_teacher]

        for student in selected_students:
            class1.add_student(student)
        for teacher in selected_teachers:
            class1.add_teacher(teacher)

        class_info = [class1, class2]
        for class_obj in class_info:
            print(class_obj.setup_and_print())
            
            print("Teachers:")
            for teacher in class_obj.teachers:
                print(teacher.name)
            print("Students:")
            for student in class_obj.students:
                print(student.name)
            print()

school_class_instance = school_class_list()
school_class_instance.school_class_list()