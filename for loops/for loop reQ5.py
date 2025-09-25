running_total = 0
for i in range(5):
    num_input = int(input(f"Enter number {i+1}: "))
    add_choice = input("Do you want to add this number to the total? (yes/no): ")
    if add_choice.lower() == "yes":
        running_total += num_input

print(f"Your final total is {running_total}")
