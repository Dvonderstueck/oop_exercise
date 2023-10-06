from Student_class import Student
from classes_class import Classes
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
from sec_class import Secretary
import logging
from Adress_class import Address



class School:
    """
    School is a class representing a school institution.

    Attributes:
        name (str): The name of the school.
        students (list): A list to store student objects associated with the school.
        teachers (list): A list to store teacher objects associated with the school.
        director (Director): The director object associated with the school.
        taught_disciplines (list): A list to store the disciplines taught by the school.

    Methods:
        add_student(self, student): Add a student to the school.
        add_teacher(self, teacher): Add a teacher to the school.
        add_director(self, director): Add a director to the school.
        teach_discipline(self, discipline1, discipline2): Assign two disciplines to be taught by the school.
        print_students_teachers_and_director(self): Print the list of students, teachers, and the director associated with the school.
        add_teachers_students_director(self, teachers, students): Add teachers, director, and students to the school.
    """

   

    def __init__(self, name):
        """
        Initialize a School object.

        Parameters:
            name (str): The name of the school.
        """
        self.name = name
        self.students = []
        self.teachers = []
        self.secretary = None
        self.director = None
        self.taught_disciplines = set()

    
    def add_person(self, person):
        """
        Add a person to the school based on their class type.

        Parameters:
            person: The person object to be added to the school.
        """
        match person:
            case Student():
                self.__add_student(person)
            case Teacher():
                self.__add_teacher(person)
            case Director():
                self.__add_director(person)
            case Secretary():
                self.__add_secretary(person)
            case _:
                raise ValueError("Invalid person object. Expected Student, Teacher, Director, or Secretary.")


    def __add_student(self, student):
        """
        Add a student to the school.

        Parameters:
            student (Student): The student object to be added to the school's student list.
        """
        if isinstance(student, Student):
            self.students.append(student)

    def __str__(self):
        """
        Return a string representation of the school's name.

        Returns:
            str: The name of the school.
        """
        return self.name

    def __add_teacher(self, teacher):
        """
        Add a teacher to the school if not already present.

        Parameters:
            teacher (Teacher): The teacher object to be added to the school's teacher list.
        """
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)

    def __add_secretary(self, secretary ):

        if isinstance(secretary, Secretary):
            if self.secretary is None:
                self.secretary = secretary



    def __add_director(self, director):
        """
        Add a director to the school.

        Parameters:
            director (Director): The director object to be added to the school's director list.
        """
        if isinstance(director, Director):
            if self.director is None:
                self.director = director
                director.school = self
            else:
                raise ValueError(f"{self.name} already has a director: {self.director.name}")
        
        

    def teach_discipline(self, discipline1, discipline2):
        """
        Assign two disciplines to be taught by the school.

        Parameters:
            discipline1 (Discipline): The first discipline to be taught.
            discipline2 (Discipline): The second discipline to be taught.
        """
        self.taught_disciplines.add(discipline1)
        self.taught_disciplines.add(discipline2)

    def print_students_teachers_and_director(self):
        """
        Print the list of students, teachers, and the director associated with the school.
        """
        print("List of Students:", ", ".join(student.name for student in self.students))
        print("List of Teachers:", ", ".join(teacher.name for teacher in self.teachers))
        if self.director:
            print("Director:", self.director.name)
        if self.secretary:
            print("Secretary:", self.secretary.name)


    def add_teachers_students_director(self, teachers, students):
        """
        Add teachers, director, and students to the school.

        Parameters:
            teachers (list): A list of teacher objects to be added.
            students (list): A list of student objects to be added.
        """
        for teacher in teachers:
            self.add_teacher(teacher)
        for student in students:
            self.add_student(student)

    def remove_director(self, director):
        """
        Remove a director from the school.

        Para:
            director (Director): The director object to be removed from the school.
        """
        if self.director == director:
            self.director = None
            director.school = None
        else:
            raise ValueError(f"{self.name} does not have the specified director: {director.name}")




