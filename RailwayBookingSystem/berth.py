class Berth:
    def __init__(self, number, btype):
        self.number = number
        self.type = btype  # LB, MB, UB, SLB, SUB
        self.occupied_by = None

    def is_available(self):
        return self.occupied_by is None

    def assign(self, passenger):
        self.occupied_by = passenger
        passenger.allocated_berth = f"{self.type}-{self.number}"

    def release(self):
        self.occupied_by = None