# binary adder assignment , Yuvraj
b1 = input("Enter the first binary number: ")
b2 = input("Enter the second binary number: ")

num1 = int(b1, 2)
num2 = int(b2, 2)
total = num1 + num2

binary_result = bin(total)[2:] 
print("The sum of the two binary numbers is:", binary_result)
