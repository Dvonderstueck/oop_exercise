class info:
    def __init__(self, name, email, address):
         self.name = name
         self.email = email
         self.address = address

    def get_full_info(self):
     return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"