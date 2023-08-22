from abc import ABC, abstractmethod
class Discipline(ABC):
   def __init__(self, name):
         super().__init__()
         self.name = name


@abstractmethod
def calculate_final_grade(self,exam):
         pass