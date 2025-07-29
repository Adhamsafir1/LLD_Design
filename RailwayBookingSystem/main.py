import uuid
from Train import Train

def main():
    train = Train()
    while True:
        print("\n==== Railway Ticket Booking System ====")
        print("1. Book Ticket(s)")
        print("2. Cancel Ticket by PNR")
        print("3. Show Full Seat Chart")
        print("4. Show Ticket Available Summary")
        print("5. Add Cabins")
        print("6. Print PNR Details")
        print("7. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            n = int(input("Number of passengers: "))
            shared_pnr = str(uuid.uuid4())[:8]
            group = []
            for i in range(n):
                print(f"\nPassenger {i + 1}:")
                name = input("  Name: ")
                age = int(input("  Age: "))
                gender = input("  Gender (M/F): ")
                pref = input("  Preferred Berth (LB/MB/UB/SUB): ").upper()
                p = train.book_ticket(name, age, gender, pref, shared_pnr)
                if p:
                    group.append(p)

            print("\nBooking Summary:")
            for p in group:
                print(p)

        elif choice == '2':
            pnr = input("Enter PNR to cancel: ")
            train.cancel_ticket(pnr)

        elif choice == '3':
            train.print_booked()

        elif choice == '4':
            train.print_available()

        elif choice == '5':
            count = int(input("Enter number of Cabins: "))
            train.add_cabin(count)

        elif choice == '6':
            pnr = input("Enter PNR: ").strip()
            seats = train.print_pnr(pnr)
            for p in seats:
                print(p)

        elif choice == '7':
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
