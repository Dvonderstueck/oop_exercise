

class Adress:
    """
    A class for generating random addresses in Cologne.

    Attributes:
        adress_list (list): A list to store generated addresses.

    Methods:
        __init__(self):
            Initialize an Adress object.

        generate_random_address(self):
            Generate a random address and store it in the address list.

    """
    
    def __init__(self):
        """
        Initialize an Adress object.

        """
        self.adress_list = []
    
    def generate_random_address(self):
        """
        Generate a random address and store it in the address list.

        Returns:
            str: A randomly generated address in the format "Boissereestraße <number>, 50674 Köln".

        """
        random_address = f"Boissereestraße {len(self.adress_list) + 1}, 50674 Köln"
        self.adress_list.append(random_address)
        return random_address

