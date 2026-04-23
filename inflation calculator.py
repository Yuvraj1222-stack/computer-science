# Question 16(a)
# Name and School: Yuvraj Saini

print('''Household budget calculator. Enter the following
information''')
num_adults = int(input('Number of adults in household : '))
num_child = int(input('Number of children in household :  '))

food_budget = 300
cost_food_adults = 50
cost_food_child = 35

child_allowance = 140
inflation=float(input('Inflation rate (e.g. 0.05 for 5% inflation): '))
child =0
if num_child>3:
    print("Children’s allowance total: €", child_allowance*num_child+20*(num_child-3))
    child+=child_allowance*num_child+20*(num_child-3)
else:    
    print("Children’s allowance total: €", child_allowance*num_child)
    child=child_allowance*num_child
print("Total household food cost: €",cost_food_adults*num_adults+cost_food_child*num_child)
figure=(cost_food_adults*num_adults+cost_food_child*num_child)*(1+inflation)
actual=round(figure,2)
percent=str(round((figure/child)*100,2))
print('Total household food cost: €',actual)
print('Percentage spend on food: '+percent+'%')
print('Budget remaining after food spend:',child+food_budget-figure)