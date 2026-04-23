# Question 16(a)
# Name and School: Yuvraj Saini

principal=int(input('Enter the principal(original) investment amount: €'))
interest=float(input('Enter the annual(yearly) interest rate (e.g. 0.05 for 5% interest): '))
value=principal
for i in range(1,11):
    value+=(interest*value)
    end=str(round(value,2))
    print('Year',i,'- Investment value: €'+end)  
