from abc import ABC, abstractmethod
from info_class import Person

class Parent(Person):
    """
    A class of a Parent from a Student

    Attributes:
        name (str): The name of the parent.
        email (str): The email address of the parent.
        address (str): The address of the parent.

    """


    def __init__(self, name, email, address):
        """
        Initialize a Parent object.

        Para:
            name (str): The name of the parent.
            email (str): The email address of the parent.
            address (str): The address of the parent.

        """
        super().__init__(name, email, address)

class ParExamGrade(ABC):
    """
    A class rhat lets the parents know the grade of ther children

    Methods:
    @abstractmethod
    def read_file(self, filename):
        Abstract method to read a file and return its contents.


    """
    
    @abstractmethod
    def read_file(self, filename):
        """
        Abstract method to read a file and return its contents.

        Para:
            filename (str): The name of the file to be read.

        Returns:
            str: The contents of the file.

        """
        pass

new_student1_parent = Parent("Lena", "Lena@gmail.com", "Boissereestraße 13, 50674 Köln")
new_student2_parent = Parent("Wolfgang", "Wolfgang@web.de", "Boissereestraße 14, 50674 Köln")
