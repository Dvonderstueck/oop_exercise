
class classes:
    def __init__(self, name):
        self.name = name
        self.disciplines = []
        self.students = []
        self.teachers = []
        

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def list_disciplines(self):
        return self.disciplines
    
    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def setup_and_print(self, *disciplines):
        for discipline in disciplines:
            self.add_discipline(discipline)
        disciplines_info = ", ".join(self.list_disciplines())
        return f"Class: {self.name}\nDisciplines: {disciplines_info}\n"