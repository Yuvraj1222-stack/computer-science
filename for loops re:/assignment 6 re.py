# Yuvraj Saini

# program for counting the number of digits in a number
num = int(input("Enter a number: "))
count = 0

for digit in str(num):
    count = count + 1

print("Total digits:", count)
