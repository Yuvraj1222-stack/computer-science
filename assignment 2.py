#author: Yuvraj Saini
# date: 1st september, 2025,monday
#description: bill division
price_bill=input('what is the total price of the bill? :')
people_shared=input('how many diners were there? :')
price_bill_total=int(price_bill)
total_people=int(people_shared)
bill_amount=(price_bill_total/total_people)
print('€',bill_amount)