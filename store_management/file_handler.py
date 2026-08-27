import json
from pathlib import Path
from models import Product, Customer, Order

DATA_DIR = Path(__file__).parent / "data"
PRODUCTS_FILE = DATA_DIR / "products.json"
CUSTOMERS_FILE = DATA_DIR / "customers.json"
ORDERS_FILE = DATA_DIR / "orders.json"


def _ensure_data_dir():
    DATA_DIR.mkdir(exist_ok=True)


def _write_json(file_path, data):
    _ensure_data_dir()
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def _read_json(file_path):
    _ensure_data_dir()
    if not file_path.exists():
        file_path.write_text("[]", encoding="utf-8")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_products(products):
    _write_json(PRODUCTS_FILE, [product.to_dict() for product in products])


def save_customers(customers):
    _write_json(CUSTOMERS_FILE, [customer.to_dict() for customer in customers])


def save_orders(orders):
    _write_json(ORDERS_FILE, [order.to_dict() for order in orders])


def save_all(store):
    save_products(store.products)
    save_customers(store.customers)
    save_orders(store.orders)


def load_products():
    return [Product.from_dict(item) for item in _read_json(PRODUCTS_FILE)]


def load_customers():
    return [Customer.from_dict(item) for item in _read_json(CUSTOMERS_FILE)]


def load_orders():
    return [Order.from_dict(item) for item in _read_json(ORDERS_FILE)]


def load_all(store):
    store.products = load_products()
    store.customers = load_customers()
    store.orders = load_orders()
