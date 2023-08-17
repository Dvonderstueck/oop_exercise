
from Student_class import Student
from classes_class import classes   
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
from Secretary_class import Secretary
from Exam_question_class import exam_question



class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
       # print(f"{student.name} has been added to {self.name}")
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    


school = School("Europa Schule köln")

math_teacher = Teacher("Lukas", "max@example.com", "123 Main St")

new_student1 = Student("Max", "max@example.com", "123 Main St")
new_student2 = Student("john", "max@example.com", "123 Main St")

school.add_teacher(math_teacher)

school.add_student(new_student1)
school.add_student(new_student2)

math_discipline = Discipline("Mathematics")
physics_discipline = Discipline("Physics")
english_discipline = Discipline("English")

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

#for student in school.students:
    #print(student.name)


for class_obj in class_info:
    print(class_obj.setup_and_print())
    print("Teachers:")
    for teacher in class_obj.teachers:
        print(teacher.name)
    print("Students:")
    for student in class_obj.students:
        print(student.name)
    print()


#for teacher in school.teachers:
   # print(teacher.name)
