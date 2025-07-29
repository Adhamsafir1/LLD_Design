# System.py
from Mail import Mail
class System:
    def __init__(self):
        self.mails =[]
        self.spam = ["Wow" , "Hurry" , "Congrats"]

    def addmail(self,sender,receiver,subject,content):
        mail = Mail(sender,receiver,subject,content)
        self.isSpam(content,mail)
        self.mails.append(mail)
        return

    def isSpam(self,content,mail):
        words = list(content.split(" "))
        for word in words:
            if word in self.spam:
                mail.spam = True
                break
        return

    def add_tag(self,id,tags):
        self.mails[id].tag.append(tags)
        return

    def printAllMail(self):
        for mail in self.mails:
            print(mail)
        return

    def WildCard(self,word):
        for mail in self.mails:
            if word in mail.content:
                print(mail)
        return

    def search(self, word):
        print(f"Searching for '{word}' in all mails:")
        for mail in self.mails:
            if (word in mail.sender or word in mail.receiver or word in mail.subject or word in mail.content):
                print(mail)
        return
    def delete(self,id):
        self.mails.pop(id)
        print("mail del Sucessfully")
        return
