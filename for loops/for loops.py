#for loops
#for loops are used to iterate over a sequence
#So for us, a string or a range of numbers

# to loop through the numbers 1 -5
for i in range (6):
    print(i, end=',')
fruit = input ('enter a fruit')
for letter in fruit:
    for i in range (3):
        print(letter)
