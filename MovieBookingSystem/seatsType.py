class seatType:
    def __init__(self, seattype):
        self.seattype = seattype
        self.seats = {}
        self.create()

    def create(self):
        for i in range(1, 11):
            seat_id = self.seattype + str(i)
            self.seats[seat_id] = None

    def __str__(self):
        result = [f"{seat_id}: {status}" for seat_id, status in self.seats.items()]
        return "\n".join(result)
