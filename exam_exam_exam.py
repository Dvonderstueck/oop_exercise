from Exam_question_class import exam_question
import test123
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

new_student2 = test123.exams_for_student(new_student2)

final_grade_math = school_secretary.get_final_grade_secretary(new_student2, math_discipline.name)
print(f"Final grade for {math_discipline.name} (via Secretary): {final_grade_math}")

final_grade_english = school_secretary.get_final_grade_secretary(new_student2, english_discipline.name)
print(f"Final grade for {english_discipline.name} (via Secretary): {final_grade_english}")

final_grade_physics = school_secretary.get_final_grade_secretary(new_student2, physics_discipline.name)
print(f"Final grade for {physics_discipline.name} (via Secretary): {final_grade_physics}")