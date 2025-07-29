class seat:
    def __init__(self, seatNo, name, phoneNo):
        self.seatNo = seatNo
        self.name = name
        self.phoneNo = phoneNo
        # self.movie = movie

    def __str__(self):
        return (
            f"SeatNo: {self.seatNo}, Name: {self.name}, PhoneNo: {self.phoneNo}"
        )
   