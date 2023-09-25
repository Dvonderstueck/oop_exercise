import School_class

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

        Parameters:
            teacher (Teacher): The teacher object to be added.
        """
        self.teachers.append(teacher)

    @staticmethod
    def print_students_teachers_and_director(school):
        """
        Print the list of students, teachers, and directors in the class.

        Para:
            school (Classes): The school class object.
        """
        print("List of Students:")
        for student in school.students:
            print(student.name)

        print("\nList of Teachers:")
        for teacher in school.teachers:
            print(teacher.name)

        print("\nDirectors:")
        for director in school.directors:
            print(director.name)
            
    @staticmethod
    def teachers_and_students(school, teachers, director, students):
        """
        Add teachers, director, and students to the class.

        Para:
            school (Classes): The school class object to which to add the teachers, director, and students.
            teachers (list): A list of teacher objects to be added.
            director (Director): The director object to be added.
            students (list): A list of student objects to be added.
        """
        for teacher in teachers:
            school.add_teacher(teacher)
        
        school.add_director(director)
        
        for student in students:
            school.add_student(student)
