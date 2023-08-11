
class info:
    def __init__(self, name, email, address):
         self.name = name
         self.email = email
         self.address = address




class Student(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        

        self.student_grades = {}  # Ein leeres Dictionary zur Speicherung der Noten.

    def add_grade(self, discipline, grade):
        self.student_grades[discipline] = grade # Füge die Note zur entsprechenden Disziplin hinzu.

    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"
    

class Discipline:
    def __init__(self, name):
        self.name = name


class add_question:
    def __init__(self, question):
        self.exam_questions.append(question)


class Teacher(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.taught_disciplines = [] # Eine Liste der unterrichteten Disziplinen.
        self.exam_questions = []  # Eine Liste von Prüfungsfragen

    def teach_discipline(self, discipline):
        self.taught_disciplines.append(discipline) # Füge die unterrichtete Disziplin hinzu.


    def question(self, question_text):
        self.exam_questions.append(question_text) # Füge eine Prüfungsfrage hinzu.


    def get_full_info(self):
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"


class Director(Teacher):
  assigned_schools = {} # Ein Dictionary zur Zuordnung von Schulen zu Schulleitern.

  def __init__(self, name, email, address, school_name):
        super().__init__(name, email, address)
        if school_name in Director.assigned_schools:
            raise ValueError(f"{school_name} already has a director.")
        self.school_name = school_name
        Director.assigned_schools[school_name] = self
        self.school_assigned = False # Zeigt an, ob eine Schule zugewiesen wurde.
        

  def assign_school(self, school_name):
     if not self.school_assigned:
            self.school_name = school_name
            self.school_assigned = True
     else:
            print(f"{self.name} is already assigned to a school.")


  def get_full_info(self):
      return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nSchool: {self.school_name}"


class Secretary(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"
    
math_discipline = Discipline("Mathematics")
physics_discipline = Discipline("Physics")
english_discipline = Discipline("English")

Student1 = Student("Dennis", "dennis.vonderstueck@grandcentrix.net", "boissereestraße 5 köln")
Teacher1 = Teacher("Müller", "müller@school.com", "Newroad 16 köln")
Secretary1 = Secretary("Schneider", "schneider@school.com", "japanroad 32 köln")
Director1 = Director("Schmidt", "Schmidt@school.com", "googlestreet 2 köln", "Europaschule köln")
Director2 = Director("Smith", "Smith@school.com", "Smithstreet 6 köln", "Evt")

Director1.assign_school("Europaschule köln")
Director2.assign_school("Evt")

Teacher1.teach_discipline(math_discipline.name,)
Teacher1.teach_discipline(physics_discipline.name)

Teacher1.question("what is 1+1")
Student1.add_grade(math_discipline.name, 85)

##print("Student1 has the grade: ",Student1.student_grades, "by the Teacher", Teacher1.name)






