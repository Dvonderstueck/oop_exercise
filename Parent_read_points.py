
def read_file(filename):
    """
    Read and return the contents of a file.

    Para:
        filename (str): The name of the file to be read.

    Returns:
        str: The contents of the file.
    """
    with open(filename, "r") as f:
        return f.read()

def read_exam_data(exam_names, student_number):
    """
    Read exam data from files for a given list of exam names and student number.

    Para:
        exam_names (list): A list of exam names.
        student_number (int): 1 for Student1, 2 for Student2.

    Returns:
        dict: A dictionary where keys are exam names and values are exam data.
    """
    exam_data = {}
    for exam_name in exam_names:
        data = read_file(f"{'max' if student_number == 1 else 'john'}_{exam_name}_saved_points.txt")
        exam_data[exam_name] = data
    return exam_data

def read_student_points(exam_names, student_number):
    """
    Read exam points for a student from various exams.

    Args:
        exam_names (list): A list of exam names.
        student_number (int): 1 for Student1, 2 for Student2.

    Returns:
        dict: A dictionary where keys are exam names and values are exam data.
    """
    return read_exam_data(exam_names, student_number)

def read_student1_points():
    exam_names_math = ["Mathematics_exam1", "Mathematics_exam2", "Mathematics_exam3"]
    exam_names_english = ["english_exam1", "english_exam2"]
    exam_names_physics = ["Physics_exam1", "Physics_exam2", "Physics_exam3"]

    exam_names_student1 = exam_names_math + exam_names_english + exam_names_physics

    return read_student_points(exam_names_student1, student_number=1)

def read_student2_points():
    exam_names_math = ["Mathematics_exam1", "Mathematics_exam2", "Mathematics_exam3"]
    exam_names_english = ["english_exam1", "english_exam2"]
    exam_names_physics = ["Physics_exam1", "Physics_exam2", "Physics_exam3"]

    exam_names_student2 = exam_names_math + exam_names_english + exam_names_physics

    return read_student_points(exam_names_student2, student_number=2)
