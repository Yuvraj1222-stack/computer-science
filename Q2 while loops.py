# Yuvraj
# Q2, while loops

grade = -1
total =0
count = 0
while grade!= '':
    grade = input('enter your grades')
    if grade.isdigit():
        total = total + int(grade)
        count = count + 1
        average = (total/count)

print(average)

if(average>=90):
     print('Your Grade is A , Congratulations!')
        
elif(average<=89)and(average>=80):
     print('Your Grade is B , Good!')
        
elif(average>=79)and(average>=70):
     print('Your Grade is C , You are doing Okay!')
        
elif(average>=69)and(average>60):
    print('Your Grade is D , we need to push up this , you can do much better!')
     
else:
    print('Your Grade is F , we need to put you up for adoption!')
