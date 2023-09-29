from Student_class import Student
from classes_class import Classes   
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
import sec_class

class School:
    """
    School is a class representing a school institution.

    Attributes:
        name (str): The name of the school.
        address (Address): An instance of the Address class for the school's address.
        students (list): A list to store student objects associated with the school.
        teachers (list): A list to store teacher objects associated with the school.
        director (Director): The director object associated with the school.
        taught_disciplines (list): A list to store the disciplines taught by the school.

    Methods:
        add_student(self, student):
        Add a student to the school.

        __str__(self):
        Return a string representation of the school's name.

        add_teacher(self, teacher):
        Add a teacher to the school.

        add_director(self, director):
        Add a director to the school.

        teach_discipline(self, discipline1, discipline2):
        Assign two disciplines to be taught by the school.

        print_students_teachers_and_director(school):
        Print the list of students, teachers, and the director associated with the school.

        show_teachers_students_director(school, teachers, director, students):
        Add teachers, director, and students to the school.

    """
    
    
    def __init__(self, name):
        """
        Initialize a School object.

        Parameters:
            name (str): The name of the school.

        Attributes:
            name (str): The name of the school.
            address (Address): An instance of the Address class for the school's address.
            students (list): A list to store student objects associated with the school.
            teachers (list): A list to store teacher objects associated with the school.
            director (Director): The director object associated with the school.
            taught_disciplines (list): A list to store the disciplines taught by the school.

        """
        self.name = name
        self.students = []
        self.teachers = []
        self.director = None
        self.taught_disciplines = []


    def add_student(self, student):
        """
        Add a student to the school.

        Parameters:
            student (Student): The student object to be added to the school's student list.

        """
        self.students.append(student)

    def __str__(self):
        """
        Return a string representation of the school's name.

        Returns:
            str: The name of the school.

        """
        return f"{self.name}"
        
    def add_teacher(self, teacher):
        """
        Add a teacher to the school.

        Parameters:
            teacher (Teacher): The teacher object to be added to the school's teacher list.

        """
        self.teachers.append(teacher)

    def add_director(self, director):
        """
        Add a director to the school.

        Parameters:
            director (Director): The director object to be added to the school's director list.

        """
        if self.director is None:
            if director.school is None: 
                self.director = director
                director.school = self
            else:
             raise ValueError(f"{director.name} is already the director of another school: {director.school.name}.")
        else:
            raise ValueError(f"{self.name} already has a director: {self.director.name}.")


    def teach_discipline(self, discipline1, discipline2):
        """
        Assign two disciplines to be taught by the school.

        Parameters:
            discipline1 (Discipline): The first discipline to be taught.
            discipline2 (Discipline): The second discipline to be taught.

        """
        self.taught_disciplines.extend([discipline1, discipline2])


    def print_students_teachers_and_director(self):
        """
        Print the list of students, teachers, and the director associated with the school.

        Parameters:
            school (School): The school object.

        """
        print("List of Students:")
        for student in self.students:
            print(student.name)

        print("\nList of Teachers:")
        for teacher in self.teachers:
            print(teacher.name)

        print("\nDirector:")
        print(self.director.name)
            
    
    
    def add_teachers_students_director(self, teachers, director, students):
        """
        Add teachers, director, and students to the school.

        Parameters:
            school (School): The school object to which to add the teachers, director, and students.
            teachers (list): A list of teacher objects to be added.
            director (Director): The director object to be added.
            students (list): A list of student objects to be added.

        """
        for teacher in teachers:
            self.add_teacher(teacher)
        
        self.add_director(director)
        
        for student in students:
            self.add_student(student)
