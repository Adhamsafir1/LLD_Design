from Seller import Seller
from Buyer import Buyer

class Inventory:
    def __init__(self):
        self.InventoryList = {}  # sellerId -> list of (product, price)
        self.Buyers = {}         # buyerId -> Buyer
        self.Sellers = {}        # sellerId -> Seller

    def create_seller(self, sellerId, sellerName):
        if sellerId not in self.Sellers:
            self.Sellers[sellerId] = Seller(sellerId, sellerName)
            print(f"Seller {sellerName} registered successfully.")
        else:
            print("Seller already exists.")

    def add(self, sellerId, product, price):
        if sellerId not in self.Sellers:
            print("Seller not found. Please register first.")
            return

        if sellerId not in self.InventoryList:
            self.InventoryList[sellerId] = []
        self.InventoryList[sellerId].append((product, float(price)))
        print(f"Product '{product}' added to seller {sellerId}'s inventory at price {price}.")

    def viewInventory(self):
        print("Inventory List:")
        for sellerId, products in self.InventoryList.items():
            print(f"Seller {sellerId}:")
            for prod, price in products:
                print(f"  - {prod}: Rs.{price}")

    def buy_product(self, buyerId, buyerName, productName):
        if buyerId not in self.Buyers:
            self.Buyers[buyerId] = Buyer(buyerId, buyerName)

        for sellerId, productList in self.InventoryList.items():
            for i, (prod, price) in enumerate(productList):
                if prod == productName:
                    self.Buyers[buyerId].cart.append((prod, price))
                    productList.pop(i)
                    print(f"Buyer {buyerId} bought '{prod}' for Rs.{price} from seller {sellerId}")
                    return

        print("Product not found in inventory.")

    def printBuyers(self):
        print("Buyers and their carts:")
        for buyer in self.Buyers.values():
            print(f"Buyer {buyer.buyerId} ({buyer.name}):")
            for prod, price in buyer.cart:
                print(f"  - {prod}: Rs.{price}")

    def totalcost(self, buyerId):
        if buyerId not in self.Buyers:
            print("Buyer not found.")
            return
        total = 0
        print(f"Total cost breakdown for Buyer {buyerId}:")
        for prod, price in self.Buyers[buyerId].cart:
            print(f"  - {prod}: Rs.{price}")
            total += price
        print(f"Total Cost: Rs.{total}")
