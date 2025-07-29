from passenger import passenger
from classes import classes

class flight:
    def __init__(self):
        self.seats = []
        self.bookedSeats = {}
        self.createseats()
        self.Amount = 0

    def createseats(self):
        for p in ["P", "F", "S"]:
            self.seats.append(classes(p))

    def booking(self, name, age, gender, pref, seatNo, passenger_id):
        full_seat_no = pref + str(seatNo)  # e.g., 'P1'

        for seat_class in self.seats:
            if seat_class.type == pref:
                if full_seat_no in seat_class.ClassArr:
                    if seat_class.ClassArr[full_seat_no] is None:
                        Passenger = passenger(passenger_id, name, age, gender, pref, full_seat_no)
                        seat_class.ClassArr[full_seat_no] = Passenger
                        self.bookedSeats[full_seat_no] = Passenger
                        total = 5000 + len(self.bookedSeats)*200
                        self.Amount += total
                        print(f"Pay Amount: {total}")
                        print("Booking successful!\n", Passenger)
                        return
                    else:
                        print("Seat already booked.")
                        return
        print("Invalid seat or preference.")


    def cancel(self, passenger_id):
        for seat_class in self.seats:
            for seat_no, passenger in seat_class.ClassArr.items():
                if passenger and passenger.passenger_id == passenger_id:
                    seat_class.ClassArr[seat_no] = None
                    self.bookedSeats.pop(seat_no, None)
                    self.Amount -= 5200
                    print(f"refund Amount: {5200}")
                    print(f"Booking for {passenger.name} ({seat_no}) cancelled successfully!")
                    return
        print("Passenger ID not found.")


    def viewseats(self):
        for seat in self.seats:
            print(seat)
        return


