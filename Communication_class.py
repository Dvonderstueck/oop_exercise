from Par_class import Parent
class Communication:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, message):
        self.messages.append({"sender": sender, "receiver": receiver, "message": message})

    def get_messages(self, user):
        received_messages = []
        for msg in self.messages:
            if msg["receiver"] == user:
                received_messages.append(msg)
        return received_messages

# Example usage
communication_system = Communication()

new_student1_parent = Parent("Lena", "Lena@gmail.com", "Boissereestraße 3, 50674 Köln")
new_student2_parent = Parent("Wolfgang", "Wolfgang@web.de", "Boissereestraße 4, 50674 Köln")
