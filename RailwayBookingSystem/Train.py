from collections import deque
from cabin import Cabin
from Passenger import Passenger

class Train:
    MAX_RAC = 2
    MAX_WL = 2

    def __init__(self):
        self.cabins = [Cabin(1)]
        self.booked_passengers = {}
        self.rac_queue = deque()
        self.waiting_list = deque()

    def add_cabin(self, count):
        for _ in range(count):
            new_id = len(self.cabins) + 1
            self.cabins.append(Cabin(new_id))
            self.MAX_RAC+=2
            self.MAX_WL+=2

    def book_ticket(self, name, age, gender, pref, pnr):
        passenger = Passenger(name, age, gender, pref, pnr)

        if age < 5:
            passenger.status = "No Seat (Infant)"
            self._add_passenger(passenger)
            return passenger

        priority = 'LB' if age >= 60 or (gender.lower() == 'female' and age <= 35) else pref

        for btype in [priority, 'LB', 'MB', 'UB', 'SUB']:
            for cabin in self.cabins:
                avail = cabin.get_available_berths(btype)
                if avail:
                    avail[0].assign(passenger)
                    self._add_passenger(passenger)
                    return passenger

        if len(self.rac_queue) < self.MAX_RAC:
            for cabin in self.cabins:
                avail = cabin.get_available_berths("SLB")
                if avail:
                    avail[0].assign(passenger)
                    passenger.status = "RAC"
                    self.rac_queue.append(passenger)
                    self._add_passenger(passenger)
                    return passenger

        if len(self.waiting_list) < self.MAX_WL:
            passenger.status = "Waiting List"
            self.waiting_list.append(passenger)
            self._add_passenger(passenger)
            return passenger

        print("No Tickets Available")
        return None

    def _add_passenger(self, passenger):
        if passenger.ticket_id not in self.booked_passengers:
            self.booked_passengers[passenger.ticket_id] = []
        self.booked_passengers[passenger.ticket_id].append(passenger)

    def cancel_ticket(self, pnr):
        group = self.booked_passengers.pop(pnr, None)
        if not group:
            print("PNR not found.")
            return

        for p in group:
            if p.status == "Confirmed":
                for cabin in self.cabins:
                    for berth in cabin.berths:
                        if berth.occupied_by == p:
                            berth.release()
            elif p.status == "RAC":
                self.rac_queue = deque([x for x in self.rac_queue if x.ticket_id != pnr])
            elif p.status == "Waiting List":
                self.waiting_list = deque([x for x in self.waiting_list if x.ticket_id != pnr])

        print(f"Cancelled all tickets under PNR {pnr}")
        self._promote_rac_to_confirmed()

    def _promote_rac_to_confirmed(self):
        if not self.rac_queue:
            return

        rac_p = self.rac_queue.popleft()
        rac_p.status = "Confirmed"
        print(f"Promoted RAC passenger: {rac_p.name} (PNR: {rac_p.ticket_id})")
        self.book_ticket(rac_p.name, rac_p.age, rac_p.gender, rac_p.preference, rac_p.ticket_id)

        if self.waiting_list:
            wl_p = self.waiting_list.popleft()
            wl_p.status = "RAC"
            self.rac_queue.append(wl_p)

    def print_booked(self):
        print("\nSeat Chart (Booked + Available):")
        for cabin in self.cabins:
            print(f"\nCabin {cabin.cabin_id}")
            for berth in cabin.berths:
                if berth.occupied_by:
                    p = berth.occupied_by
                    print(f"{berth.type}-{berth.number} | {p.name}, {p.age}, {p.gender} | PNR: {p.ticket_id} | Status: {p.status}")
                else:
                    print(f"{berth.type}-{berth.number}| -- | -- | PNR: -- | Status: Available")
        print(f"\nTotal Booked: {sum(len(v) for v in self.booked_passengers.values())}")
        print(f"RAC Queue: {len(self.rac_queue)} / {self.MAX_RAC}")
        print(f"Waiting List: {len(self.waiting_list)} / {self.MAX_WL}")

    def print_available(self):
        total = 0
        for cabin in self.cabins:
            for b in cabin.berths:
                if b.is_available():
                    print(f"{b.type}-{b.number} is Available")
                    total += 1
        print(f"\nTotal Available Berths: {total}")
        print(f"Available RAC: {self.MAX_RAC - len(self.rac_queue)}")
        print(f"Available WL: {self.MAX_WL - len(self.waiting_list)}")

    def print_pnr(self, pnr):
        if pnr in self.booked_passengers:
            return self.booked_passengers[pnr]
        else:
            print("PNR not found.")
            return []
