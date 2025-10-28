apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25

total_volume = apple_juice + orange_juice + grape_juice

print("Total volume sold:", total_volume, "liters")

total_int = int(total_volume)
print("Total volume (integer):", total_int, "liters")

total_str = str(total_volume)
print("The total volume sold today is " + total_str + " liters.")
import random
bonus = random.randint(5, 10)
final_total = total_volume + bonus
print("Final total including bonus:", final_total, "liters")
print (globals())