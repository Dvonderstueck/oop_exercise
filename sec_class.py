from info_class import info

class Secretary(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def get_final_grade_secretary(self, student, discipline_name):
        final_grade = student.get_final_grade(discipline_name)
        return final_grade
