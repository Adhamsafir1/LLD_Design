from taxi_system import TaxiSystem

def main():
    num_taxis = int(input("Enter number of taxis: "))
    system = TaxiSystem(num_taxis)

    while True:
        print("\n1. Book a Taxi\n2. Cancel Booking\n3. View All Taxis\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            from_point = input("Enter pickup point (A-Z): ").strip().upper()
            to_point = input("Enter drop point (A-Z): ").strip().upper()
            pickup_time = int(input("Enter pickup time (in hrs): "))
            system.book_taxi(from_point,to_point,pickup_time)
        elif choice == '2':
            taxi_id = int(input("Enter TaxiId to cancel:"))
            booking_id = int(input("Enter booking ID to cancel: "))
            system.cancel_booking(booking_id,taxi_id)
        elif choice == '3':
            system.display_taxis()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
