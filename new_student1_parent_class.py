from Par_class import par_exam_grade

class student1_par(par_exam_grade):
    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()
        
John_par = student1_par()
data = John_par.read_file("john_Mathematics_exam1_saved_points.txt")
print(data)