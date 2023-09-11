# Import necessary class from corresponding module
from info_class import Info

# Define a Student class that inherits from the Info class
class Student(Info):

    def __init__(self, name, email, address):
        """
        Initialize a Student object.

        Args:
            name (str): The name of the student.
            email (str): The email address of the student.
            address (str): The address of the student.

        Attributes:
            student_grades (dict): A dictionary to store the student's grades for different disciplines.
            assigned_classes (list): A list to store the classes assigned to the student.

        """
        super().__init__(name, email, address)
        self.student_grades = {}
        self.assigned_classes = []

    def add_grade(self, discipline, grade):
        """
        Add a grade for a specific discipline to the student's record.

        Args:
            discipline (str): The name of the discipline.
            grade (float): The grade received for the discipline.

        """
        self.student_grades[discipline] = grade

    @staticmethod
    def get_input(question):
        """
        Get user input.

        Args:
            question (str): The question to display to the user.

        Returns:
            str: The user's input as a string.

        """
        return input(question)

    def get_final_grade(self, discipline_name):
        """
        Get the final grade for a specific discipline.

        Args:
            discipline_name (str): The name of the discipline.

        Returns:
            float or None: The final grade for the specified discipline, or None if not found.

        """
        return self.student_grades.get(discipline_name)

    def add_final_grade(self, discipline_name, final_grade):
        """
        Add a final grade for a specific discipline to the student's record.

        Args:
            discipline_name (str): The name of the discipline.
            final_grade (float): The final grade for the discipline.

        """
        self.student_grades[discipline_name] = final_grade

    def get_exam_grades(self, discipline_name):
        """
        Get the exam grades for a specific discipline.

        Args:
            discipline_name (str): The name of the discipline.

        Returns:
            float or None: The exam grades for the specified discipline, or None if not found.

        """
        return self.student_grades.get(discipline_name)

    def save_points_to_file(self, discipline, exam_name):
        """
        Save the student's points for a specific discipline and exam to a file.

        Args:
            discipline (str): The name of the discipline.
            exam_name (str): The name of the exam.

        """
        file_path = f"{self.name}_{discipline}_{exam_name}_saved_points.txt"

        new_points = self.student_grades.get(discipline, 0)

        with open(file_path, 'w') as file:
            file.write(f"Saved points for {discipline}: {new_points}\n")

        print(f"Total points for {discipline} in {exam_name} have been updated and saved to {file_path}")

    print(save_points_to_file.__doc__)
