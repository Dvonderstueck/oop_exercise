from Math_class import Math
from English_class import English
from Physics_class import Physics

def calculate_and_add_final_grade(student, discipline_instance, exam_results):
    """
    Calculate and add the final grade for a student in a specific discipline based on exam results.

    Args:
        student (Student): The student object for which the final grade is calculated and added.
        discipline_instance (Discipline): The discipline instance for which the final grade is calculated.
        exam_results (list): A list of exam results as tuples (discipline_name, exam_num, points_earned).
    """
    discipline_name = discipline_instance.name
    discipline_exam_results = [(name, num, points) for name, num, points in exam_results if name == discipline_name]
    final_grade = discipline_instance.calculate_final_grade(*[points for _, _, points in discipline_exam_results])
    student.add_final_grade(discipline_name, final_grade)
    print(f"Final grade for {discipline_name}: {final_grade}")

def conduct_single_exam(exam, exam_num, discipline_instance, student_instance, discipline_point_values):
    """
    Conduct a single exam, evaluate answers, and calculate points earned.

    Para:
        exam (ExamQuestion): The exam instance containing questions.
        exam_num (int): The exam number.
        discipline_instance (Discipline): The discipline instance for which the exam is conducted.
        student_instance (Student): The student taking the exam.
        discipline_point_values (dict): A dictionary mapping discipline names to point values.

    Returns:
        tuple: A tuple containing (discipline_name, exam_num, points_earned).

    """
    correct_answer_attr = getattr(exam, f'exam{exam_num}_{discipline_instance.name.lower()}_exam_answer')
    exam_questions = exam.exam_questions

    points_earned = 0

    for i, (discipline, question_info) in enumerate(exam_questions):
        correct_answer = correct_answer_attr[i]
        user_input = student_instance.get_input(f"{discipline} - {question_info}: ")

        if user_input == correct_answer:
            print("Correct!")
            points_earned += discipline_point_values[discipline_instance.name]
        else:
            print("Incorrect. The correct answer is:", correct_answer)

    if points_earned > 0:
        print(f"Total points earned in this exam: {points_earned}")

    return (discipline_instance.name, exam_num, points_earned)


def conduct_exams(student_instance, disciplines, discipline_point_values):
    """
    Conduct exams for a student in multiple disciplines and calculate points earned.

    Args:
        student_instance (Student): The student taking the exams.
        disciplines (list): A list of Discipline instances for the exams.
        discipline_point_values (dict): A dictionary mapping discipline names to point values.

    Returns:
        list: A list of exam results as tuples (discipline_name, exam_num, points_earned).
    """
    exam_results = []

    for discipline_instance in disciplines:
        exams = discipline_instance.conduct_exams()

        for exam_num, exam in enumerate(exams, start=1):
            exam_result = conduct_single_exam(exam, exam_num, discipline_instance, student_instance, discipline_point_values)
            exam_results.append(exam_result)
            student_instance.add_grade(discipline_instance.name, exam_result[2])
            student_instance.save_points_to_file(discipline_instance.name, f"exam{exam_num}")

    return exam_results

def exams_for_student(student_instance):
    """
    Conduct exams for a student in multiple disciplines, calculate final grades, and save points to files.

    Args:
        student_instance (Student): The student taking the exams.

    Returns:
        Student: The student object with final grades and saved points.
    """
    disciplines = [Math("Mathematics"), Physics("Physics"), English("English")]

    discipline_point_values = {
        "Mathematics": 3.4,
        "Physics": 3.35,
        "English": 1.67,
    }

    exam_results = conduct_exams(student_instance, disciplines, discipline_point_values)

    for discipline_instance in disciplines:
        calculate_and_add_final_grade(student_instance, discipline_instance, exam_results)

    return student_instance
