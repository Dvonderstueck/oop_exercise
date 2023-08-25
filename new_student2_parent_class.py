from Par_class import par_exam_grade

class student2_par(par_exam_grade):
    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()
        
John_par = student2_par()
math_exam1 = John_par.read_file("john_Mathematics_exam1_saved_points.txt")
math_exam2 = John_par.read_file("john_Mathematics_exam2_saved_points.txt")
math_exam3 = John_par.read_file("john_Mathematics_exam3_saved_points.txt")

english_exam1 = John_par.read_file("john_english_exam1_saved_points.txt")
english_exam2 = John_par.read_file("john_english_exam2_saved_points.txt")

physics_exam1 = John_par.read_file("john_Physics_exam1_saved_points.txt")
physics_exam2 = John_par.read_file("john_Physics_exam2_saved_points.txt")
physics_exam3 = John_par.read_file("john_Physics_exam3_saved_points.txt")
print(english_exam2)