header = """\n\t--- BOOKSTORE RECEIPT ---
\tName: Madison Bookstore
\t-------------------------\n"""

item1 = "Book Title: {} \tPrice: ₹{}\n".format("Python Basics", 450)
item2 = "Book Title: {} \tPrice: ₹{}\n".format("Data Science Intro", 600)

Totalprice=450+600
total_line="Total amount: ₹{}".format(Totalprice)

thank="\nThanku for shopping from us\t"

recipt=(header+item1+item2+total_line+thank)
print(recipt.upper())