num_check = int(input("Enter a number: "))

if num_check < 10:
    print("Too low")
elif 10 <= num_check <= 20:
    print("Correct")
else:
    print("Too high")
