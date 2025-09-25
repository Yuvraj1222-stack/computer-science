user_name = input("Enter your name: ")
repeat_count = int(input("How many times should the letters be printed? "))
for _ in range(repeat_count):
    for char in user_name:
        print(char)
