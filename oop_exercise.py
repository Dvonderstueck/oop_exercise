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

exam3 = exam_question()
exam3.ask_question(math_discipline.name, "What is 7+3?")
exam3.ask_question(math_discipline.name, "What is 15+5?")
exam3.ask_question(math_discipline.name, "What is 200+3?")


#Student1.add_grade(math_discipline.name, 85)

class1 = classes("class 1")
class2 = classes("class 2")
class1.add_discipline(math_discipline.name)
class1.add_discipline(physics_discipline.name)
class2.add_discipline(english_discipline.name)
class_info = [class1, class2]

class1.setup_and_print()
class2.setup_and_print()

teacher_questions_exam1 = exam1.exam_questions
user_inputs_exam1 = list(map(lambda q: (q[0], q[1], Student1.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam1))

total_points_exam1 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam1):
     correct_answer = exam1.exam1_math_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam1 += 1
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam1: {total_points_exam1}")
Student1.add_grade(math_discipline.name, total_points_exam1)
Student1.save_points_to_file(math_discipline.name, "exam1")

 # Process exam2
teacher_questions_exam2 = exam2.exam_questions
user_inputs_exam2 = list(map(lambda q: (q[0], q[1], Student1.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam2))

total_points_exam2 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam2):
     correct_answer = exam2.exam2_math_exam_answer[i]
     if user_answer == correct_answer:
        print("Correct!")
        total_points_exam2 += 1
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam2: {total_points_exam2}")
Student1.add_grade(math_discipline.name, total_points_exam2)
Student1.save_points_to_file(math_discipline.name, "exam2")

teacher_questions_exam3 = exam3.exam_questions
user_inputs_exam3 = list(map(lambda q: (q[0], q[1], Student1.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam3))

total_points_exam3 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam3):
   correct_answer = exam3.exam3_math_exam_answer[i]
   if user_answer == correct_answer:
        print("Correct!")
        total_points_exam3 += 1
else:
        print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam3: {total_points_exam3}")
Student1.add_grade(math_discipline.name, total_points_exam3)

# Save points earned in exam3 to the student's file
Student1.save_points_to_file(math_discipline.name, "exam3")

final_grade_math = math_discipline.calculate_final_grade(total_points_exam1, total_points_exam2, total_points_exam3)
print(f"Final grade for {math_discipline.name}: {final_grade_math}")













#for class_obj in class_info:
    #print(class_obj.setup_and_print())

#print(Student1.get_full_info())
#print("Disciplines in class1:", class1.list_disciplines())

#print(Student1.get_grade())








