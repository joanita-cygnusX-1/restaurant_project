
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
    else:
        print("\n--- Your Order ---")
        total = 0
        for item in order:
            print(f"- {item['name']} (${item['price']:.2f})")
            total += item['price']
        print(f"Total: ${total:.2f}")
    print("------------------")

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
            confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm == "y":
                display_order()
                print("Exiting program. Goodbye!")
                exit()
            else:
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
    print(f"\nItems in {category}:")
    for num, details in menu[category].items():
        print(f"{num}. {details['name']} - ${details['price']:.2f}")
    choice = input("Enter item number to add to order (or 0 to cancel): ")
    
    if choice == "0":
        print("Item selection cancelled.")
        return

    if not choice.isdigit() or int(choice) not in menu[category]:
        print("Invalid item number.")
        return

    selected = menu[category][int(choice)]
    order.append(selected)
    print(f"{selected['name']} added to your order.")

def main():
    print("🍽️ Welcome to the Restaurant Ordering System!")
    while True:
        category = get_category_choice()
        get_item_choice(category)

# Run the program
main()

if __name__ == "__main__":
    main()
  