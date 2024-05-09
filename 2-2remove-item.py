"""
Task 2: Include a feature to remove items from the list.
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

shopping_list = []
add_item(shopping_list)
print("Your shopping list:", shopping_list)
remove_item(shopping_list)
print("Your final shopping list:", shopping_list)