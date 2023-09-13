

class ExamQuestion():
    """
    A class for managing and storing exam questions and answers for various disciplines.

    Attributes:
        exam_questions (list): A list to store exam questions as tuples of (discipline, question_text).
        Various attributes for correct answers to exam questions for different disciplines.

    Methods:
        ask_question(self, discipline, question_text):
            Add a question to the list of exam questions.

    """
     
    def __init__(self):
        """
        Initialize an ExamQuestion object with empty lists for exam questions and correct answers.

        """
        self.exam_questions = []
        self.exam2_mathematics_exam_answer = ["348", "568", "1005"]
        self.exam1_mathematics_exam_answer = ["5", "10", "103"]
        self.exam3_mathematics_exam_answer = ["10", "20", "203"]

        self.exam2_english_exam_answer = ["sad", "books", "ate"]
        self.exam1_english_exam_answer = ["went", "made", "left"]

        self.exam1_physics_exam_answer = ["gravity", "friction", "kinetic energy"]
        self.exam2_physics_exam_answer = ["potential energy", "seconds", "it decreases"]
        self.exam3_physics_exam_answer = ["static energy", "mass", "weight"]

    def ask_question(self, discipline, question_text):
        """
        Add a question to a exam list

        Para:
            discipline: The discipline of the exam
            question_text: The question that is added 
        """
        self.exam_questions.append((discipline, question_text))
