'''
Yuvraj Saini
Lists , the book pg 371 to 379

'''
#11.61A

lst1=[10,12,14]
lst1.append(16)
print(lst1)

#11.61B

val=[17,24,15,30]
val.extend([34,27])
print(val)

#11.4 , Write a program that asks the user to input a number a list to be appended to an existing list .Whether the user enters a single number or a list of numbers,the prgram should append the list accordingly.
#eval is a function , Never Use in LC code

myl = [2,4,6]
print("Existing list is :", myl)
n = eval(input("Enter a number or a list to be appended:"))
if type(n) ==type([]):#if a list is input
    myl.extend(n)
elif type(n) == type(1): #if an integer is input
    myl.append(n)
else:
    print("Please enter either an integer or a list.")
print("Appended List is : ",myl)

#11.6.2
#Inserting an element in a list

val=[17,24,15,30]
val.insert(2,33) #add number 33 at third position(index 2)
print('11.62 list',val)

#11.6.3
#modifiying/Updating Elements to a list

lst=[10,12,14,16]
lst[2] = 24
print(lst)

#11.6.4A
#deleting an Element from a list using its Index/position
val=[17,24,33,15,30]
deleted_val=val.pop(2)
print('this is the deleted element',deleted_val)
print('11.6.4A list:',val)#prints list without the deleted

#11.6.4B
#deleting an element using its value

val=[17,24,33,15,30]#to delete 24, write as follows:
val.remove(24)
print('11.6.4B ',val)

#11.6.4C,deleting a sublist from a list

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
del lst[10]#deletes num at position 10 , so deletes 11
print('11.6.4C list ',lst)

#11.5 program for displaying options for inserting or deleting elements in a list , if the use chooses a deletion option, display a submenu and ask if element is to deleted with value or by using it postion or a list slice is to be deleted.

val=[17,23,18,19]
print('the list is:',val)
while True :
    print("main Menu")
    print("1.Insert")
    print("2.Delete")
    print("3.Exit")
    ch =int(input("Enter you choice 1/2/3 :"))
    if ch == 1:
        item = int(input("Enter item:"))
        pos = int(input("Insert at a which position?"))
        index = pos - 1
        val.insert(index,item)
        print("Success! List now is:",val)
    elif ch == 2:
        print(" Deletion Menu")
        print("1. Delete using Value")
        print("2. Delete using index")
        print("3. Delete a sublist")
        dch = int(input("Enter choice(1 or 2 or 3):"))
        if  dch == 1:
            item = int(input("Enter item to be deleted:"))
            val.remove(item)
            print("List now is :",val)
        elif dch == 2:
             index = int(input("Enter index of item to be deleted:"))
             val.pop(index)
             print("List now is:",val)
        elif dch == 3:
            l =int(input("Enter lower limit of list slice to be deleted:"))
            h = int(input("Enter upper limit of list slice to be deleted:"))
            del val[1:h]
            print("List now is:",val)
        else:
            print("valid choices are 1/2/3 only.")
    elif ch == 3:
        break;
    else :
        print("valid choices 1/2/3 only.")

#11.6 Write a program that inputs a list , replicates it twice and then prints the sorted list in ascending and descending orders:

val = eval(input("Enter a list :"))
print("Original list :", val)
val = val * 2
print("Replicated list :",val)
val.sort()
print("Sorted in ascending order :",val)
val.sort(reverse = True)
print("Sorted in descending order :",val)

#11.7 program to find the minimum element from a list of element along with its index in the list.

lst = eval(input("Enter list :"))
length = len(lst)
min_ele = lst[0]
min_index = 0
for i in range(1,length):
    if lst[i] < min_ele :
        min_ele = lst[i]
        min_index = i
print("Given list is :",lst)
print("The minimum element of the given list is :")
print(min_ele,"at index",min_index)


#11.8 program to calculate the mean of a give list of numbers

lst = eval(input("Enter list : "))
length = len(lst)
mean = sum = 0
for i in range(0,length):
    sum += lst[i]
mean = sum/length
print("Given list is : ",lst)
print("The mean of the given list is :",mean)

#11.9 program to search for an element in a given list of numbers

lst = eval(input("Enter list :"))
length = len(lst)
element = int(input("Enter element to be searched for :"))
for i in range (0,length):
    if element == lst[i]:
        print(element ,"found at index",i)
        break
else :    #else of for loop
    print(element,"not found in given list")
    
#11.10 Program to count the frequency of a given element in a list of numbers.
lst = eval(input("Enter list :"))
length = len(lst)
element = int(input("Enter element :"))
count = 0
for i in range(0,length):
    if element == lst[i]:
        count +=1
if count == 0:
    print(element,"not found in given list")
else:
    print(element,"has frequency as",count,"in given list")
    
#11.11 program to find frequencies of all elements of a list.Also,print the list of unique elements in the list and duplicate elements in the given list.
lst = eval(input("Enter list :"))
length = len(lst)
uniq =[]    # list to hol unique elements
dupl =[]    # list to hold duplicate elements
count = i = 0
while i < length:
    element = list[i]
    count = 1        # count as 1 for the element at lst[i]
    if element not in uniq and element not in dupl:
        i += 1
        for j in range(i,length):
            if element == lst[j]:
                count += 1
        else:   # When inner loop - for loop ends
            print("Element",element,"frequency:",count)
            if count == 1:
                uniq.append(element)
            else:
                dupl.append(element)
    else:   # When element is found in uniq or dupl lists
        i += 1
        
        
print("Original list",lst)
print("Unique elements list",uniq)
print("Duplicates elements list",dupl)

#11.12 Write a program to check if the maximum element of the list lies in the first half of the list or in second half.

lst = eval(input("Enter a list:"))
ln = len(lst)
mx = max(lst)
ind = lst.index(mx)
if ind <= (ln/2):
    print("The maximum element",mx,"lies in the 1st half.")
else:
    print("The maximum element",mx,"lies in the 2nd half.")
        
#11.15 Write a program to input two lists and display the maximum element from the elements of both the lists combined, along with its index in its list.
        
lst1 = eval(input("Enter list1:"))
lst2 = eval(input("Enter list2:"))
mx1 = max(lst1)
mx2 = max(lst2)
if mx1 >= mx2:
    print(mx1,"the maximum value is in list1 at index",lst1.index(mx1))
else:
    print(mx2,"the maximum value is in list2 at index",lst.index(mx2))
    