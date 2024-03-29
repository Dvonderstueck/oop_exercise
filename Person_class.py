
class Person:
    """
    A class for representing basic information about a person.

     Attributes:
        name (str): The name of the person.
        email (str): The email address of the person.
        address (str): The address of the person.

    Methods:
        get_full_info(self):
            Get a string representation of the person's full information.
     """
    
    def __init__(self, name, email, address):
         """
        Initialize an Info object with a name, email, and address.

        Para:
            name (str): The name of the person.
            email (str): The email address of the person.
            address (str): The address of the person.

        """
         self.name = name
         self.email = email
         self.address = address


    def set_specific_attributes(self, name, email, address):
        if isinstance(self, Person):
            self.name = name
            self.email = email
            self.address = address 


    def get_full_info(self):
         """
        Get a string representation of the person's full information.

        Returns:
            str: A string containing the person's name, email, and address.

        """
         return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"
    




