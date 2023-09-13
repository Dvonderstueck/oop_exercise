from Discipline_class import Discipline
from Exam_question_class import ExamQuestion

class Physics(Discipline):
    """
    A class of the school discipline of Physics

    Attributes:
        name (str): The name of the Discipline (Physics)


    Methods:
        def calculate_final_grade(self, exam1_points, exam2_points, exam3_points):
        Add a way to calculate the finla grade for physics

        def ask_question(self, discipline, question_text):
        Add a question to a exam list

        def get_correct_answer(self, index):
        Get the correct answer for a question at a specified index.

        def conduct_exams(self):
        Create and return three sets of exam questions for Physics.

    """

    def __init__(self, name):
        self.name = name

    def calculate_final_grade(self, exam1_points, exam2_points, exam3_points):
        """
        Add a way to calculate the finla grade for physics

        Para:
            exam1_points: The points from the first exam
            exam2_points: The points from the second exam
            exam3_points: The points from the third exam

        Returns:
           The final grade 
        """
        total_points = exam1_points + exam2_points + exam3_points
        final_grade = total_points / 3
        return final_grade
    

    def ask_question(self, discipline, question_text):
        """
        Add a question to a exam list

        Para:
            discipline: The discipline of the exam
            question_text: The question that is added 
        """
        self.exam_questions.append((discipline, question_text))

    def get_correct_answer(self, index):
        """
        Get the correct answer for a question at a specified index.

        Para:
            index (int): The index of the question.

        Returns:
            str: The correct answer to the question.

        """
        return self.exam1_physics_exam_answer[index]
    
    def conduct_exams(self):
        """
        Create and return three sets of exam questions for Physics.

        Returns:
            Tuple: Three sets of exam questions for Physics.

        """
        exam1_physics = ExamQuestion()
        exam1_physics.ask_question(self.name, "What is the force that pulls objects towards the center of the Earth called?")
        exam1_physics.ask_question(self.name, "If you push a toy car, what force makes it eventually come to a stop?")
        exam1_physics.ask_question(self.name, "What do we call the energy an object has due to its motion?")

        exam2_physics = ExamQuestion()
        exam2_physics.ask_question(self.name, "Which type of energy is associated with an object's position or height above the ground?")
        exam2_physics.ask_question(self.name, "What is the unit of measurement for time")
        exam2_physics.ask_question(self.name, "When an object's speed decreases, what happens to its kinetic energy?")

        exam3_physics = ExamQuestion()
        exam3_physics.ask_question(self.name, "What force allows a balloon to stick to a wall after rubbing it against your hair?")
        exam3_physics.ask_question(self.name, "What is the measure of the amount of matter in an object?")
        exam3_physics.ask_question(self.name, "What is the force exerted on an object due to gravity?")

        return exam1_physics, exam2_physics, exam3_physics

