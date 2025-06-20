from restaurant import welcome_message, display_menu

def test_welcome_message():
    assert welcome_message("Franchels") == "Welcome to Franchels!!"

def test_display_menu():
    test_menu = {
        "1 Starters": ["Soup", "Salad"],
        "2 Meals": ["Steak", "Fish"],
        "3 Beverages": ["Water", "Juice"]
    }

    output = display_menu(test_menu)

    assert "1 Starters" in output
    assert "  - Soup" in output
    assert "2 Meals" in output
    assert "  - Fish" in output
    assert "3 Beverages" in output
    assert "  - Juice" in output
