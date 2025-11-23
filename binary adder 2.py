b1 = input("Enter first binary number: ")
b2 = input("Enter second binary number: ")

while len(b1) < len(b2):
    b1 = "0" + b1
while len(b2) < len(b1):
    b2 = "0" + b2

carry = 0
result = ""

i = len(b1) - 1
while i >= 0:
    d1 = int(b1[i])
    d2 = int(b2[i])
    total = d1 + d2 + carry

    if total == 0:
        result = "0" + result
        carry = 0
    elif total == 1:
        result = "1" + result
        carry = 0
    elif total == 2:
        result = "0" + result
        carry = 1
    else:
        result = "1" + result
        carry = 1

    i -= 1

if carry == 1:
    result = "1" + result

print("The sum is:", result)
