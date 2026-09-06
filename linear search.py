def linear_search(list_items, x):
    
    for index in range(len(list_items)):
        if list_items[index] == x:
            return index  
    return -1

listx = [10,5,6,23,67]

resultx = linear_search(listx,23)
print(resultx)