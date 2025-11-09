#assignment 10
# Q3

x1 = input("Ënter your word") 
first = x1[0].lower()

other= x1[1:len(x1)]

result = other.replace(first, '$')

result = first + result
print(result)

 

