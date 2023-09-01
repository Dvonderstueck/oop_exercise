
class classes:
    def __init__(self, name):
        self.name = name
        self.disciplines = []
        self.students = []
        self.teachers = []
        self.directors = []
        

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def list_disciplines(self):
        return self.disciplines
    
    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def print_students_teachers_and_director(self):
        print("List of Students:")
        for student in self.school.students:
            print(student.name)

        print("\nList of Teachers:")
        for teacher in self.school.teachers:
            print(teacher.name)

        print("\nDirector:")
        for director in self.school.directors:
            print(director.name)

    def teachers_and_students(self):
                self.school.add_teacher(self.math_teacher)
                self.school.add_teacher(self.english_teacher)
                self.school.add_teacher(self.physics_teacher)
                self.school.add_Director(self.director1)
                self.school.add_student(self.new_student1)
                self.school.add_student(self.new_student2)
    
  