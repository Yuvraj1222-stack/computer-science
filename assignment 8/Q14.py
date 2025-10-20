#Yuvraj
#assignment 8 Q14
N = int(input("Enter N (N > 20): "))
if N <= 20:
    print("Please enter a number greater than 20")
else:
    i = 11
    while i <= N:
        if i % 3 == 0 and i % 7 == 0:
            print("TipsyTopsy")
        elif i % 3 == 0:
            print("Tipsy")
        elif i % 7 == 0:
            print("Topsy")
        else:
            print(i)
        i = i + 1
