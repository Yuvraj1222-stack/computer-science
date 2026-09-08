def binary_search(y_list, target):
    low = 0
    high = len(y_list) - 1

    while low <= high:
        middle = (low + high) // 2

        if y_list[middle] == target:
            return middle
        elif y_list[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1


numbers = [2, 4, 5, 7, 9, 12, 15]
print(binary_search(numbers, 12))
print(binary_search(numbers, 4))
