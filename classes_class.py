

class Classes:
    """
    A class for representing school classes.

    Attributes:
        name (str): The name of the class.
        disciplines (list): A list of disciplines taught in the class.
        students (list): A list of students in the class.
        teachers (list): A list of teachers in the class.
        directors (list): A list of directors associated with the class.

    Methods:
        __init__(self, name):
            Initialize a Classes object with a name.

        add_discipline(self, discipline):
            Add a discipline to the class.

        list_disciplines(self):
            List the disciplines taught in the class.

        add_student(self, student):
            Add a student to the class.

        add_teacher(self, teacher):
            Add a teacher to the class.

        print_students_teachers_and_director(self):
            Print the list of students, teachers, and directors in the class.

        teachers_and_students(self):
            Add teachers and students (and Director) to the class.

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

    def print_students_teachers_and_director(self):
        """
        Print the list of students, teachers, and directors in the class.

        """
        print("List of Students:")
        for student in self.school.students:
            print(student.name)

        print("\nList of Teachers:")
        for teacher in self.school.teachers:
            print(teacher.name)

        print("\nDirector:")
        for director in self.school.directors:
            print(director.name)

    def teachers_and_students(self):
        """
        Add teachers and students (and Director) to the class.

        """

        self.school.add_teacher(self.math_teacher)
        self.school.add_teacher(self.english_teacher)
        self.school.add_teacher(self.physics_teacher)
        self.school.add_Director(self.director1)
        self.school.add_student(self.new_student1)
        self.school.add_student(self.new_student2)
    
  