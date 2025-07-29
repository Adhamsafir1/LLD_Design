from screan import screan
from seat import seat
class Theatre:
    def __init__(self):
        self.screans = []
        self.Booking = []
        self.create()

    def create(self):
        for i in range(1, 3):  # Creating 2 screens
            self.screans.append(screan(i))

    def print_seat(self):
        for seats in self.screans:
            print(seats)

    def booking(self, movieId, seat_type, seatNo, name, phoneNo):
        screen_index = movieId - 1
        if screen_index >= len(self.screans):
            print("Invalid movieId/screen.")
            return

        Aseat = seat_type + str(seatNo)

        for seat_type_obj in self.screans[screen_index].TotalSeats:
            if seat_type_obj.seattype == seat_type:
                if seat_type_obj.seats.get(Aseat) is None:
                    # Book the seat
                    booked_seat = seat(Aseat, name, phoneNo)
                    seat_type_obj.seats[Aseat] = booked_seat
                    self.Booking.append(booked_seat)
                    print(f"Seat {Aseat} successfully booked for {name}.")
                    return
                else:
                    print(f"Seat {Aseat} is already booked.")
                    return
        print(f"Seat type {seat_type} not found in screen {movieId}.")

    def show_bookings(self):
        print("All Bookings:")
        for b in self.Booking:
            print(b)


    def cancel_booking(self, seat_id):
        for screen in self.screans:
            for seat_type_obj in screen.TotalSeats:
                if seat_id in seat_type_obj.seats:
                    if seat_type_obj.seats[seat_id] is not None:
                        seat_type_obj.seats[seat_id] = None  
                        self.Booking = [b for b in self.Booking if b.seatNo != seat_id]
                        print(f"Booking for seat {seat_id} has been cancelled.")
                        return
                    else:
                        print(f"Seat {seat_id} was not booked.")
                        return
        print(f"Seat {seat_id} not found.")


