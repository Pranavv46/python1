"""
You are helping a shopper manage their grocery shopping list. Your task is to create a simple Python program that does the following steps in order:
Initial Grocery List:
Create a list with the initial items: ["milk", "bread", "eggs"].
Add Item Function:
  Write a function add_item(item) that adds a given item (string) to the grocery list.
Remove Last Item Function:
  Write a function remove_last_item() that removes the last item from the grocery list.
Lambda Function for Display:
Use a lambda function to print each item in the list with the format: "Item: <item>".
Recursive Character Count (Bonus):
Write a recursive function count_characters(items) that returns the total number of characters in all item names combined. For example, ["milk", "bread"] has 4 + 5 = 9 characters..
"""
grocery_list=["milk","bread","eggs"]

def add_item(item):
    grocery_list.append(item)
    print(f"✅'{item}' added to the list")

def remove_last_item():
    if grocery_list:
        removed =grocery_list.pop()
        print(f"🗑️ '{removed}' removed grom the list")
    else:
        print(f"⚠️ the list is LREdy empty")

display_item = lambda item:print(f"item:{item}") 

def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])

print("Initial grocery list:", grocery_list)

add_item("butter")
add_item("juice")
remove_last_item()

print("\n🛒 Current Grocery List:")
for item in grocery_list:
    display_item(item)

total_chars = count_characters(grocery_list)
print(f"\n🔤 Total number of characters in all item names: {total_chars}")    