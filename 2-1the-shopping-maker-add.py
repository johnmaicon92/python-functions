"""
Task 1: Write a function that lets the user add items to a list.
"""



def add_item(selected_items):
    while True:
        input_items = input("Enter an item to your shopping cart or 'done' to finish: ").strip()
        if input_items.lower() == "done":
            break
        else:
            selected_items.append(input_items)

shopping_list = []
add_item(shopping_list)
print("Your shopping list:", shopping_list)