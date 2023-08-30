from Par_class import par_exam_grade

class student2_par(par_exam_grade):
    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()
        

student2 = student2_par()

class Student2_exam_points:
    def read_exam_data(exam_names):
        exam_data = {}
        
        for exam_name in exam_names:
            data = student2.read_file(f"john_{exam_name}_saved_points.txt")
            exam_data[exam_name] = data
        
        return exam_data

    exam_names_math = ["Mathematics_exam1", "Mathematics_exam2", "Mathematics_exam3"]
    exam_names_english = ["english_exam1", "english_exam2"]
    exam_names_physics = ["Physics_exam1", "Physics_exam2", "Physics_exam3"]

    math_exam_data = read_exam_data(exam_names_math)
    english_exam_data = read_exam_data(exam_names_english)
    physics_exam_data = read_exam_data(exam_names_physics)




