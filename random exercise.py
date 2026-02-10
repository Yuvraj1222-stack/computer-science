
import random
rand1 = random.randint(1,100)
print(rand1)


lst1 =['apple' , 'dragonfruit' , 'mango' ,'cherry' , 'blackberries']
rand2 = random.choice(lst1)
print(rand2)

coin = ['heads' , 'tails']
x = random.choice(coin)
y = input('Take your guess!!:(Coinflip)')
if y == x:
    print('you win')
else:
    print('Better luck next time')
    
print (x , y)

randx = random.randint(1,100)
count = 0
x = int(input("make a guess (number 1- 100):"))
if x == randx:
    print("correct guess")
else:
    print("Try Again")
    
