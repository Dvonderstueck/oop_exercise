from Discipline_class import Discipline
from Exam_question_class import ExamQuestion


class Math(Discipline):

    def __init__(self, name):
        self.name = name

    def calculate_final_grade(self, exam1_points, exam2_points, exam3_points):
        total_points = exam1_points + 2.0 * exam2_points + 3.0 * exam3_points
     
        final_grade = total_points / 6.0  
        return final_grade
    
   
    
    def conduct_exams(self):
        exam1_math = ExamQuestion()
        exam1_math.ask_question(self.name, "What is 2+3?")
        exam1_math.ask_question(self.name, "What is 5+5?")
        exam1_math.ask_question(self.name, "What is 100+3?")

        exam2_math = ExamQuestion()
        exam2_math.ask_question(self.name, "What is 345+3?")
        exam2_math.ask_question(self.name, "What is 563+5?")
        exam2_math.ask_question(self.name, "What is 1002+3?")

        exam3_math = ExamQuestion()
        exam3_math.ask_question(self.name, "What is 7+3?")
        exam3_math.ask_question(self.name, "What is 15+5?")
        exam3_math.ask_question(self.name, "What is 200+3?")

        return exam1_math, exam2_math, exam3_math







