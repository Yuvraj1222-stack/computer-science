#Question16_B_OL
#Enter your name here: Yuvraj


print(' Welcome to Your weekly step tracker! ')
days=[1,2,3,4,5,6,7]
name=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
list1=[]
for i in range(0,7):
    steps=int(input(f'Please enter the steps you did on  {name[i]}'))
    list1.append(steps)
print('The list of steps is : ',list1)
print('The total steps taken this week was : ',sum(list1))
avg=sum(list1)/len(list1)
print('The average number of steps is :',round(avg,2))
print('The largest number of steps you took this week was :', max(list1))
print('The smallest number of steps you took this week was :',min(list1))