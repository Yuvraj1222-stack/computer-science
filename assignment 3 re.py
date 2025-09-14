# Yuvraj Saini
#Code for sum of all number from 1 to a give number. 


n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum is:", total)
