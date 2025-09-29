# pg174 , Q11 , Yuvraj

P = float(input("Enter principal amount: "))
R = float(input("Enter annual rate of interest (%): "))
T = float(input("Enter time in years: "))

# Simple Interest
SI = (P * R * T) / 100

# Compound Interest (compounded annually)
A = P * (1 + R/100) ** T
CI = A - P

print("Simple Interest =", SI)
print("Compound Interest =", CI)
