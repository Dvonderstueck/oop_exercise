from info_class import info
class Student(info):

    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.student_grades = {}
        self.assigned_classes = []

    
    def add_grade(self, discipline, grade):
        self.student_grades[discipline] = grade

    def assign_class(self, class_name):
        if class_name not in self.assigned_classes:
            self.assigned_classes.append(class_name)
        else:
            print(f"{self.name} is already assigned to {class_name}.")
    
    def get_input(question):
        return input(question)

     

    
    #def get_grade(self):
   #  return f"Teacher: {Teacher1.name}\nGrade: {self.student_grades}"