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
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"

class Secretary(info):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"

Student1 = Student("Dennis", "dennis.vonderstueck@grandcentrix.net", "boissereestraße 5 köln")
Teacher1 = Teacher("Müller", "müller@school.com", "Newroad 16 köln")
Secretary1 = Secretary("Schneider", "schneider@school.com", "japanroad 32 köln")
Director1 = Director("Müller", "müller@school.com", "googlestreet 2 köln")







