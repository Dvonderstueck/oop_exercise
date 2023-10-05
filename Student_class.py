from info_class import Person
import Parent_read_points

class Student(Person):
    """
    A class representing a student in a school.

    Attributes:
        name (str): The name of the student.
        email (str): The email address of the student.
        address (str): The address of the student.
        student_grades (dict): A dictionary to store the student's grades for different disciplines.
        assigned_classes (list): A list to store the classes assigned to the student.
        exam_data (dict): A dictionary to store the student's exam data for different exams.

    Methods:
        add_grade(self, discipline, grade):
            Add a grade for a specific discipline to the student's record.
            
        get_input(question):
            Get user input.
            
        get_final_grade(self, discipline_name):
            Get the final grade for a specific discipline.
            
        add_final_grade(self, discipline_name, final_grade):
            Add a final grade for a specific discipline to the student's record.
            
        get_exam_grades(self, discipline_name):
            Get the exam grades for a specific discipline.
            
        save_points_to_file(self, discipline, exam_name):
            Save the student's points for a specific discipline and exam to a file.
            
        read_exam_data(self, exam_names):
            Read exam data from files for a given list of exam names for this student.
    """

    def __init__(self, name, email, address):
        """
        Initialize a Student object.

        Parameters:
            name (str): The name of the student.
            email (str): The email address of the student.
            address (str): The address of the student.
        """
        super().__init__(name, email, address)
        self.student_grades = {}
        self.assigned_classes = []
        self.exam_data = {}

    def add_grade(self, discipline, grade):
        """
        Add a grade for a specific discipline to the student's record.

        Parameters:
            discipline (str): The name of the discipline.
            grade (float): The grade received for the discipline.
        """
        self.student_grades[discipline] = grade

    @staticmethod
    def get_input(question):
        """
        Get user input.

        Parameters:
            question (str): The question to display to the user.

        Returns:
            str: The user's input as a string.
        """
        return input(question)

    def get_final_grade(self, discipline_name):
        """
        Get the final grade for a specific discipline.

        Parameters:
            discipline_name (str): The name of the discipline.

        Returns:
            float or None: The final grade for the specified discipline, or None if not found.
        """
        return self.student_grades.get(discipline_name)

    def add_final_grade(self, discipline_name, final_grade):
        """
        Add a final grade for a specific discipline to the student's record.

        Parameters:
            discipline_name (str): The name of the discipline.
            final_grade (float): The final grade for the discipline.
        """
        self.student_grades[discipline_name] = final_grade

    def get_exam_grades(self, discipline_name):
        """
        Get the exam grades for a specific discipline.

        Parameters:
            discipline_name (str): The name of the discipline.

        Returns:
            float or None: The exam grades for the specified discipline, or None if not found.
        """
        return self.student_grades.get(discipline_name)

    def save_points_to_file(self, discipline, exam_name):
        """
        Save the student's points for a specific discipline and exam to a file.

        Parameters:
            discipline (str): The name of the discipline.
            exam_name (str): The name of the exam.
        """
        file_path = f"{self.name.lower()}_{discipline}_{exam_name}_saved_points.txt"
        new_points = self.student_grades.get(discipline, 0)

        try:
            with open(file_path, 'w') as file:
                file.write(f"Saved points for {discipline}: {new_points}\n")

            print(f"Total points for {discipline} in {exam_name} have been updated and saved to {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}. The data could not be saved.")

    def read_exam_data(self, exam_names):
        """
        Read exam data from files for a given list of exam names for this student.

        Parameters:
            exam_names (list of str): A list of exam names.

        Returns:
            dict: A dictionary where keys are exam names and values are exam data.
        """
        for exam_name in exam_names:
            data = Parent_read_points.read_file(filename=f"{self.name.lower()}_{exam_name}_saved_points.txt")
            self.exam_data[exam_name] = data
