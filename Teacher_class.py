from info_class import info
class Teacher(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.taught_disciplines = []  # A list of taught disciplines.
         
       

    def teach_discipline(self, discipline):
        self.taught_disciplines.append(discipline)

    
   # exam_questions_math = [] 
   # exam_questions_english = [] 
   # exam_questions_physics = [] 
            