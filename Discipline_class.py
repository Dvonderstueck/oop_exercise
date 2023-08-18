class Discipline:

    def __init__(self, name):
        self.name = name


    def calculate_final_grade(self, exam1_points, exam2_points, exam3_points):
        total_points = exam1_points + 2 * exam2_points + 3 * exam3_points
        final_grade = total_points / 6  # Divide by the sum of coefficients (1 + 2 + 3)
        return final_grade