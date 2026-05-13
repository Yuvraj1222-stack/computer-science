def ANIMAL_CRACKER(a):
    if a[0] == a[(a.index(' '))+1]:
        result='True'
    else:
        result='False'
    return result
Word=input('Enter a two string word: ')
X=ANIMAL_CRACKER(Word)
print(X)