import random
from classes_class import Classes
from Student_class import Student
from Teacher_class import Teacher
from Adress_class import Address
from Discipline_class import Discipline

class SchoolClassList:
    """
    SchoolClassList is a class that represents a list of school classes and provides methods to manage and retrieve information about these classes, including adding students and teachers to classes.

    Attributes:
        classes (list): A list of class objects.

    Methods:
        create_school_classes: Creates school classes, disciplines, teachers, and students and populates the 'classes' attribute with class information.
        add_student_to_class: Adds a student to a specified class if the student is not already in the class.
        add_teacher_to_class: Adds a teacher to a specified class if the teacher is not already assigned to the class.
        get_class_info: Returns a formatted string containing information about a specified class, including its name, disciplines, teachers, and students.
    """
    def __init__(self):
        self.classes = []

    def create_school_classes(self):
        """
     Creates school classes, disciplines, teachers, and students and populates the 'classes' attribute with class information.
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
        english_teacher = Teacher("Nina", "Nina@school.com", Address.generate_random_address())
        physics_teacher = Teacher("Tommy", "Tommy@school.com", Address.generate_random_address())
        new_student1 = Student("Max", "max@example.com", Address.generate_random_address())
        new_student2 = Student("John", "john@example.com", Address.generate_random_address())

        class_info = [class1, class2]

        self.classes = class_info

        self.add_teacher_to_class(class1, math_teacher)
        self.add_teacher_to_class(class1, physics_teacher)
        self.add_teacher_to_class(class2, english_teacher)
        self.add_student_to_class(class1, new_student1)
        self.add_student_to_class(class2, new_student2)

    def add_student_to_class(self, class_obj, student):
        """
    Adds a student to a specified class if the student is not already in the class.

    Para:
        class_obj (Classes): The class object to which the student should be added.
        student (Student): The student object to be added to the class.
        """
        if student not in class_obj.students:
            class_obj.add_student(student)
        else:
            print(f"{student.name} is already in {class_obj.name}")

    def add_teacher_to_class(self, class_obj, teacher):
        """
    Adds a teacher to a specified class if the teacher is not already assigned to the class.

    Para:
        class_obj (Classes): The class object to which the teacher should be added.
        teacher (Teacher): The teacher object to be added to the class.
       """
        if teacher not in class_obj.teachers:
            class_obj.add_teacher(teacher)
    
    def get_class_info(self, class_obj):
        """
    Returns a formatted string containing information about a specified class, including its name, disciplines, teachers, and students.

    Para:
        class_obj (Classes): The class object for which information is to be retrieved.

    Returns:
        str: A formatted string with class information.
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

