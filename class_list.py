from classes_class import Classes
from Student_class import Student
from Teacher_class import Teacher
from Adress_class import Address
from Discipline_class import Discipline
import random

class SchoolClassList:
    """
    A class for managing school classes, disciplines, teachers, and students.

    Methods:
        school_class_list(self):
            Create and populate school classes, disciplines, teachers, and students.

        get_class_info(self, class_obj):
            Get information about a specific school class.

        add_student_to_class(class_obj, student):
        Add a student to a school class if they are not already enrolled.

        add_teacher_to_class(class_obj, teacher):
        Add a teacher to a school class if they are not already assigned.


    """

    def school_class_list(self):
        """
        Create and populate school classes, disciplines, teachers, and students.

        Returns:
            list: A list of school class objects.

        """

        class1 = Classes("class 1")
        class2 = Classes("class 2") 

        math_discipline = Discipline("Mathematics")
        physics_discipline = Discipline("Physics")
        english_discipline = Discipline("English")

        class1.add_discipline(math_discipline.name)
        class1.add_discipline(physics_discipline.name)
        class2.add_discipline(english_discipline.name) 

        math_teacher = Teacher("Lukas", "lukas@school.com", Address.generate_random_address())
        english_teacher = Teacher("Nina", "Nina@school.com",Address.generate_random_address())
        physics_teacher = Teacher("Tommy", "Tommy@school.com",Address.generate_random_address())
        new_student1 = Student("Max", "max@example.com", Address.generate_random_address())
        new_student2 = Student("john", "john@example.com", Address.generate_random_address())

        class_info = [class1, class2]
        
        def add_student_to_class(class_obj, student):
            """
             Add a student to a school class if they are not already enrolled.

            Para:
            class_obj (Classes): The school class object to which the student should be added.
            student (Student): The student object to be added to the class.

             """
            if student not in class_obj.students:
                class_obj.add_student(student)
            else:
                print(f"{student.name} is already in {class_obj.name}")

        def add_teacher_to_class(class_obj, teacher):
            """
            Add a teacher to a school class if they are not already assigned.

            Args:
                class_obj (Classes): The school class object to which the teacher should be added.
                teacher (Teacher): The teacher object to be added to the class.

            """
            if teacher not in class_obj.teachers:
                class_obj.add_teacher(teacher)
          
        add_teacher_to_class(class1, math_teacher)
        add_teacher_to_class(class1, physics_teacher)
        add_teacher_to_class(class2, english_teacher)
        add_student_to_class(class1, new_student1)
        add_student_to_class(class2, new_student2)

        return class_info
    
    def get_class_info(self, class_obj):
        """
        Get information about a specific school class.

        Args:
            class_obj (Classes): The school class object for which information is requested.

        Returns:
            str: Information about the school class, including its name, disciplines, teachers, and students.

        """
        class_info = f"Class: {class_obj.name}\n"
        class_info += f"Disciplines: {', '.join(class_obj.disciplines)}\n\n"
        
        class_info += "Teachers:\n"
        for teacher in class_obj.teachers:
            class_info += f"{teacher.name}\n"
        
        class_info += "Students:\n"
        for student in class_obj.students:
            class_info += f"{student.name}\n"
        
        return class_info

        
    

school_class_instance = SchoolClassList()
school_class_instance.school_class_list()
