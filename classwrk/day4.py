fruits=["apple","banana]","mango"]
vegetables=["tomato","potato","carrot"]
beverages=["tea","coffe","juice"]

fruits.append("orange")
vegetables.insert(1,"onion")
beverages.pop()

inventory=[fruits,vegetables,beverages]

print("first two fruits",fruits[:2])

print("last vegetables",vegetables[-1])

#list comprehension
fruits_length=[len(item) for item in fruits]
print("length of each item in fruits:",fruits_length)

is_water_present="water" in beverages
print("is 'water' is present:",is_water_present)

first_items = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items from each section:", first_items)
print("\nFull Inventory:", inventory)