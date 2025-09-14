# Yuvraj Saini

# A programm for printing the sum of all odd numbers only from 1 to any given number


n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        total = total + i

print("Sum of odd numbers is:", total)
