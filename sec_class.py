from info_class import info

class Secretary(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def get_final_grade_secretary(self, student, discipline_name):
        final_grade = student.get_final_grade(discipline_name)
        return final_grade

    def print_final_grade_via_secretary(self):
             final_grade_math = self.school_secretary.get_final_grade_secretary(self.new_student2, self.math_exam_list.name)
             print(f"Final grade for {self.math_exam_list.name} (via Secretary): {final_grade_math}")

             final_grade_english = self.school_secretary.get_final_grade_secretary(self.new_student2, self.english_exam_list.name)
             print(f"Final grade for {self.english_exam_list.name} (via Secretary): {final_grade_english}")

             final_grade_physics = self.school_secretary.get_final_grade_secretary(self.new_student2, self.physics_exam_list.name)
             print(f"Final grade for {self.physics_exam_list.name} (via Secretary): {final_grade_physics}")