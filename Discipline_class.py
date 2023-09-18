from abc import ABC, abstractmethod


class Discipline(ABC):
   """
    An abstract base class for representing school disciplines.

    Attributes:
        name (str): The name of the discipline.

    Methods:
        calculate_final_grade(self, exam):
            Abstract method to calculate the final grade for the discipline.

    """
   
   def __init__(self, name):
         """
        Initialize a Discipline object with a name.

        Args:
            name (str): The name of the discipline.

        """
         super().__init__()
         self.name = name


@abstractmethod
def calculate_final_grade(self,exam):
         """
        Abstract method to calculate the final grade for the discipline.

        Para:
            exam (object): The exam object associated with the discipline.

        """
         pass