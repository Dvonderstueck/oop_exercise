from Par_class import ParExamGrade


class Student1Par(ParExamGrade):
    """
    A class for the parent of student2 

    Attributes:
        exam_names_math (list): A list of exam names related to Mathematics.
        exam_names_english (list): A list of exam names related to English.
        exam_names_physics (list): A list of exam names related to Physics.
        math_exam_data (dict): A dictionary where keys are exam names(These keys are used to access the corresponding exam data.), and values are exam data for Mathematics.
        english_exam_data (dict): A dictionary where keys are exam names(These keys are used to access the corresponding exam data.), and values are exam data for English.
        physics_exam_data (dict): A dictionary where keys are exam names(These keys are used to access the corresponding exam data.), and values are exam data for Physics.


    Methods:
    read_file(self, filename)
        Read and return the contents of a file.

    @staticmethod
    read_exam_data(exam_names):
        Read exam data from files for a given list of exam names.

    read_student1_points(self):
        Read exam points for Student1 from various exams.

    


    """

    def read_file(self, filename):
        """
        Read and return the contents of a file.

        Para:
            filename (str): The name of the file to be read.

        Returns:
            str: The contents of the file.

        """
        with open(filename, "r") as f:
            return f.read()

student1 = Student1Par()


class Student1ExamPoints:

    @staticmethod
    def read_exam_data(exam_names):
        """
        Read exam data from files for a given list of exam names.

        Para:
            exam_names (list): A list of exam names.

        Returns:
            dict: A dictionary where keys are exam names and values are exam data.

        """
        exam_data = {}
        
        for exam_name in exam_names:
            data = student1.read_file(f"max_{exam_name}_saved_points.txt")
            exam_data[exam_name] = data
        
        return exam_data
    
    def read_student1_points(self):
        """
        Read exam points for Student1 from various exams.

        """
        self.student1_exam_points1 = Student1ExamPoints.math_exam_data
        self.student1_exam_points2 = Student1ExamPoints.english_exam_data
        self.student1_exam_points3 = Student1ExamPoints.physics_exam_data

    exam_names_math = ["Mathematics_exam1", "Mathematics_exam2", "Mathematics_exam3"]
    exam_names_english = ["english_exam1", "english_exam2"]
    exam_names_physics = ["Physics_exam1", "Physics_exam2", "Physics_exam3"]

    math_exam_data = read_exam_data(exam_names_math)
    english_exam_data = read_exam_data(exam_names_english)
    physics_exam_data = read_exam_data(exam_names_physics)


