# Yuvraj Saini

# counting the even and odd numbers from user's input
even = 0
odd = 0

while True:
    n = input("Enter number (q to quit): ")
    if n == 'q':
        break
    n = int(n)
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even:", even)
print("Odd:", odd)
