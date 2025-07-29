import uuid

class Account:
    def __init__(self, AccName, Age, Branch_id):
        self.AccNo = str(uuid.uuid4())[:6]  # Short but unique
        self.AccName = AccName
        self.Age = Age
        self.Amount = 0
        self.Branch_id = Branch_id

    def __str__(self):
        return (
            f"Account Details:\n"
            f"  Account No  : {self.AccNo}\n"
            f"  Name        : {self.AccName}\n"
            f"  Age         : {self.Age}\n"
            f"  Amount      : Rs.{self.Amount}\n"
            f"  Branch ID   : {self.Branch_id}"
        )
