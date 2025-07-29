# main.py
from Inventory import Inventory

def main():
    system = Inventory()

    while True:
        print("\n1. Create Seller")
        print("2. Add Product")
        print("3. View Inventory")
        print("4. Buy Product")
        print("5. View Buyers")
        print("6. Total Cost for Buyer")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter Seller ID: ")
            name = input("Enter Seller Name: ")
            system.create_seller(sid, name)

        elif choice == "2":
            sid = input("Enter Seller ID: ")
            product = input("Enter Product Name: ")
            price = input("Enter price: ")
            system.add(sid, product, price)

        elif choice == "3":
            system.viewInventory()

        elif choice == "4":
            bid = input("Enter Buyer ID: ")
            bname = input("Enter Buyer Name: ")
            product = input("Enter Product Name to Buy: ")
            system.buy_product(bid, bname, product)

        elif choice == "5":
            system.printBuyers()

        elif choice == "6":
            bid = input("Enter Buyer ID to view total cost: ")
            system.totalcost(bid)

        elif choice == "7":
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
