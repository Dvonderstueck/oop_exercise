from info_class import info
from Student_class import Student
from classes_class import classes   
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
from Secretary_class import Secretary
from Exam_question_class import exam_question

    
math_discipline = Discipline("Mathematics")
physics_discipline = Discipline("Physics")
english_discipline = Discipline("English")

Student1 = Student("Dennis", "dennis.vonderstueck@grandcentrix.net", "boissereestraße 5 köln")
Teacher1 = Teacher("Müller", "müller@school.com", "Newroad 16 köln")
Secretary1 = Secretary("Schneider", "schneider@school.com", "japanroad 32 köln")
Director1 = Director("Schmidt", "Schmidt@school.com", "googlestreet 2 köln", "Europaschule köln")
Director2 = Director("Smith", "Smith@school.com", "Smithstreet 6 köln", "Evt")


Director1.assign_school("Europaschule köln")
Director2.assign_school("Evt")
Student1.assign_class("class 1")
Student1.assign_class("class 2")

Teacher1.teach_discipline(math_discipline.name,)
Teacher1.teach_discipline(physics_discipline.name)



exam1 = exam_question()  
exam1.ask_question(math_discipline.name, "What is 2+3?")
exam1.ask_question(math_discipline.name, "What is 5+5?")
exam1.ask_question(math_discipline.name, "What is 100+3?")

exam2 = exam_question()  
exam2.ask_question(math_discipline.name, "What is 345+3?")
exam2.ask_question(math_discipline.name, "What is 563+5?")
exam2.ask_question(math_discipline.name, "What is 1002+3?")


Student1.add_grade(math_discipline.name, 85)

class1 = classes("class 1")
class2 = classes("class 2")  
class1.add_discipline(math_discipline.name)
class1.add_discipline(physics_discipline.name)
class2.add_discipline(english_discipline.name) 
class_info = [class1, class2]

class1.setup_and_print()
class2.setup_and_print()

# Use map() to get user inputs for teacher questions
teacher_questions = exam1.exam_questions
user_inputs = list(map(lambda q: (q[0], q[1], Student.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions))  # Create a list of tuples containing discipline, question text, and user answer for each question.

for i, (discipline, question_info, user_answer) in enumerate(user_inputs):
    correct_answer = exam1.exam1_math_exam_answer[i]
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", correct_answer)




#for class_obj in class_info:
    #print(class_obj.setup_and_print())

#print(Student1.get_full_info())
#print("Disciplines in class1:", class1.list_disciplines())

#print(Student1.get_grade())








