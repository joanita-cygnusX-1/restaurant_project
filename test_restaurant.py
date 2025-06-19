 
from restaurant import welcome_message, display_menu

def test_welcome_message():
    assert welcome_message("Franchels") == "Welcome to Franchels!!"

def test_menu():
    menu_list = ["1 Starters", "2 Meals", "3 Beverages"]
    output = display_menu(menu_list)
    assert "1 Starters" in output
    assert "2 Meals" in output
    assert "3 Beverages" in output
