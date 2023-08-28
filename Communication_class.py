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


communication_system = Communication()

new_student1_parent = Parent("Lena", "Lena@gmail.com", "Boissereestraße 3, 50674 Köln")
new_student2_parent = Parent("Wolfgang", "Wolfgang@web.de", "Boissereestraße 4, 50674 Köln")


teacher_name = "Lukas"
parent_name = new_student1_parent
message = "Your child's performance has improved."
communication_system.send_message(teacher_name, parent_name, message)

# Parent checks received messages
parent_received_messages = communication_system.get_messages(parent_name)
for msg in parent_received_messages:
    print(f"From: {msg['sender']}\nMessage: {msg['message']}")
