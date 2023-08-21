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

address_instance = adress()

math_discipline = Discipline("Mathematics")
physics_discipline = Discipline("Physics")
english_discipline = Discipline("English")

exam1_math = exam_question()
exam1_math.ask_question(math_discipline.name, "What is 2+3?")
exam1_math.ask_question(math_discipline.name, "What is 5+5?")
exam1_math.ask_question(math_discipline.name, "What is 100+3?")

exam2_math = exam_question()
exam2_math.ask_question(math_discipline.name, "What is 345+3?")
exam2_math.ask_question(math_discipline.name, "What is 563+5?")
exam2_math.ask_question(math_discipline.name, "What is 1002+3?")

exam3_math = exam_question()
exam3_math.ask_question(math_discipline.name, "What is 7+3?")
exam3_math.ask_question(math_discipline.name, "What is 15+5?")
exam3_math.ask_question(math_discipline.name, "What is 200+3?")

exam1_english = exam_question()
exam1_english.ask_question(english_discipline.name, "What is the simple past of go?")
exam1_english.ask_question(english_discipline.name, "What is the simple past of make")
exam1_english.ask_question(english_discipline.name, "What is the simple past of leave")

exam2_english = exam_question()
exam2_english.ask_question(english_discipline.name, "What is the opposite of the word of happy? ")
exam2_english.ask_question(english_discipline.name, "What is the plural form of the word book ?")
exam2_english.ask_question(english_discipline.name, "What is the past tense of the verb eat ?")

exam1_physics = exam_question()
exam1_physics.ask_question(physics_discipline.name, "What is the force that pulls objects towards the center of the Earth called?")
exam1_physics.ask_question(physics_discipline.name, "If you push a toy car, what force makes it eventually come to a stop?")
exam1_physics.ask_question(physics_discipline.name, "What do we call the energy an object has due to its motion?")

exam2_physics = exam_question()
exam2_physics.ask_question(physics_discipline.name, "Which type of energy is associated with an object's position or height above the ground?")
exam2_physics.ask_question(physics_discipline.name, "What is the unit of measurement for time")
exam2_physics.ask_question(physics_discipline.name, "When an object's speed decreases, what happens to its kinetic energy?")

exam3_physics = exam_question()
exam3_physics.ask_question(physics_discipline.name, "What force allows a balloon to stick to a wall after rubbing it against your hair?")
exam3_physics.ask_question(physics_discipline.name, "What is the measure of the amount of matter in an object?")
exam3_physics.ask_question(physics_discipline.name, "What is the force exerted on an object due to gravity?")

new_student2 = Student("john", "max@example.com", address_instance.generate_random_address())

#Math exam 1
teacher_questions_exam1_math = exam1_math.exam_questions
user_inputs_exam1 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam1_math))

total_points_exam1 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam1):
     correct_answer = exam1_math.exam1_math_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam1 += 4
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam1: {total_points_exam1}")
new_student2.add_grade(math_discipline.name, total_points_exam1)
new_student2.save_points_to_file(math_discipline.name, "exam1")

 #Math exam 2
teacher_questions_exam2_math = exam2_math.exam_questions
user_inputs_exam2 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam2_math))

total_points_exam2 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam2):
     correct_answer = exam2_math.exam2_math_exam_answer[i]
     if user_answer == correct_answer:
        print("Correct!")
        total_points_exam2 += 4
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam2: {total_points_exam2}")
new_student2.add_grade(math_discipline.name, total_points_exam2)
new_student2.save_points_to_file(math_discipline.name, "exam2")

#Math exam3
teacher_questions_exam3_math = exam3_math.exam_questions
user_inputs_exam3 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam3_math))

total_points_exam3 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam3):
    correct_answer = exam3_math.exam3_math_exam_answer[i]
    if user_answer == correct_answer:
        print("Correct!")
        total_points_exam3 += 4
    else:
        print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam3: {total_points_exam3}")
new_student2.add_grade(math_discipline.name, total_points_exam3)
new_student2.save_points_to_file(math_discipline.name, "exam3")



#English exam 1
teacher_questions_exam1_english = exam1_english.exam_questions
user_inputs_exam1 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam1_english))

total_points_exam1 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam1):
     correct_answer = exam1_english.exam1_english_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam1 += 2
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam1: {total_points_exam1}")
new_student2.add_grade(english_discipline.name, total_points_exam1)
new_student2.save_points_to_file(english_discipline.name, "exam1")


#English exam 2
teacher_questions_exam2_english = exam2_english.exam_questions
user_inputs_exam2 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam2_english))

total_points_exam2 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam2):
     correct_answer = exam2_english.exam2_english_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam2 += 2
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam2: {total_points_exam2}")
new_student2.add_grade(english_discipline.name, total_points_exam2)
new_student2.save_points_to_file(english_discipline.name, "exam2")


#physics exam 1
teacher_questions_exam1_physics = exam1_physics.exam_questions
user_inputs_exam1 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam1_physics))

total_points_exam1 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam1):
     correct_answer = exam1_physics.exam1_physics_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam1 += 4
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam1: {total_points_exam1}")
new_student2.add_grade(physics_discipline.name, total_points_exam1)
new_student2.save_points_to_file(physics_discipline.name, "exam1")


#physics exam 2
teacher_questions_exam2_physics = exam2_physics.exam_questions
user_inputs_exam2 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam2_physics))

total_points_exam2 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam2):
     correct_answer = exam2_physics.exam2_physics_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam2 += 4
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam2: {total_points_exam2}")
new_student2.add_grade(physics_discipline.name, total_points_exam2)
new_student2.save_points_to_file(physics_discipline.name, "exam2")


#physics exam 3
teacher_questions_exam3_physics = exam3_physics.exam_questions
user_inputs_exam3 = list(map(lambda q: (q[0], q[1], new_student2.get_input(f"{q[0]} - {q[1]}: ")), teacher_questions_exam3_physics))

total_points_exam3 = 0

for i, (discipline, question_info, user_answer) in enumerate(user_inputs_exam3):
     correct_answer = exam3_physics.exam3_physics_exam_answer[i]
     if user_answer == correct_answer:
         print("Correct!")
         total_points_exam3 += 4
     else:
         print("Incorrect. The correct answer is:", correct_answer)

print(f"Total points earned in exam3: {total_points_exam3}")
new_student2.add_grade(physics_discipline.name, total_points_exam3)
new_student2.save_points_to_file(physics_discipline.name, "exam3")



final_grade_math = math_discipline.calculate_final_grade_math(total_points_exam1, total_points_exam2, total_points_exam3)
print(f"Final grade for {math_discipline.name}: {final_grade_math}")

final_grade_english = english_discipline.calculate_final_grade_english(total_points_exam1, total_points_exam2)
print(f"Final grade for {english_discipline.name}: {final_grade_english}")

final_grade_physics = physics_discipline.calculate_final_grade_physics(total_points_exam1, total_points_exam2, total_points_exam3)
print(f"Final grade for {physics_discipline.name}: {final_grade_physics}")

new_student2.add_final_grade(math_discipline.name, final_grade_math)
new_student2.add_final_grade(english_discipline.name, final_grade_english)
new_student2.add_final_grade(physics_discipline.name, final_grade_physics)

math_final_grade = new_student2.get_final_grade(math_discipline.name)
english_final_grade = new_student2.get_final_grade(english_discipline.name)
physics_final_grade = new_student2.get_final_grade(physics_discipline.name)

