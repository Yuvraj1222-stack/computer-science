# Yuvraj Sain
# for loops assignment re:

# program to print even numbers in a range
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)