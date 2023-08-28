
from Director_class import Director
from Adress_class import adress
class SchoolUtils:
 
    def teach(person, subject):
        print(f"{person.name} is teaching {subject}")

address_instance = adress()
director1 = Director("Schmidt", "Schmidt@school.com", address_instance.generate_random_address(), "")
SchoolUtils.teach(director1, "math")