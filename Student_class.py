from info_class import Info

class Student(Info):

    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.student_grades = {}
        self.assigned_classes = []

    def add_grade(self, discipline, grade):
        self.student_grades[discipline] = grade

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

        new_points = self.student_grades.get(discipline, 0)

        with open(file_path, 'w') as file:
            file.write(f"Saved points for {discipline}: {new_points}\n")

        print(f"Total points for {discipline} in {exam_name} have been updated and saved to {file_path}")
