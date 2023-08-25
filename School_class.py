from Communication_class import Communication
from Student_class import Student
from classes_class import classes   
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
#from Secretary_class import Secretary
import sec_class
from Exam_question_class import exam_question
from Adress_class import adress
from Schooluitils_class import SchoolUtils
#from new_student1_exam import final_grade_math
import test123
from Par_class import Parent


communication_system = Communication()


address_instance = adress()
class School:
    def __init__(self, name,):
        self.name = name
        self.adress = address_instance
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
       # print(f"{student.name} has been added to {self.name}")
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.adress}"
    
    

    


school = School("Europa Schule köln")


math_teacher = Teacher("Lukas", "max@school.com", address_instance.generate_random_address())
school_secretary = sec_class.Secretary("Jenny", "secretary@school.com", address_instance.generate_random_address())  
new_student1 = Student("Max", "max@example.com", address_instance.generate_random_address())
new_student2 = Student("john", "max@example.com", address_instance.generate_random_address())
director1 = Director("Schmidt", "Schmidt@school.com", address_instance.generate_random_address(), "Europaschule köln")
parent_instance = Parent("Lena", "Lena@gmail.com", "Boissereestraße 3, 50674 Köln")




school.add_teacher(math_teacher)

school.add_student(new_student1)
school.add_student(new_student2)

math_discipline = Discipline("Mathematics")
physics_discipline = Discipline("Physics")
english_discipline = Discipline("English")

math_teacher.teach_discipline(math_discipline.name,)
math_teacher.teach_discipline(physics_discipline.name)

class1 = classes("class 1")
class2 = classes("class 2")  
class1.add_discipline(math_discipline.name)
class1.add_discipline(physics_discipline.name)
class2.add_discipline(english_discipline.name) 
class_info = [class1, class2]

selected_students = [new_student1]
selected_teachers = [math_teacher]

for student in selected_students:
    class1.add_student(student)
for teacher in selected_teachers:
    class1.add_teacher(teacher)



#new_student2 = test123.exams_for_student(new_student2)

#final_grade_math = school_secretary.get_final_grade_secretary(new_student2, math_discipline.name)
#print(f"Final grade for {math_discipline.name} (via Secretary): {final_grade_math}")

#final_grade_english = school_secretary.get_final_grade_secretary(new_student2, english_discipline.name)
#print(f"Final grade for {english_discipline.name} (via Secretary): {final_grade_english}")

###final_grade_physics = school_secretary.get_final_grade_secretary(new_student2, physics_discipline.name)
####print(f"Final grade for {physics_discipline.name} (via Secretary): {final_grade_physics}")




#for student in school.students:    
   # print(student.name)


   # for class_obj in class_info:
    #  print(class_obj.setup_and_print())
     
#      print("Teachers:")
#      for teacher in class_obj.teachers:
#          print(teacher.name)
#      print("Students:")
#      for student in class_obj.students:
#          print(student.name)
#      print()

#print(new_student2.get_full_info())


teacher_name = "John Doe"
parent_name = parent_instance
message = "Your child's performance has improved."
communication_system.send_message(teacher_name, parent_name, message)

# Parent checks received messages
parent_received_messages = communication_system.get_messages(parent_name)
for msg in parent_received_messages:
    print(f"From: {msg['sender']}\nMessage: {msg['message']}")

#for teacher in school.teachers:
   # print(teacher.name)
#SchoolUtils.teach(director1, "Management")