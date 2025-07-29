class Mail:
    def __init__(self,sender,receiver,subject,content):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content
        self.tag = []
        self.spam = False

    def __str__(self):
        
        return (
            f"sender: {self.sender}\n"
            f"Receiver: {self.receiver}\n"
            f"Suject: {self.subject}\n"
            f"content: {self.content}\n"
            f"tag: {self.tag}\n"
            f"spam: {self.spam}\n"
        )



