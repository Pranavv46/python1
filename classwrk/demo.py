# Create a multiline string for the receipt header
header = """\n\t--- BOOKSTORE RECEIPT ---
\tName: Madison Bookstore
\t-------------------------\n"""

# Item details
item1 = "Book Title: {} \tPrice: ₹{}".format("Python Basics", 450)
item2 = "Book Title: {} \tPrice: ₹{}".format("Data Science Intro", 600)

# Calculate total
total_price = 450 + 600
total_line = "Total Amount: ₹{}".format(total_price)

# Thank-you message
thank_you = "\n\tThank you for shopping with us!\n"

# Combine all parts
receipt = header + item1 + "\n" + item2 + "\n" + total_line + thank_you

# Display in uppercase
print(receipt.upper())
