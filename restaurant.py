def welcome_message(name):
    return f"Welcome to {name}!!"

def display_menu(menu):
    menu_text = ""
    for category, items in menu.items():
        menu_text += category + "\n"
        for item in items:
            menu_text += "  - " + item + "\n"
    return menu_text.strip()

def start(name, menu_data):
    print(welcome_message(name))
    print("Explore our Menu\n")
    print(display_menu(menu_data))

def main():
    restaurant_name = "Franchels Restaurant"
    #menu_list = ["1 Starters", "2 Meals", "3 Beverages"]
    menu_list = {
        "1 Starters": ["Soup of the Day", "Bruschetta", "Garlic Bread"],
        "2 Meals": ["Grilled Chicken", "Pasta Carbonara", "Veggie Burger"],
        "3 Beverages": ["Coke", "Orange Juice", "Water"]
    }
    start(restaurant_name, menu_list)

if __name__ == "__main__":
    main()
