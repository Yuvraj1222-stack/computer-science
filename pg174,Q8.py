# pg174 , Q8 , Yuvraj

cm = float(input("Enter your height in cm: "))
inches_total = cm / 2.54
feet = int(inches_total // 12)
inches = inches_total % 12

print("Height =", feet, "feet and", round(inches, 2), "inches")
