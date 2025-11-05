# Restaurant Ordering System with Quantity, Edit & Exit Confirmation

menu = {
    "Starters": {
        1: {"name": "Spring Rolls", "price": 5.0},
        2: {"name": "Garlic Bread", "price": 4.5}
    },
    "Meals": {
        1: {"name": "Grilled Chicken", "price": 10.0},
        2: {"name": "Veggie Burger", "price": 8.5}
    },
    "Beverages": {
        1: {"name": "Lemonade", "price": 3.0},
        2: {"name": "Iced Tea", "price": 3.5}
    }
}

order = []

def display_order():
    if not order:
        print("\nYour order is empty.")
        return
    print("\n--- Your Order ---")
    total = 0
    for item in order:
        print(f"- {item['name']} x{item['quantity']} = ${item['price']*item['quantity']:.2f}")
        total += item['price'] * item['quantity']
    print(f"Total: ${total:.2f}")
    print("------------------")

def confirm_exit():
    if order:
        display_order()
    confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
    if confirm == "y":
        print("Thank you for shopping with us. Come again next time. Goodbye!")
        exit()

def get_category_choice():
    categories = list(menu.keys())
    invalid_attempts = 0
    while True:
        print("\nPlease choose a category:")
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {cat}")
        print("0. Exit")

        choice = input("Enter the number of the category: ")

        if choice == "0":
            confirm_exit()
            continue

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(categories):
            print("Please enter a valid number.")
            invalid_attempts += 1
            if invalid_attempts >= 2:
                print("Too many invalid attempts. Showing order and exiting...")
                display_order()
                exit()
            continue

        return categories[int(choice) - 1]

def get_item_choice(category):
    items = menu[category]
    print(f"\nItems in {category}:")
    for num, details in items.items():
        print(f"{num}. {details['name']} - ${details['price']:.2f}")
    
    choice = input("Enter item number to add to order (or 0 to cancel): ")
    if choice == "0":
        print("Item selection cancelled.")
        return

    if not choice.isdigit() or int(choice) not in items:
        print("Invalid item number.")
        return

    selected_item = items[int(choice)]

    while True:
        quantity_input = input(f"Enter quantity for {selected_item['name']}: ")
        if not quantity_input.isdigit() or int(quantity_input) < 1:
            print("Please enter a valid positive number for quantity.")
        else:
            quantity = int(quantity_input)
            break

    order.append({
        "name": selected_item['name'],
        "price": selected_item['price'],
        "quantity": quantity
    })
    print(f"{selected_item['name']} x{quantity} added to your order.")

def main():
    print("🍽️ Welcome to the Restaurant Ordering System!")
    while True:
        category = get_category_choice()
        get_item_choice(category)
        display_order()

# Run the program
if __name__ == "__main__":
    main()
