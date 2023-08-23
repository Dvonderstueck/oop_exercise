
from abc import ABC, abstractmethod

class par_exam_grade(ABC):
    @abstractmethod
    def read_file(self, filename):
        pass
