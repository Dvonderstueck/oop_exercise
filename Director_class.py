from Person_class import Person

class Director(Person):
    """
    A class for representing a school director.

    Attributes:
        can_do_everything (bool): Indicates if the director has the authority to do everything.
        taught_disciplines (list): A list of disciplines that the director can teach.
        school (str): The name of the school to which the director is assigned.

    Methods:
        __init__(self, name, email, address, school_name=None):
            Initialize a Director object with name, email, address, and school assignment.
        teach_discipline(self, *disciplines):
            Assign disciplines that the director can teach.
        exam_quest_list_teacher(self, *disciplines):
            List exam questions for the assigned disciplines.
        assign_school(self, school_name):
            Assign the director to a school.
        get_full_info(self):
            Get a string representation of the director's full information.
    """

    def __init__(self, name, email, address):
        """
        Initialize a Director object with name, email, and address.

        Parameters:
            name (str): The name of the director.
            email (str): The email address of the director.
            address (str): The address of the director.

        """
        super().__init__(name, email, address)
        self.can_do_everything = True
        self.taught_disciplines = []
        self.school = None

    def teach_discipline(self, *disciplines):
        """
        Assign disciplines that the director can teach.

        Parameters:
            *disciplines (str): Variable number of disciplines to teach.

        """
        self.taught_disciplines.extend(disciplines)

    def exam_quest_list_teacher(self, *disciplines):
        """
        List exam questions for the assigned disciplines.

        Parameters:
            *disciplines (str): Variable number of disciplines to list exam questions for.

        """
        for discipline in disciplines:
            exams = discipline.conduct_exams()
            for i, exam in enumerate(exams, start=1):
                print(f"{discipline.name} Exam {i} Questions:")
                for discipline_name, question_text in exam.exam_questions:
                    if discipline.name == discipline_name:
                        print(question_text)
                print()

    def assign_school(self, school_name):
        """
        Assign the director to a school.

        Parameters:
            school_name (str): The name of the school to which the director is assigned.

        """
        self.school = school_name

    def get_full_info(self):
        """
        Get a string representation of the director's full information.

        Returns:
            str: A string containing the director's name, email, address, and school assignment.

        """
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nSchool: {self.school}"
