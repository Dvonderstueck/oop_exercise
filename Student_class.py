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
    
    @staticmethod
    def get_input(question):  
        return input(question)
    
    def get_final_grade(self, discipline_name):
        return self.student_grades.get(discipline_name)  

    def add_final_grade(self, discipline_name, final_grade):
        self.student_grades[discipline_name] = final_grade 

    def get_exam_grades(self, discipline_name):
        return self.student_grades.get(discipline_name)
    
    def save_points_to_file(self, discipline, exam_name):
        file_path = f"{self.name}_{discipline}_{exam_name}_saved_points.txt"
        
        # Read existing points from the file (if it exists)
        existing_points = 0
        try:
            with open(file_path, 'r') as file:
                existing_line = file.readline()
                existing_points = int(existing_line.split(': ')[-1].strip())
        except FileNotFoundError:
            pass
        
        new_points = self.student_grades.get(discipline, 0)
        total_points = existing_points + new_points
        
       
        with open(file_path, 'a') as file:  
            file.write(f"Saved points for {discipline}: {total_points}\n")
        
        print(f"Total points for {discipline} in {exam_name} have been updated and saved to {file_path}")

     


    
   # def get_grade(self):
   # return f"Teacher: {Teacher1.name}\nGrade: {self.student_grades}"