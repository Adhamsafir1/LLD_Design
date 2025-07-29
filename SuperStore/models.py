import hashlib

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = self._encrypt_password(password)
        self.role = role  # 'buyer' or 'seller'
        self.cart = {} if role == 'buyer' else None

    def _encrypt_password(self, pwd):
        return hashlib.sha256(pwd.encode()).hexdigest()
    

    def check_password(self, pwd):
        return self.password == hashlib.sha256(pwd.encode()).hexdigest()

class Product:
    def __init__(self, item_id, name, price, quantity, seller):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.seller = seller

