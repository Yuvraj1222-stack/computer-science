# yuvraj
# while loops , Q6

num = int(input('Input a number : '))
count = 0

while count != 50 :
    if count < 50 :
        num = int(input('Input a number : '))
    else :
        break
    
    count += num
    print(count)
