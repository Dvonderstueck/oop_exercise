from Adress_class import adress
from Math_class import Math
from English_class import English
from Physics_class import Physics
from Student_class import Student
from Exam_question_class import exam_question

def calculate_and_add_final_grade(student, discipline_instance, exam_results):
    discipline_exam_results = [(name, num, points) for name, num, points in exam_results if name == discipline_instance.name]
    final_grade = discipline_instance.calculate_final_grade(*[points for name, num, points in discipline_exam_results])
    student.add_final_grade(discipline_instance.name, final_grade)
    print(f"Final grade for {discipline_instance.name}: {final_grade}")

def exams_for_student(student_instance):
    address_instance = adress()

    math_discipline = Math("Mathematics")
    physics_discipline = Physics("Physics")
    english_discipline = English("English")

    exam_results = []

    disciplines = [math_discipline, physics_discipline, english_discipline]

    discipline_point_values = {
        "Mathematics": 3.35,
        "Physics": 4,
        "English": 1.67,
    }

    for discipline_instance in disciplines:
        exams = discipline_instance.conduct_exams()

        for exam_num, exam in enumerate(exams, start=1):
            correct_answer_attr = getattr(exam, f'exam{exam_num}_{discipline_instance.name.lower()}_exam_answer')
            exam_questions = exam.exam_questions

            points_earned = 0
            user_inputs = list(map(lambda q: (q[0], q[1], student_instance.get_input(f"{q[0]} - {q[1]}: ")), exam_questions))

            for i, (discipline, question_info, user_inputs,) in enumerate(user_inputs):
                correct_answer = correct_answer_attr[i]
                if user_inputs == correct_answer:
                    print("Correct!")
                    points_earned += discipline_point_values[discipline_instance.name]
                else:
                    print("Incorrect. The correct answer is:", correct_answer)

            print(f"Total points earned in this exam: {discipline_point_values[discipline_instance.name]}")
            exam_results.append((discipline_instance.name, exam_num, points_earned))
            student_instance.add_grade(discipline_instance.name, points_earned)
            student_instance.save_points_to_file(discipline_instance.name, f"exam{exam_num}")

    for discipline_instance in disciplines:
        calculate_and_add_final_grade(student_instance, discipline_instance, exam_results)

    return student_instance

address_instance = adress()