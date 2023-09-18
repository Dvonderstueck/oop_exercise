from info_class import Info


class Secretary(Info):
    """
    A class to represent a secretary of a school

    Attributes:
        name (str): The name of the secretary.
        email (str): The email address of the secretary.
        address (str): The address of the secretary.

    Methods:    
        get_final_grade_secretary(self, student, discipline_name):
        Get the final grade for a specific discipline of a student via the secretary.

        print_final_grade_via_secretary(self):
        Print the final grades for different disciplines of a student via the secretary.



    """

    def __init__(self, name, email, address):
        """
        Initialize a Secretary object.

        Para:
            name (str): The name of the secretary.
            email (str): The email address of the secretary.
            address (str): The address of the secretary.

        """
        super().__init__(name, email, address)

    def get_final_grade_secretary(self, student, discipline_name):
        """
        Get the final grade for a specific discipline of a student via the secretary.

        Para:
            student (Student): The student object for which the final grade is to be retrieved.
            discipline_name (str): The name of the discipline.

        Returns:
            float or None: The final grade for the specified discipline of the student, or None if not found.

        """
        final_grade = student.get_final_grade(discipline_name)
        return final_grade

    def print_final_grade_via_secretary(self):
        """
        Print the final grades for different disciplines of a student via the secretary.

        """
        final_grade_math = self.school_secretary.get_final_grade_secretary(self.new_student2, self.math_exam_list.name)
        print(f"Final grade for {self.math_exam_list.name} (via Secretary): {final_grade_math}")

        final_grade_english = self.school_secretary.get_final_grade_secretary(self.new_student2, self.english_exam_list.name)
        print(f"Final grade for {self.english_exam_list.name} (via Secretary): {final_grade_english}")

        final_grade_physics = self.school_secretary.get_final_grade_secretary(self.new_student2, self.physics_exam_list.name)
        print(f"Final grade for {self.physics_exam_list.name} (via Secretary): {final_grade_physics}")
