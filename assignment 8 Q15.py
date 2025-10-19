#Yuvraj
#assignment 8 Q15
numbers = input("Enter numbers separated by spaces: ")
numbers = numbers.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
largest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
print("Largest number is:", largest)
