from info_class import info
from Student_class import Student
from classes_class import classes   
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
from Secretary_class import Secretary
from Exam_question_class import exam_question
from School_class import school

    
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


# Use map() to get user inputs for teacher questions
teacher_questions = exam1.exam_questions
user_inputs = list(map(lambda q: (q[0], q[1], Student.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions))  # Create a list of tuples containing discipline, question text, and user answer for each question.

total_points = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs):
    correct_answer = exam1.exam1_math_exam_answer[i]
    if user_answer == correct_answer:
          print("Correct!")
          total_points += 1
          Student1.add_grade(discipline, total_points)
    else:
          print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned: {total_points}")

saved_points = Student1.student_grades.get(math_discipline.name, 0)

 # Get saved points for the math discipline
print(f"Saved points for {math_discipline.name}: {saved_points}")

# Save the saved points to a text document for Student1 and math discipline
Student1.save_points_to_file(math_discipline.name)




#print(Student1.get_full_info())
#print("Disciplines in class1:", class1.list_disciplines())

#print(Student1.get_grade())








