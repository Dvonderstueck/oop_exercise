
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

    def print_students_and_teachers(self):
        print("List of Students:")
        for student in self.school.students:
            print(student.name)

        print("\nList of Teachers:")
        for teacher in self.school.teachers:
            print(teacher.name)
    
  