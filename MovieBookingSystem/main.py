from Theatre import Theatre

def main():
    t = Theatre()
    while True:

        print("1.Booking Ticket:")
        print("2.Show Bookings")
        print("3.Print Screaning")
        print("4.cancell Ticket:")
        choice = input("Enter Choice:")
        if choice=="1":
            print("1:vettaikaaran , 2:GBU")
            movieId = int(input("Enter MovieId:"))
            seat_type = input("Enter seatType:")
            seatNo = int(input("Enter SeatNo:"))
            name = input("Name:")
            PhoneNo = input("Enter PhoneNo")
            # movie = input("Enter MovieName:")
            t.booking(movieId,seat_type,seatNo,name,PhoneNo)

            # t.booking(movieId=1, seat_type="L", seatNo=5, name="Adham", phoneNo="1234567890", movie="Inception")
        elif choice == "2":
            t.show_bookings()
        elif choice =="3":
            t.print_seat()
        elif choice == "4":
            seat_id = input("Enter SeatId:")
            t.cancel_booking(seat_id)


if __name__ == "__main__":
    main()
