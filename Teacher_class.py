from info_class import info
class Teacher(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.taught_disciplines = []  # A list of taught disciplines.
         
       

    def teach_discipline(self, discipline):
        self.taught_disciplines.append(discipline)

    
    def create_exam(self, discipline, questions):
        if discipline in self.taught_disciplines:
            self.exam_questions[discipline] = questions
        else:
            print(f"{self.name} doesn't teach {discipline}.")
            