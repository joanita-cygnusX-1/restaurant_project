def welcome_message(name):
    return f"Welcome to {name}!!"

def display_menu(menu):
    menu_text = ""
    for category, items in menu.items():
        menu_text += category + "\n"
        if items:
            for i, item in enumerate(items, start=1):
                menu_text += f"  {i}. {item['name']} - ${item['price']}\n"
        else:
            menu_text += "  No items to display\n"
    return menu_text.strip()

def pick_menu_item(menu):
    print("Please choose a category:")
    categories = list(menu.keys())
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    try:
        category_choice = int(input("Enter the number of the category: "))
        if 1 <= category_choice <= len(categories):
            selected_category = categories[category_choice - 1]
        else:
            print("Invalid category number.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

    items = menu[selected_category]
    if not items:
        print("No items to display in this category.")
        return None

    print(f"\nItems in {selected_category}:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item['name']} - ${item['price']}")

    try:
        item_choice = int(input("Enter the number of the item: "))
        if 1 <= item_choice <= len(items):
            selected_item = items[item_choice - 1]
        else:
            print("Invalid item number.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

    try:
        quantity = int(input(f"How many '{selected_item['name']}' would you like? "))
        if quantity < 1:
            print("Quantity must be at least 1.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

    return {
        "category": selected_category,
        "name": selected_item["name"],
        "price": selected_item["price"],
        "quantity": quantity
    }

def show_order_summary(order_items):
    print("\n----- Order Summary -----")
    total = 0
    for i, item in enumerate(order_items, start=1):
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{i}. {item['quantity']} x {item['name']} (${item['price']} each) = ${subtotal}")
    print(f"Total: ${total}")
    print("-------------------------\n")

def start(name, menu_data):
    print(welcome_message(name))
    print("Explore our Menu\n")
    print(display_menu(menu_data))

    order_items = []
    while True:
        result = pick_menu_item(menu_data)
        if result:
            order_items.append(result)
            another = input("Would you like to add another item? (yes/no): ").lower()
            if another != "yes":
                break
        else:
            print("Item not added. Try again.")

    show_order_summary(order_items)

def main():
    restaurant_name = "Franchels Restaurant"
    menu_list = {
        "Starters": [
            {"name": "Soup of the Day", "price": 5},
            {"name": "Bruschetta", "price": 7},
            {"name": "Garlic Bread", "price": 4}
        ],
        "Meals": [
            {"name": "Grilled Chicken", "price": 12},
            {"name": "Pasta Carbonara", "price": 10},
            {"name": "Veggie Burger", "price": 9}
        ],
        "Beverages": [
            {"name": "Coke", "price": 2},
            {"name": "Orange Juice", "price": 3},
            {"name": "Water", "price": 1}
        ]
    }
    start(restaurant_name, menu_list)

if __name__ == "__main__":
    main()
