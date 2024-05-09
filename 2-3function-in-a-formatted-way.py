"""
Task 3: Add a function that prints out the entire list in a formatted way.
"""

def add_item(selected_items):
    while True:
        input_items = input("Enter an item to your shopping cart or 'done' to finish: ").strip()
        if input_items.lower() .strip() == "done":
            break
        else:
            selected_items.append(input_items)

def remove_item(selected_items):
    while True:
        input_items = input("Enter an item to remove from your shopping cart or 'done' to finish: ").strip()
        if input_items.lower() .strip() == "done":
            break
        if input_items in selected_items:
            selected_items.remove(input_items)

def print_formatted_list(selected_items):
    for i, item in enumerate(selected_items, 1):
        print(f"{i}. {item}")

shopping_list = []
add_item(shopping_list)
print("Your shopping list:")
print_formatted_list(shopping_list)
remove_item(shopping_list)
print("Your final shopping list:")
print_formatted_list(shopping_list)