#Yuvraj
#String assignment 3

user = input('Enter a word :')
if(user[0]=='a'or user[0]=='i'or user[0]=='o'or user[0]=='e'or user[0]=='u'or user[0]=='A'or user[0]=='O'or user[0]=='U'or user[0]=='E'or user[0]=='I'):
    print(user+'way')

else:
    neword= ''
    for i in range(1,len(user)):
        neword=neword+user[i]
    neword= neword+user[0]
    print(neword+'ay')
        
