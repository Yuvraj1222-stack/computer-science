# pg 174 , Q7 , Yuvraj

marks = []
for i in range(5):
    m = float(input("Enter marks of subject " + str(i+1) + ": "))
    marks.append(m)

average = sum(marks) / 5
print("Average marks =", average)
