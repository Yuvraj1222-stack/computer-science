#Yuvraj
#assignment 8 Q18
X = int(input("Enter an integer X: "))
temp = X
count = 0
while temp > 0:
    temp = temp // 10
    count = count + 1
temp = X
while temp >= 10:
    temp = temp // 10
msd = temp
Y = count * 10 + msd
print("Y is:", Y)
