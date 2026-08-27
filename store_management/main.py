from models import Store
from file_handler import load_all
from functions import (
    add_product,
    view_products,
    add_customer,
    view_customers,
    create_order,
    calculate_sales,
    save_data,
    display_menu,
    get_menu_choice,
)


def main():
    store = Store()

    # Load previously saved data when the program starts.
    load_all(store)

    print("Welcome to the Store Management System!")

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            add_product(store)

        elif choice == 2:
            view_products(store)

        elif choice == 3:
            add_customer(store)

        elif choice == 4:
            view_customers(store)

        elif choice == 5:
            create_order(store)

        elif choice == 6:
            calculate_sales(store)

        elif choice == 7:
            save_data(store)

        elif choice == 8:
            # Save automatically before exiting so recent changes are not lost.
            save_data(store)
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
