from School_class import School
class Classes:
    """
    A class for representing school classes.

    Attributes:
        name (str): The name of the class.
        disciplines (list): A list of disciplines taught in the class.
        students (list): A list of students in the class.
        teachers (list): A list of teachers in the class.
        directors (list): A list of directors associated with the class.
    """

    def __init__(self, name):
        """
        Initialize a Classes object with a name.

        Para:
            name (str): The name of the class.

        """
        self.name = name
        self.disciplines = []
        self.students = []
        self.teachers = []
        self.directors = []

    def add_discipline(self, discipline):
        """
        Add a discipline to the class.

        Para:
            discipline (Discipline): The discipline to be added.

        """
        self.disciplines.append(discipline)

    def list_disciplines(self):
        """
        List the disciplines taught in the class.

        Returns:
            list: A list of disciplines in the class.

        """
        return self.disciplines
    
    def add_student(self, student):
        """
        Add a student to the class.

        Para:
            student (Student): The student object to be added.

        """
        self.students.append(student)

    def add_teacher(self, teacher):
        """
        Add a teacher to the class.

        Para:
            teacher (Teacher): The teacher object to be added.

        """
        self.teachers.append(teacher)

    @staticmethod
    def print_students_teachers_and_director(school, math_teacher, english_teacher, physics_teacher, director1, new_student1, new_student2):
        """
        Print the list of students, teachers, and directors in the class.

        """
        print("List of Students:")
        for student in school.students:
            print(student.name)

        print("\nList of Teachers:")
        for teacher in school.teachers:
            print(teacher.name)

        print("\nDirector:")
        print(director1.name)
            
    @staticmethod
    def teachers_and_students(math_teacher, english_teacher, physics_teacher, director1, new_student1, new_student2):
        """
        Add teachers and students (and Director) to the class.

        """
        School.add_teacher(math_teacher)
        School.add_teacher(english_teacher)
        School.add_teacher(physics_teacher)
        School.add_director(director1)
        School.add_student(new_student1)
        School.add_student(new_student2)
