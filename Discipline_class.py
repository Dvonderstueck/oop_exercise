class Discipline:

    def __init__(self, name):
        self.name = name

    def calculate_final_grade(self, exam_scores):
        if self.name == "Mathematics":
            return (exam_scores[0] + 2 * exam_scores[1] + 3 * exam_scores[2]) / 6
        elif self.name == "English":
            return (exam_scores[0] + exam_scores[1]) / 2
        elif self.name == "Physics":
            return sum(exam_scores) / 3 / 4  # Calculate average and divide by 4
  