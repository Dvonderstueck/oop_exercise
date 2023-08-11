class info:
    def __init__(self, name, email, address):
         self.name = name
         self.email = email
         self.address = address

class Student(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"

class Teacher(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"

class Director(info):
  assigned_schools = {}

  def __init__(self, name, email, address, school_name):
        super().__init__(name, email, address)
        if school_name in Director.assigned_schools:
            raise ValueError(f"{school_name} already has a director.")
        self.school_name = school_name
        Director.assigned_schools[school_name] = self
        self.school_assigned = False
        

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

Student1 = Student("Dennis", "dennis.vonderstueck@grandcentrix.net", "boissereestraße 5 köln")
Teacher1 = Teacher("Müller", "müller@school.com", "Newroad 16 köln")
Secretary1 = Secretary("Schneider", "schneider@school.com", "japanroad 32 köln")
Director1 = Director("Schmidt", "Schmidt@school.com", "googlestreet 2 köln", "Europaschule köln")
Director2 = Director("Smith", "Smith@school.com", "Smithstreet 6 köln", "Evt")

Director1.assign_school("Europaschule köln")
Director2.assign_school("Evt")

print(Director2.get_full_info())





