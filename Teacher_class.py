from info_class import Person
from Math_class import Math
from English_class import English
from Physics_class import Physics
from Adress_class import Address


math_exam_list = Math("Mathematics")  
english_exam_list = English("English")
physics_exam_list = Physics("Physics")


class Teacher(Person):
    """
    A class of a Teacher of a school

    Attributes:
        name (str): The name of the teacher.
        email (str): The email address of the teacher.
        address (str): The address of the teacher.
        taught_disciplines (list): A list to store the disciplines taught by the teacher.

    Methods:
        teach_discipline(self, discipline1, discipline2):
        Assign two disciplines to be taught by the teacher.

        exam_quest_list_teacher(self, disciplines):
        Print exam questions for the disciplines taught by the teacher.

        list_teacher_disciplines(self):
        Print the disciplines taught by the teacher.

    """
    
    def __init__(self, name, email, address):
        """
        Initialize a Teacher object.

        Para:
            name (str): The name of the teacher.
            email (str): The email address of the teacher.
            address (str): The address of the teacher.

        Attributes:
            taught_disciplines (list): A list to store the disciplines taught by the teacher.

        """
        super().__init__(name, email, address)
        self.taught_disciplines = []

    def teach_discipline(self, discipline1, discipline2):
        """
        Assign two disciplines to be taught by the teacher.

        Para:
            discipline1 (object): The first discipline to be taught.
            discipline2 (object): The second discipline to be taught.

        """
        self.taught_disciplines.extend([discipline1, discipline2])

    def exam_quest_list_teacher(self, disciplines):
        """
        Print exam questions for the disciplines taught by the teacher.

        Para:
            disciplines (list): A list of disciplines to retrieve exam questions for.

        """
        for discipline in disciplines:
            exams = discipline.conduct_exams()
            for i, exam in enumerate(exams, start=1):
                print(f"{discipline.name} Exam {i} Questions:")
                for discipline_name, question_text in exam.exam_questions:
                    if discipline.name == discipline_name: 
                        print(question_text)
                print()

    def list_teacher_disciplines(self):
        """
        Print the disciplines taught by the teacher.

        """
        print(f"{self.name}'s Taught Disciplines:")
        for discipline in self.taught_disciplines:
            print(discipline.name)


math_teacher = Teacher("Lukas", "Lukas@school.com", Address.generate_random_address())
english_teacher = Teacher("Nina", "Nina@school.com", Address.generate_random_address())
physics_teacher = Teacher("Tommy", "Tommy@school.com", Address.generate_random_address())


math_teacher.teach_discipline(math_exam_list, physics_exam_list)
english_teacher.teach_discipline(english_exam_list, math_exam_list)
physics_teacher.teach_discipline(physics_exam_list, physics_exam_list)


print()
