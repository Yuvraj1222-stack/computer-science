#Yuvraj
#Assignment 7 Q4

decimal = int(input("Enter a decimal number: "))

binary = ""

while decimal > 0:
    remainder = decimal % 2
    binary += str(remainder)  
    decimal = decimal // 2

print("Binary (reversed) is:", binary)
