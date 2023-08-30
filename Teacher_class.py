from info_class import info
from Math_class import Math
from English_class import English
from Physics_class import Physics
from Discipline_class import Discipline
from Adress_class import adress

address_instance = adress()

math_exam_list = Math("Mathematics")  
english_exam_list = English("English")
physics_exam_list = Physics("Physics")

class Teacher(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.taught_disciplines = []  # A list of taught disciplines.
         
       

    def teach_discipline(self, discipline1, discipline2):
        self.taught_disciplines.extend([discipline1, discipline2])

    def exam_quest_list_teacher(self, *disciplines):
        for discipline in disciplines:
            exams = discipline.conduct_exams()
            for i, exam in enumerate(exams, start=1):
                print(f"{discipline.name} Exam {i} Questions:")
                for question in exam.exam_questions:
                    print(question[1])
                print()




math_teacher = Teacher("Lukas", "Lukas@school.com", address_instance.generate_random_address())
english_teacher = Teacher("Nina", "Nina@school.com", address_instance.generate_random_address())
physics_teacher = Teacher("Tommy", "Tommy@school.com", address_instance.generate_random_address())


math_teacher.teach_discipline(math_exam_list,physics_exam_list)
english_teacher.teach_discipline(english_exam_list,math_exam_list)
physics_teacher.teach_discipline(physics_exam_list,physics_exam_list)




               
        
        
        

    

            