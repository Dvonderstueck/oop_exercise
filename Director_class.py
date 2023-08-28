
from info_class import info
class Director(info):
  
  
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




