from booking import Booking
from taxi import Taxi

class TaxiSystem:
    def __init__(self, taxi_count):
        self.taxis = [Taxi(i + 1) for i in range(taxi_count)]
        self.customer_count = 1

    def book_taxi(self,from_point,to_point,pickup_time):
        customer_id = self.customer_count
        self.customer_count += 1
        selected_taxi = None
        min_distance = float('inf')

        for taxi in self.taxis:
            if taxi.is_available(pickup_time):
                distance = abs(ord(taxi.current_point) - ord(from_point))
                if distance < min_distance or (
                    distance == min_distance and taxi.total_earnings < (selected_taxi.total_earnings if selected_taxi else float('inf'))):
                    selected_taxi = taxi
                    min_distance = distance

        if selected_taxi is None:
            print("No taxis available at the moment.")
            return

        travel_time = abs(ord(to_point) - ord(from_point)) 
        drop_time = pickup_time + travel_time
        amount = selected_taxi.calculate_earnings(from_point, to_point)
        booking_id = len(selected_taxi.bookings) + 1

        booking = Booking(customer_id, booking_id, from_point, to_point, amount, pickup_time, drop_time)
        selected_taxi.add_booking(booking)
        print(f"Taxi {selected_taxi.taxi_id} booked successfully! Amount: Rs.{amount}")

    def cancel_booking(self, booking_id,taxi_id):
        for taxi in self.taxis:
            for b in taxi.bookings:
                if taxi.taxi_id== taxi_id and  b.bookingId == booking_id:
                    taxi.bookings.remove(b)
                    taxi.total_earnings -= b.amount
                    taxi.current_point = "A"
                    print(f"Booking ID {booking_id} cancelled.")
                    return
        print("Booking ID not found.")

    def display_taxis(self):
        for taxi in self.taxis:
            print(taxi)
