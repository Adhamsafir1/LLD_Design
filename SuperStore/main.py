from services import ProfileService, InventoryService, OrderService, PaymentService

if __name__ == '__main__':
    profile = ProfileService()
    inventory = InventoryService()
    order = OrderService(inventory)
    payment = PaymentService()

    print(profile.register("alice", "pass123", "seller"))
    print(profile.register("bob", "pass456", "buyer"))

    seller = profile.login("alice", "pass123")
    buyer = profile.login("bob", "pass456")

    print(inventory.add_item("Laptop", 50000, 10, seller.username))
    print(inventory.add_item("Mouse", 500, 50, seller.username))

    inventory.list_inventory()

    print(order.add_to_cart(buyer, 1, 1))
    print(order.add_to_cart(buyer, 2, 2))
    print(order.buy_items(buyer))

    payment.make_payment(buyer, 51000)