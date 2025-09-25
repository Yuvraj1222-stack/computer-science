units_consumed = int(input("Enter number of units consumed: "))

if units_consumed <= 100:
    bill_cost = units_consumed * 0.05
elif units_consumed <= 250:
    bill_cost = (100 * 0.05) + ((units_consumed - 100) * 0.08)
else:
    bill_cost = (100 * 0.05) + (150 * 0.08) + ((units_consumed - 250) * 0.10)

print(f"Total water bill = ${bill_cost:.2f}")
