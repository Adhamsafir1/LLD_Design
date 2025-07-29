from booking import Booking

class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id
        self.current_point = 'A'
        self.total_earnings = 0
        self.bookings = []

    def is_available(self, request_time):
        if not self.bookings:
            return True
        return self.bookings[-1].dropTime <= request_time

    def calculate_earnings(self, from_point, to_point):
        distance = abs(ord(to_point) - ord(from_point)) * 15
        return 100 + max(0, (distance - 5) * 10)

    def add_booking(self, booking):
        self.bookings.append(booking)
        self.total_earnings += booking.amount
        self.current_point = booking.to

    def __str__(self):
        booking_info = ', '.join(
            [f"[{b.bookingId}: {b.From}->{b.to}, Rs.{b.amount}, {b.pickupTime}-{b.dropTime}]" for b in self.bookings]
        )
        return f"Taxi {self.taxi_id}: Current Point = {self.current_point}, Earnings = Rs.{self.total_earnings}, Bookings = {booking_info or 'None'}"
