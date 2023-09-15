from Discipline_class import Discipline
from Exam_question_class import ExamQuestion


class English(Discipline):
    """
    A class of the school discipline of English

    Attributes:
        name (str): The name of the Discipline (English)


    Methods:
        calculate_final_grade(self, exam1_points, exam2_points, exam3_points):
        Add a way to calculate the finla grade for English

        ask_question(self, discipline, question_text):
        Add a question to a exam list

        get_correct_answer(self, index):
        Get the correct answer for a question at a specified index.

        conduct_exams(self):
        Create and return three sets of exam questions for English.

    """

    def __init__(self, name):
        self.name = name

    def calculate_final_grade(self, exam1_points, exam2_points):
        """
        Add a way to calculate the finla grade for English

        Para:
            exam1_points: The points from the first exam
            exam2_points: The points from the second exam
            exam3_points: The points from the third exam

        Returns:
           The final grade 
        """
        total_points = exam1_points + exam2_points 
        final_grade = total_points 
        return final_grade
    

    
    def conduct_exams(self):
        """
        Create and return three sets of exam questions for English.

        Returns:
            Tuple: Three sets of exam questions for English.

        """
        exam1_english = ExamQuestion()
        exam1_english.ask_question(self.name, "What is the simple past of go?")
        exam1_english.ask_question(self.name, "What is the simple past of make")
        exam1_english.ask_question(self.name, "What is the simple past of leave")

        exam2_english = ExamQuestion()
        exam2_english.ask_question(self.name, "What is the opposite of the word of happy? ")
        exam2_english.ask_question(self.name, "What is the plural form of the word book ?")
        exam2_english.ask_question(self.name, "What is the past tense of the verb eat ?")

        return exam1_english, exam2_english