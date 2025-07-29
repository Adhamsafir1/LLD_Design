from seatsType import seatType
class screan:
    def __init__(self, screanId):
        self.screanId = screanId
        self.TotalSeats = []
        self.create()

    def create(self):
        for s in ["L", "M", "U"]:
            self.TotalSeats.append(seatType(s))

    def __str__(self):
        result = f"ScreanId: {self.screanId}\n"
        for stype in self.TotalSeats:
            result += f"Seat Type {stype.seattype}:\n{stype}\n"
        return result
