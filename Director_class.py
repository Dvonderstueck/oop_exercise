from info_class import Info



class Director(Info):
    """
    A class for representing a school director.

    Attributes:
        assigned_schools (dict): A dictionary to keep track of assigned school names and directors.

    Methods:
        __init__(self, name, email, address, school_name):
            Initialize a Director object with name, email, address, and school assignment.
        
        teach_discipline(self, discipline1, discipline2, discipline3):
            Assign disciplines that the director can teach.

        exam_quest_list_teacher(self, disciplines, discipline2, discipline3):
            List exam questions for the assigned disciplines.

        assign_school(self, school_name):
            Assign the director to a school.

        get_full_info(self):
            Get a string representation of the director's full information.

    """

    assigned_schools = {}

    def __init__(self, name, email, address, school):
        """
        Initialize a Director object with name, email, address, and school assignment.

        Para:
            name (str): The name of the director.
            email (str): The email address of the director.
            address (str): The address of the director.
            school_name (str): The name of the school to which the director is assigned.

        """
        super().__init__(name, email, address)
        self.school_name = school
        if school in Director.assigned_schools:
            raise ValueError(f"{school} already has a director.")

     


        Director.assigned_schools[school] = self
        self.school_assigned = False
        self.can_do_everything = True
        self.taught_disciplines = []


    def teach_discipline(self, discipline1, discipline2, discipline3):
        """
        Assign disciplines that the director can teach.

        Para:
            discipline1 (str): The first discipline to teach.
            discipline2 (str): The second discipline to teach.
            discipline3 (str): The third discipline to teach.

        """
        self.taught_disciplines.extend([discipline1, discipline2, discipline3])

    def exam_quest_list_teacher(self, disciplines, discipline2, discipline3):
        """
        List exam questions for the assigned disciplines.

        Para:
            disciplines (list): A list of disciplines.
            discipline2 (str): The second discipline to list exam questions for.
            discipline3 (str): The third discipline to list exam questions for.

        """
        for discipline in disciplines, discipline2, discipline3:
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

        Para:
            school_name (str): The name of the school to assign the director to.

        """
        if not self.school_assigned:
            self.school_name = school_name
            self.school_assigned = True
        else:
            print(f"{self.name} is already assigned to a school.")

    def get_full_info(self):
        """
        Get a string representation of the director's full information.

        Returns:
            str: A string containing the director's name, email, address, and school assignment.

         """
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nSchool: {self.school_name}"
    


    


    
    