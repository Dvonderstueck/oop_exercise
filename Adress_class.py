import random
class adress:
    def __init__(self):
        self.adress_list = []
    
    def generate_random_address(self):
        random_address = f"Boissereestraße {len(self.adress_list) + 1}, 50674 Köln"
        self.adress_list.append(random_address)
        return random_address

