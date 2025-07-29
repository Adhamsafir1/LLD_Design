class Passenger:
    def __init__(self, name, age, gender, preference, pnr):
        self.name = name
        self.age = age
        self.gender = gender
        self.preference = preference
        self.allocated_berth = None
        self.ticket_id = pnr
        self.status = "Confirmed"

    def __str__(self):
        return (f"PNR: {self.ticket_id} | Name: {self.name} | Age: {self.age} | Gender: {self.gender} | "
                f"Preferred: {self.preference} | Allocated: {self.allocated_berth or 'None'} | Status: {self.status}")