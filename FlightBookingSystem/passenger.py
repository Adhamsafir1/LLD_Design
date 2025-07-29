class passenger:
    def __init__(self, passenger_id, name, age, gender, pref, seatNo):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.gender = gender
        self.pref = pref
        self.seatNo = seatNo

    def __str__(self):
        return (
            f"Passenger ID: {self.passenger_id}\n"
            f"Name        : {self.name}\n"
            f"Age         : {self.age}\n"
            f"Gender      : {self.gender}\n"
            f"Preference  : {self.pref}\n"
            f"Seat No     : {self.seatNo}"
        )

