from info_class import info

class Director(info):
    assigned_schools = {}  # A dictionary for mapping schools to directors.

    def __init__(self, name, email, address, school_name):
        super().__init__(name, email, address)
        if school_name in Director.assigned_schools:
            raise ValueError(f"{school_name} already has a director.")
        self.school_name = school_name
        Director.assigned_schools[school_name] = self
        self.school_assigned = False  # Indicates whether a school is assigned.
        self.can_do_everything = True
        self.taught_disciplines = []

        

    def teach_discipline(self, discipline1, discipline2,  discipline3):
        self.taught_disciplines.extend([discipline1, discipline2,  discipline3])

    def exam_quest_list_teacher(self, *disciplines):
        for discipline in disciplines:
            exams = discipline.conduct_exams()
            for i, exam in enumerate(exams, start=1):
                print(f"{discipline.name} Exam {i} Questions:")
                for question in exam.exam_questions:
                    print(question[1])

    def assign_school(self, school_name):
        if not self.school_assigned:
            self.school_name = school_name
            self.school_assigned = True
        else:
            print(f"{self.name} is already assigned to a school.")

    def get_full_info(self):
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nSchool: {self.school_name}"
    
    