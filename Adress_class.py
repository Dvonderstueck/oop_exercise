class Address:
    """
    A class for generating random addresses in Cologne.

    Attributes:
        address_list (list): A list to store generated addresses.

    Methods:
        generate_random_address(cls):
            Generate a random address without creating an object.
            
            Returns:
                str: A randomly generated address in the format "Boissereestraße <number>, 50674 Köln".
    """

    address_list = []  

    @classmethod
    def generate_random_address(cls):
        """
        Generate a random address without creating an object.

        Returns:
            str: A randomly generated address in the format "Boissereestraße <number>, 50674 Köln".
        """
        random_address = f"Boissereestraße {len(cls.address_list) + 1}, 50674 Köln"
        cls.address_list.append(random_address)
        return random_address
