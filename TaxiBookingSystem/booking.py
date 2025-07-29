class Booking:
    def __init__(self, customerId, bookingId, From, to, amount, pickupTime, dropTime):
        self.customerId = customerId
        self.bookingId = bookingId
        self.From = From
        self.to = to
        self.amount = amount
        self.pickupTime = pickupTime
        self.dropTime = dropTime
