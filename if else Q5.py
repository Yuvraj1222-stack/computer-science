raining = input("Is it raining? (yes/no): ")

if raining.lower() == "yes":
    windy = input("Is it windy? (yes/no): ")
    if windy.lower() == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
