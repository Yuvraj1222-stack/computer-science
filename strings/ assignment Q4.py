#Yuvraj
#strings Q4
text = input("Enter a string: ")
char = input("Enter a character to count: ")

count = 0
for c in text:
    if c == char:
        count = count + 1

print("The character", char, "occurs", count, "times in the string")
