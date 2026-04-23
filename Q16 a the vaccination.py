# Question 16(a) 
# Name and School: Yuvraj , A.C.C
 
import random
hello=0
vaccines=['A','B','C']
while hello<2:
    if hello==1:
        end=input("If you have finished entering people's details type 'END', otherwise press RETURN: ")
        if end=='END' :
            break
        elif end=='''
''':
            continue      
    s_name = input("Enter your surname: ")
    f_name = input("Enter your first name: ")
    age=int(input('Enter your age!: '))
    eircode=input('Enter your Eircode(e.g N37.. ): ')
    enrol=input('''Do you agree to enroll in a vaccine trial?
Type 'Yes' or 'No' ''')
    print("Hello", f_name, s_name,"you are",age,"years old and your Eircode is",eircode)
    last=int(eircode[-1])
    if last%2==0:
        print('You must attend Eastwood for your vaccine')
    else:
        print('You must attend Northfield for your vaccine')
    if enroll=='Yes':
        print('You are now enrolled in the trial to receive Super vaccine',random.choice(vaccines))
    else:
        if 12<=age<50:
            print(f_name+', you will receive the MRNA vaccine')
        elif age >= 50:
            print(f_name+', you will receive the ADENO vaccine')
    hello+=1