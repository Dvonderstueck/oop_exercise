
class info:
    def __init__(self, name, email, address):
         self.name = name
         self.email = email
         self.address = address

    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"


class classes:
    def __init__(self, name):
        self.name = name
        self.disciplines = []
        

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def list_disciplines(self):
        return self.disciplines
    
    def setup_and_print(self, *disciplines):
        for discipline in disciplines:
            self.add_discipline(discipline)
        disciplines_info = ", ".join(self.list_disciplines())
        return f"Class: {self.name}\nDisciplines: {disciplines_info}\n"
      



class Student(info):

    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.student_grades = {}
        self.assigned_classes = []

    
    def add_grade(self, discipline, grade):
        self.student_grades[discipline] = grade

    def assign_class(self, class_name):
        if class_name not in self.assigned_classes:
            self.assigned_classes.append(class_name)
        else:
            print(f"{self.name} is already assigned to {class_name}.")
    
    def get_input(question):
        return input(question)

     

    
    def get_grade(self):
     return f"Teacher: {Teacher1.name}\nGrade: {self.student_grades}"
    
     
    
#saves disciplines
class Discipline:
    def __init__(self, name):
        self.name = name


class add_question: #maybe change it to a method in teacher??
    def __init__(self, question):
        self.exam_questions.append(question)


class Teacher(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.taught_disciplines = []  # A list of taught disciplines.
          # A list of exam questions
       

    def teach_discipline(self, discipline):
        self.taught_disciplines.append(discipline)


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


class exam_question(): 
    def __init__(self):
        self.exam_questions = []
        self.exam2_math_exam_answer = ["348", "568", "1005"]
        self.exam1_math_exam_answer = ["5", "10", "103"]
        

    def ask_question(self, discipline, question_text):
        self.exam_questions.append((discipline, question_text))

    def list_exam_questions(self):
        exam_questions_info = ""
        for discipline, question_text in self.exam_questions:
            exam_questions_info += f"Discipline: {discipline}\nQuestion: {question_text}\n\n"
        return exam_questions_info


    
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
Student1.assign_class("class 1")
Student1.assign_class("class 2")

Teacher1.teach_discipline(math_discipline.name,)
Teacher1.teach_discipline(physics_discipline.name)



exam1 = exam_question()  
exam1.ask_question(math_discipline.name, "What is 2+3?")
exam1.ask_question(math_discipline.name, "What is 5+5?")
exam1.ask_question(math_discipline.name, "What is 100+3?")

exam2 = exam_question()  
exam2.ask_question(math_discipline.name, "What is 345+3?")
exam2.ask_question(math_discipline.name, "What is 563+5?")
exam2.ask_question(math_discipline.name, "What is 1002+3?")

Student1.add_grade(math_discipline.name, 85)

class1 = classes("class 1")
class2 = classes("class 2")  
class1.add_discipline(math_discipline.name)
class1.add_discipline(physics_discipline.name)
class2.add_discipline(english_discipline.name) 
class_info = [class1, class2]

class1.setup_and_print()
class2.setup_and_print()

# Use map() to get user inputs for teacher questions
teacher_questions = exam1.exam_questions
user_inputs = list(map(lambda q: Student.get_input(q[1]), teacher_questions))

for i, (question_info, user_answer) in enumerate(zip(teacher_questions, user_inputs)):
    correct_answer = question_info
    if user_answer == exam1.exam1_math_exam_answer[i]:  # Compare with the correct answer from Teacher1_math_exam_answer
       print("Correct!")
    else:
        print("Incorrect. The correct answer is:", exam1.exam1_math_exam_answer[i])





#for class_obj in class_info:
    #print(class_obj.setup_and_print())

#print(Student1.get_full_info())
#print("Disciplines in class1:", class1.list_disciplines())

#print(Student1.get_grade())








