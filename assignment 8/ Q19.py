#Yuvraj
#assignment 8 Q19
n = int(input("Enter n: "))
m = int(input("Enter m: "))
i = 1
while i <= n:
    if i % m == 0:
        if i % 2 == 0:
            print(i, "is divisible by", m, "and is even")
        else:
            print(i, "is divisible by", m, "and is odd")
    i = i + 1
