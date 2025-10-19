#Yuvraj
#assignment 8 Q20a
seq1 = []
num = 2
for i in range(7):
    seq1.append(num)
    num = num + 3
seq2 = []
num = 9
for i in range(7):
    seq2.append(num)
    num = num + 4
total = 0
for i in range(7):
    total = total + seq1[i] + seq2[i]
print("Sum of sequences is:", total)
