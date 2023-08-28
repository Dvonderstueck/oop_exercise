from info_class import info
from Math_class import Math
from English_class import English
from Physics_class import Physics
from Discipline_class import Discipline

math_exam_list = Math("Mathematics")  
english_exam_list = English("English")
physics_exam_list = Physics("Physics")

class Teacher(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.taught_disciplines = []  # A list of taught disciplines.
         
       

    def teach_discipline(self, discipline):
        self.taught_disciplines.append(discipline)

    def exam_quest_list_teacher(self, *disciplines):
        for discipline in disciplines:
            exams = discipline.conduct_exams()
            for i, exam in enumerate(exams, start=1):
                print(f"{discipline.name} Exam {i} Questions:")
                for question in exam.exam_questions:
                    print(question[1])
                print()


math_exam_list = Math("Mathematics")
english_exam_list = English("English")
physics_exam_list = Physics("Physics")


teacher = Teacher("John Doe", "john@example.com", "123 Main St")


teacher.teach_discipline(math_exam_list)
teacher.teach_discipline(english_exam_list)
teacher.teach_discipline(physics_exam_list)


teacher.exam_quest_list_teacher(math_exam_list, english_exam_list, physics_exam_list)

               
        
        
        

    

            