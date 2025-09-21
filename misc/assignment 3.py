#author:Yuvraj Saini
# date: 1st september, 2025,monday
#description: pizza questonier
amount_pizza=input('how many slices of pizza did you start with? :')
ate_pizza=input('how many slices did you eat? :')
amount_pizza_num=int(amount_pizza)
ate_pizza_num=int(ate_pizza)
pizza_left=(amount_pizza_num - ate_pizza_num)
print(pizza_left)
