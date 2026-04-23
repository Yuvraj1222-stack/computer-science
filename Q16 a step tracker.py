#Question16_A_OL
#Enter your name here : Yuvraj
 
print("Welcome to the Step Tracker App!")
name=input('Please enter your name: ')
steps_today = int(input("Enter the number of steps you walked today : "))#this is where the user enters the numbers of steps they walked
hello=0
while hello==0:
    if steps_today<0:
        print('The number of steps cannot be negative')
        break
    elif steps_today<5000:
        print('Try to be more active today',name)
        break
    elif steps_today >=10000:
        print("Well done",name,"! You reached your goal!")
        break
    else:
        print('Good effort',name,'! Almost there.')
        break
