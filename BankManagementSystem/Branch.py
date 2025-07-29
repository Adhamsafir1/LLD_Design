from Account import Account

class Branch:
    def __init__(self):
        self.AccList = []

    def createAcc(self, AcName, Age, Branch_id):
        acc = Account(AcName, Age, Branch_id)
        self.AccList.append(acc)
        print("Account added successfully!")
        print(acc)
        return acc

    def DelAcc(self, AccNo):
        for acc in self.AccList:
            if acc.AccNo == AccNo:
                self.AccList.remove(acc)
                print("Account deleted successfully.")
                return
        print("Account not found.")

    def Transaction(self, AccNo, TransAccNo, Amounts):
        from_acc = None
        to_acc = None

        for acc in self.AccList:
            if acc.AccNo == AccNo:
                from_acc = acc
            if acc.AccNo == TransAccNo:
                to_acc = acc

        if not from_acc or not to_acc:
            print("One or both accounts not found.")
            return

        if from_acc.Amount >= Amounts:
            from_acc.Amount -= Amounts
            to_acc.Amount += Amounts
            print("Transaction successful.")
        else:
            print("Insufficient Balance.")

    def withdrawl(self, AccNo, Amounts):
        for acc in self.AccList:
            if acc.AccNo == AccNo:
                if acc.Amount >= Amounts:
                    acc.Amount -= Amounts
                    print(f"Withdrawal successful. Remaining Balance: Rs.{acc.Amount}")
                else:
                    print("Insufficient Balance.")
                return
        print("Account not found.")

    def Deposite(self, AccNo, Amounts):
        for acc in self.AccList:
            if acc.AccNo == AccNo:
                acc.Amount += Amounts
                print(f"Deposit successful. Total Balance: Rs.{acc.Amount}")
                return
        print("Account not found.")
