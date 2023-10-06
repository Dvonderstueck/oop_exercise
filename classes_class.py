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

    def add_discipline(self, discipline):
        """
        Add a discipline to the class.

        Para:
            discipline (Discipline): The discipline object to be added.
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
