from Branch import Branch

def main():
    branching = Branch()  

    while True:
        print("\n=== Bank Menu ===")
        print("1. Create Account")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Transfer Amount")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            branch_id = input("Enter Branch ID: ")
            branching.createAcc(name, age, branch_id)

        elif choice == '2':
            acc_no = input("Enter Account No: ")
            amt = int(input("Enter Amount to Deposit: "))
            branching.Deposite(acc_no, amt)

        elif choice == '3':
            acc_no = input("Enter Account No: ")
            amt = int(input("Enter Amount to Withdraw: "))
            branching.withdrawl(acc_no, amt)

        elif choice == '4':
            from_acc = input("Enter Sender Account No: ")
            to_acc = input("Enter Receiver Account No: ")
            amt = int(input("Enter Amount to Transfer: "))
            branching.Transaction(from_acc, to_acc, amt)

        elif choice == '5':
            acc_no = input("Enter Account No to Delete: ")
            branching.DelAcc(acc_no)

        elif choice == '6':
            print("Exiting Banking System...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
