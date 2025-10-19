#Yuvraj
#assignment 8 Q16
numbers = input("Enter numbers separated by spaces: ")
numbers = numbers.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
largest = numbers[0]
second = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > largest:
        second = largest
        largest = numbers[i]
    elif numbers[i] > second and numbers[i] != largest:
        second = numbers[i]
print("Second largest number is:", second)
