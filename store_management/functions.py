from models import Product, Customer, Order
from file_handler import save_all


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")


def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Error: Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")


def add_product(store):
    print("\n--- Add Product ---")
    name = get_non_empty_string("Enter product name: ")
    price = get_positive_float("Enter price: ")
    quantity = get_non_negative_int("Enter quantity: ")

    product = Product(store.next_product_id(), name, price, quantity)
    store.products.append(product)

    print(f"Product added successfully. Product ID: {product.id}")


def view_products(store):
    print("\n--- Products ---")
    if not store.products:
        print("No products available.")
        return

    print(f"{'ID':<5}{'Name':<25}{'Price':<12}{'Stock':<10}")
    print("-" * 52)

    for product in store.products:
        print(
            f"{product.id:<5}"
            f"{product.name:<25}"
            f"{product.price:<12.2f}"
            f"{product.quantity:<10}"
        )


def add_customer(store):
    print("\n--- Add Customer ---")
    name = get_non_empty_string("Enter customer name: ")

    customer = Customer(store.next_customer_id(), name)
    store.customers.append(customer)

    print(f"Customer added successfully. Customer ID: {customer.id}")


def view_customers(store):
    print("\n--- Customers ---")
    if not store.customers:
        print("No customers registered.")
        return

    print(f"{'ID':<5}{'Name':<30}")
    print("-" * 35)

    for customer in store.customers:
        print(f"{customer.id:<5}{customer.name:<30}")


def create_order(store):
    print("\n--- Create Order ---")

    if not store.customers:
        print("Error: No customers available. Add a customer first.")
        return

    if not store.products:
        print("Error: No products available. Add a product first.")
        return

    view_customers(store)
    customer_id = get_positive_int("Enter customer ID: ")
    customer = store.find_customer(customer_id)

    if customer is None:
        print("Error: Invalid customer ID.")
        return

    available_products = [p for p in store.products if p.quantity > 0]
    if not available_products:
        print("Error: No products are currently in stock.")
        return

    print()
    view_products(store)
    product_id = get_positive_int("Enter product ID: ")
    product = store.find_product(product_id)

    if product is None:
        print("Error: Invalid product ID.")
        return

    if product.quantity <= 0:
        print("Error: This product is out of stock.")
        return

    quantity = get_positive_int("Enter quantity: ")

    if quantity > product.quantity:
        print(
            f"Error: Not enough stock. Available stock: {product.quantity}"
        )
        return

    total = product.price * quantity
    product.quantity -= quantity

    order = Order(
        store.next_order_id(),
        customer.id,
        product.id,
        quantity,
        total
    )
    store.orders.append(order)

    print("\nOrder created successfully!")
    print(f"Customer: {customer.name}")
    print(f"Product: {product.name}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total:.2f}")
    print(f"Remaining Stock: {product.quantity}")


def calculate_sales(store):
    print("\n--- Sales Summary ---")

    if not store.orders:
        print("No completed orders yet.")
        print("Total Orders: 0")
        print("Total Revenue: 0.00")
        return

    total = store.total_sales()

    print(f"Total Orders: {len(store.orders)}")
    print(f"Total Revenue: {total:.2f}")


def save_data(store):
    try:
        save_all(store)
        print("Data saved successfully.")
    except OSError as error:
        print(f"Error while saving data: {error}")


def display_menu():
    print("\n" + "=" * 35)
    print("     STORE MANAGEMENT SYSTEM")
    print("=" * 35)
    print("1. Add Product")
    print("2. View Products")
    print("3. Add Customer")
    print("4. View Customers")
    print("5. Create Order")
    print("6. Calculate Total Sales")
    print("7. Save Data")
    print("8. Exit")
    print("=" * 35)


def get_menu_choice():
    while True:
        choice = input("Enter your choice: ").strip()
        try:
            choice = int(choice)
            if 1 <= choice <= 8:
                return choice
            print("Error: Please choose a number from 1 to 8.")
        except ValueError:
            print("Error: Please enter a number.")
