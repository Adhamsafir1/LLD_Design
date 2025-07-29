class classes:
    def __init__(self, type):
        self.type = type
        self.ClassArr = {}  # seatNo -> passenger or None
        self.create()

    def create(self):
        for i in range(1, 11):
            seat = self.type + str(i)
            self.ClassArr[seat] = None  # None means unoccupied

    def __str__(self):
        seat_status = [
            f"{seat}: {'Available' if passenger is None else 'Booked'}"
            for seat, passenger in self.ClassArr.items()
        ]
        seats_display = ", ".join(seat_status)
        return f"Class Type: {self.type}\nSeats: {seats_display}"
