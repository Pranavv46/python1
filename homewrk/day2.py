#step1
paragraph="""Python is an easy to learn, powerful programming language. 
This Python course helps beginners understand basic concepts
like syntax, variables, and functions effectively."""

#length
length =len(paragraph)
print("the length is :",length)

#dispaly
print("first character:",paragraph[0])
print("last character:",paragraph[-2])

#slice
preview = paragraph[:49]
print("\nPreview:", preview)

#replace
replaced=paragraph.replace("python","PYTHON")
print("\nAfter replacement:\n", replaced)