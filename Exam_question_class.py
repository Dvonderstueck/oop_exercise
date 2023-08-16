class exam_question(): 
    def __init__(self):
        self.exam_questions = []
        self.exam2_math_exam_answer = ["348", "568", "1005"]
        self.exam1_math_exam_answer = ["5", "10", "103"]
        

    def ask_question(self, discipline, question_text):
        self.exam_questions.append((discipline, question_text))

    def list_exam_questions(self):
        exam_questions_info = ""
        for discipline, question_text in self.exam_questions:
            exam_questions_info += f"Discipline: {discipline}\nQuestion: {question_text}\n\n"
        return exam_questions_info
    
