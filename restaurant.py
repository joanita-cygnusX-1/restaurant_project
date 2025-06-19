def welcome_message(name):
    return f"Welcome to {name}!!"

def display_menu(menu):
    menu_text = ""
    for item in menu:
        menu_text += item + "\n"
    return menu_text.strip()

def start(name, menu_data):
    print(welcome_message(name))
    print("Explore our Menu\n")
    print(display_menu(menu_data))

def main():
    restaurant_name = "Franchels Restaurant"
    menu_list = ["1 Starters", "2 Meals", "3 Beverages"]
    start(restaurant_name, menu_list)

if __name__ == "__main__":
    main()
