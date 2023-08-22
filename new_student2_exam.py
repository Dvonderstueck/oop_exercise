from info_class import info
from Student_class import Student
from classes_class import classes
from Discipline_class import Discipline
from Teacher_class import Teacher
from Director_class import Director
from Secretary_class import Secretary
from Exam_question_class import exam_question
from School_class import school
from Adress_class import adress
from Math_class import Math
from English_class import English
from Physics_class import Physics

address_instance = adress()

math_discipline = Math("Mathematics")
physics_discipline = Physics("Physics")
english_discipline = English("English")

exam1_math, exam2_math, exam3_math = math_discipline.conduct_exams()
exam1_english, exam2_english = english_discipline.conduct_exams()
exam1_physics, exam2_physics, exam3_physics = physics_discipline.conduct_exams()


new_student2 = Student("john", "max@example.com", address_instance.generate_random_address())

#Math exam 1
teacher_questions_exam1_math = exam1_math.exam_questions
user_inputs_exam1 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam1_math))

total_points_exam1_math = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam1):
     correct_answer = exam1_math.exam1_math_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam1_math += 3.35
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam1: {total_points_exam1_math}")
new_student2.add_grade(math_discipline.name, total_points_exam1_math)
new_student2.save_points_to_file(math_discipline.name, "exam1")

 #Math exam 2
teacher_questions_exam2_math = exam2_math.exam_questions
user_inputs_exam2 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam2_math))

total_points_exam2_math = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam2):
     correct_answer = exam2_math.exam2_math_exam_answer[i]
     if user_answer == correct_answer:
        print("Correct!")
        total_points_exam2_math += 3.35
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam2: {total_points_exam2_math}")
new_student2.add_grade(math_discipline.name, total_points_exam2_math)
new_student2.save_points_to_file(math_discipline.name, "exam2")

#Math exam3
teacher_questions_exam3_math = exam3_math.exam_questions
user_inputs_exam3 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam3_math))

total_points_exam3_math = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam3):
    correct_answer = exam3_math.exam3_math_exam_answer[i]
    if user_answer == correct_answer:
        print("Correct!")
        total_points_exam3_math += 3.35
    else:
        print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam3: {total_points_exam3_math}")
new_student2.add_grade(math_discipline.name, total_points_exam3_math)
new_student2.save_points_to_file(math_discipline.name, "exam3")



#English exam 1
teacher_questions_exam1_english = exam1_english.exam_questions
user_inputs_exam1 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam1_english))

total_points_exam1_english = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam1):
     correct_answer = exam1_english.exam1_english_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam1_english += 1.67
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam1: {total_points_exam1_english}")
new_student2.add_grade(english_discipline.name, total_points_exam1_english)
new_student2.save_points_to_file(english_discipline.name, "exam1")


#English exam 2
teacher_questions_exam2_english = exam2_english.exam_questions
user_inputs_exam2 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam2_english))

total_points_exam2_english = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam2):
     correct_answer = exam2_english.exam2_english_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam2_english += 1.67
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam2: {total_points_exam2_english}")
new_student2.add_grade(english_discipline.name, total_points_exam2_english)
new_student2.save_points_to_file(english_discipline.name, "exam2")


#physics exam 1
teacher_questions_exam1_physics = exam1_physics.exam_questions
user_inputs_exam1 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam1_physics))

total_points_exam1_physics = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam1):
     correct_answer = exam1_physics.exam1_physics_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam1_physics += 4
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam1: {total_points_exam1_physics}")
new_student2.add_grade(physics_discipline.name, total_points_exam1_physics)
new_student2.save_points_to_file(physics_discipline.name, "exam1")


#physics exam 2
teacher_questions_exam2_physics = exam2_physics.exam_questions
user_inputs_exam2 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam2_physics))

total_points_exam2_physics = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam2):
     correct_answer = exam2_physics.exam2_physics_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam2_physics += 4
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam2: {total_points_exam2_physics}")
new_student2.add_grade(physics_discipline.name, total_points_exam2_physics)
new_student2.save_points_to_file(physics_discipline.name, "exam2")


#physics exam 3
teacher_questions_exam3_physics = exam3_physics.exam_questions
user_inputs_exam3 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam3_physics))

total_points_exam3_physics = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam3):
     correct_answer = exam3_physics.exam3_physics_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam3_physics += 4
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam3: {total_points_exam3_physics}")
new_student2.add_grade(physics_discipline.name, total_points_exam3_physics)
new_student2.save_points_to_file(physics_discipline.name, "exam3")



final_grade_math = math_discipline.calculate_final_grade(total_points_exam1_math, total_points_exam2_math, total_points_exam3_math)
print(f"Final grade for {math_discipline.name}: {final_grade_math}")

final_grade_english = english_discipline.calculate_final_grade(total_points_exam1_english, total_points_exam2_english)
print(f"Final grade for {english_discipline.name}: {final_grade_english}")

final_grade_physics = physics_discipline.calculate_final_grade(total_points_exam1_physics, total_points_exam2_physics, total_points_exam3_physics)
print(f"Final grade for {physics_discipline.name}: {final_grade_physics}")

new_student2.add_final_grade(math_discipline.name, final_grade_math)
new_student2.add_final_grade(english_discipline.name, final_grade_english)
new_student2.add_final_grade(physics_discipline.name, final_grade_physics)

math_final_grade = new_student2.get_final_grade(math_discipline.name)
english_final_grade = new_student2.get_final_grade(english_discipline.name)
physics_final_grade = new_student2.get_final_grade(physics_discipline.name)

