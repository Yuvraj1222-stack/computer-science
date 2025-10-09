#Yuvraj
#Assignment Q5#

no = int(input('Input a digit or digits : '))
count = 1

while count != 50 and no:
    if count <= no :
        print(count,'squared', count ,'is',count*count)
    count += 1
    if count > no:
        break