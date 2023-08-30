from Discipline_class import Discipline
from Exam_question_class import exam_question
class English(Discipline):

    def __init__(self, name):
        self.name = name

    def calculate_final_grade(self, exam1_points, exam2_points):
        total_points = exam1_points + exam2_points 
        final_grade = total_points 
        return final_grade
    
    def ask_question(self, discipline, question_text):
        self.exam_questions.append((discipline, question_text))

    # def get_correct_answer(self, index):
    #  return self.exam1_english_exam_answer[index]
    
    def conduct_exams(self):
        exam1_english = exam_question()
        exam1_english.ask_question(self.name, "What is the simple past of go?")
        exam1_english.ask_question(self.name, "What is the simple past of make")
        exam1_english.ask_question(self.name, "What is the simple past of leave")

        exam2_english = exam_question()
        exam2_english.ask_question(self.name, "What is the opposite of the word of happy? ")
        exam2_english.ask_question(self.name, "What is the plural form of the word book ?")
        exam2_english.ask_question(self.name, "What is the past tense of the verb eat ?")

        return exam1_english, exam2_english