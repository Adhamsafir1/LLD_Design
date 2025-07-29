# File: services.py
from models import User, Product

class ProfileService:
    def __init__(self):
        self.users = {}

    def register(self, username, password, role):
        if username in self.users:
            return "Username already exists"
        user = User(username, password, role)
        self.users[username] = user
        return "Registration successful"

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            return user
        return None

class InventoryService:
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def add_item(self, name, price, qty, seller):
        item = Product(self.next_id, name, price, qty, seller)
        self.products[self.next_id] = item
        self.next_id += 1
        return f"Item '{name}' added"

    def update_item(self, item_id, qty):
        product = self.products.get(item_id)
        if product:
            product.quantity = qty
            return f"Item '{product.name}' quantity updated to {qty}"
        return "Item not found"

    def list_inventory(self):
        for item in self.products.values():
            print(f"ID: {item.item_id} | Name: {item.name} | Price: {item.price} | Qty: {item.quantity} | Seller: {item.seller}")

    def get_product(self, item_id):
        return self.products.get(item_id)

class OrderService:
    def __init__(self, inventory_service):
        self.inventory_service = inventory_service
        self.orders = []

    def add_to_cart(self, user, item_id, qty):
        product = self.inventory_service.get_product(item_id)
        if product and product.quantity >= qty:
            if item_id in user.cart:
                user.cart[item_id] += qty
            else:
                user.cart[item_id] = qty
            return f"{qty} of {product.name} added to cart"
        return "Item not available in required quantity"

    def buy_items(self, user):
        total = 0
        for item_id, qty in user.cart.items():
            product = self.inventory_service.get_product(item_id)
            if not product or product.quantity < qty:
                return f"Not enough stock for {product.name if product else 'item'}"

        for item_id, qty in user.cart.items():
            product = self.inventory_service.get_product(item_id)
            product.quantity -= qty
            total += product.price * qty
            self.orders.append((user.username, product.name, qty))
        user.cart.clear()
        return f"Order placed. Total amount: Rs.{total}"

class PaymentService:
    def make_payment(self, user, amount):
        print(f"{user.username} paid Rs.{amount}. Payment successful!")

