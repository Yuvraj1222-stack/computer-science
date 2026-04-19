#Yuvraj
# while loops, Q7
xy = 1
while xy!= '' :
    number = int(input('enter your number : '))
    if number >= 10 and number <= 20 :
        print('Thank you!')
        break
    elif number < 10 :
        print('too Low')
    elif number > 20 :
        print('too High')
