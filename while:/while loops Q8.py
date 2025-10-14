#Yuvraj
#while loops Q8

guess = 1
total = 0

while guess!= '' :
    number = int(input('Enter your number : '))
    if number == 25:
        print('Right on Target!')
        break
    elif number < 20 :
        print('too Low')
    elif number > 30 :
        print('too High')
    total += 1

print('Task took you',total,'Times to get it, Great Job!')
