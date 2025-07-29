from flight import flight
import uuid

def main():
    system = flight()
    while True:
        print("\n1. Book Ticket\n2. viewSeats \n3. Cancel Ticket")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            passenger_id = str(uuid.uuid4())[:8]
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender (M/F): ").strip().upper()
            pref = input("Enter Class Preference (P/F/S): ").strip().upper()
            seat_number = int(input("Enter Seat Number (1-10): "))

            system.booking(name, age, gender, pref, seat_number, passenger_id)

        elif choice =='2':
            system.viewseats()

        elif choice =='3':
            passenger_id = input("Enter passenger ID:")
            # alloc = input("Enter alloc: ")
            system.cancel(passenger_id)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
