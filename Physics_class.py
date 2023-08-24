from Discipline_class import Discipline
from Exam_question_class import exam_question
class Physics(Discipline):

    def __init__(self, name):
        self.name = name

    def calculate_final_grade(self, exam1_points, exam2_points, exam3_points):
        total_points = exam1_points + exam2_points + exam3_points
        final_grade = total_points / 3
        return final_grade
    
    def ask_question(self, discipline, question_text):
        self.exam_questions.append((discipline, question_text))

    def get_correct_answer(self, index):
     return self.exam1_physics_exam_answer[index]
    
    def conduct_exams(self):
        exam1_physics = exam_question()
        exam1_physics.ask_question(self.name, "What is the force that pulls objects towards the center of the Earth called?")
        exam1_physics.ask_question(self.name, "If you push a toy car, what force makes it eventually come to a stop?")
        exam1_physics.ask_question(self.name, "What do we call the energy an object has due to its motion?")

        exam2_physics = exam_question()
        exam2_physics.ask_question(self.name, "Which type of energy is associated with an object's position or height above the ground?")
        exam2_physics.ask_question(self.name, "What is the unit of measurement for time")
        exam2_physics.ask_question(self.name, "When an object's speed decreases, what happens to its kinetic energy?")

        exam3_physics = exam_question()
        exam3_physics.ask_question(self.name, "What force allows a balloon to stick to a wall after rubbing it against your hair?")
        exam3_physics.ask_question(self.name, "What is the measure of the amount of matter in an object?")
        exam3_physics.ask_question(self.name, "What is the force exerted on an object due to gravity?")


        return exam1_physics, exam2_physics, exam3_physics