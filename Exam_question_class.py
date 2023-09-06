class ExamQuestion():
     
    def __init__(self):
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
        self.exam_questions.append((discipline, question_text))
