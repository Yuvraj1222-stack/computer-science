# Yuvraj
# assignment 7 Q2


count_p = 0
count_n = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break
    elif num > 0:
        count_p += 1
    else:
        count_n += 1

print("Count of positive numbers:", count_p)
print("Count of negative numbers:", count_n)
