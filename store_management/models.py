class Product:
    def __init__(self, product_id, name, price, quantity):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            float(data["price"]),
            int(data["quantity"])
        )


class Customer:
    def __init__(self, customer_id, name):
        self.id = customer_id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"])


class Order:
    def __init__(self, order_id, customer_id, product_id, quantity, total):
        self.id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total = total

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total": self.total
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["customer_id"],
            data["product_id"],
            int(data["quantity"]),
            float(data["total"])
        )


class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []

    def find_product(self, product_id):
        return next((p for p in self.products if p.id == product_id), None)

    def find_customer(self, customer_id):
        return next((c for c in self.customers if c.id == customer_id), None)

    def next_product_id(self):
        return max((p.id for p in self.products), default=0) + 1

    def next_customer_id(self):
        return max((c.id for c in self.customers), default=0) + 1

    def next_order_id(self):
        return max((o.id for o in self.orders), default=0) + 1

    def total_sales(self):
        return sum(order.total for order in self.orders)
