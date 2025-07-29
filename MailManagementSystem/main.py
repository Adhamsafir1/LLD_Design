from System import System

def main():
    system = System()
    while True:
        print("1. Add Mail")
        print("2. Add tag")
        print("3. print AllMail")
        print("4. WildCard Search")
        print("5. Search")
        print("6. Exit")
        choice = input("Enter choice:")
        if choice =="1":
            sender = input("Enter Sender:")
            receiver = input("Enter Receiver:")
            subject = input("Enter Subject:")
            content = input("Enter Content:")
            system.addmail(sender,receiver,subject,content)
        elif choice=="2":
            id = int(input("Enter Id:"))
            tags = input("Enter Tag: ")
            system.add_tag(id,tags)
        elif choice=="3":
            system.printAllMail()
        elif choice=="4":
            word  = input("Enter Word to Search:")
            system.WildCard(word)
        elif choice=="5":
            word = input("Enter word to search: ")
            system.search(word)
        elif choice=="6":
            id = int(input("Enter ID :"))
            system.delete(id)
        elif choice=="7":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()