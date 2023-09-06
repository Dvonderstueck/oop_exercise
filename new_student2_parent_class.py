from Par_class import ParExamGrade


class Student2Par(ParExamGrade):

    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()

student2 = Student2Par()

class Student2ExamPoints:

    @staticmethod
    def read_exam_data(exam_names):
        exam_data = {}
        
        for exam_name in exam_names:
            data = student2.read_file(f"john_{exam_name}_saved_points.txt")
            exam_data[exam_name] = data
        
        return exam_data
    
    def read_student2_points(self):
        self.student2_exam_points1 = Student2ExamPoints.math_exam_data
        self.student2_exam_points2 = Student2ExamPoints.english_exam_data
        self.student2_exam_points3 = Student2ExamPoints.physics_exam_data

    exam_names_math = ["Mathematics_exam1", "Mathematics_exam2", "Mathematics_exam3"]
    exam_names_english = ["english_exam1", "english_exam2"]
    exam_names_physics = ["Physics_exam1", "Physics_exam2", "Physics_exam3"]

    math_exam_data = read_exam_data(exam_names_math)
    english_exam_data = read_exam_data(exam_names_english)
    physics_exam_data = read_exam_data(exam_names_physics)
