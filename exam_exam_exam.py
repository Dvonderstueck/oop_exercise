from Exam_question_class import exam_question
import Exam_class
from Student_class import Student
from Discipline_class import Discipline
from Adress_class import adress
import sec_class

address_instance = adress()

new_student1 = Student("Max", "max@example.com", address_instance.generate_random_address())
new_student2 = Student("john", "max@example.com", address_instance.generate_random_address())
school_secretary = sec_class.Secretary("Jenny", "secretary@school.com", address_instance.generate_random_address())  

math_discipline = Discipline("Mathematics")
physics_discipline = Discipline("Physics")
english_discipline = Discipline("English")