from Par_class import par_exam_grade

class student1_par(par_exam_grade):
    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()
        
Max_par = student1_par()
math_exam1 = Max_par.read_file("max_Mathematics_exam1_saved_points.txt")
math_exam2 = Max_par.read_file("max_Mathematics_exam2_saved_points.txt")
math_exam3 = Max_par.read_file("max_Mathematics_exam3_saved_points.txt")

english_exam1 = Max_par.read_file("max_english_exam1_saved_points.txt")
english_exam2 = Max_par.read_file("max_english_exam2_saved_points.txt")

physics_exam1 = Max_par.read_file("max_Physics_exam1_saved_points.txt")
physics_exam2 = Max_par.read_file("max_Physics_exam2_saved_points.txt")
physics_exam3 = Max_par.read_file("max_Physics_exam3_saved_points.txt")
print(english_exam2)