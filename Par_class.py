from abc import ABC, abstractmethod
from info_class import info

class Parent(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address) 

class par_exam_grade(ABC):
    @abstractmethod
    def read_file(self, filename):
        pass

new_student1_parent = Parent("Lena", "Lena@gmail.com", "Boissereestraße 3, 50674 Köln")
new_student2_parent = Parent("Wolfgang", "Wolfgang@web.de", "Boissereestraße 4, 50674 Köln")


