# Master Yoda question

def master_yoda(sentence):
    word_list = sentence.split()
    new_words = word_list[::-1]
    return " ".join(new_words)

print(master_yoda("I am home"))
print(master_yoda("We are ready"))

#Almost there question

def almost_there(number):
    close_to_100 = abs(number - 100) <= 10
    close_to_200 = abs(number - 200) <= 10
    return close_to_100 or close_to_200

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

#Question 7

def has_33(numbers):
    index = 0

    while index < len(numbers) - 1:
        if numbers[index] == 3 and numbers[index + 1] == 3:
            return True
        index += 1

    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


# question 8


def paper_doll(word):
    final_word = ""

    for letter in word:
        final_word = final_word + (letter * 3)

    return final_word

print(paper_doll("Hello"))
print(paper_doll("Mississippi"))

#Question 9

def blackjack(num1, num2, num3):
    total = num1 + num2 + num3

    if total <= 21:
        return total

    elif 11 in [num1, num2, num3]:
        total = total - 10

        if total <= 21:
            return total

    return "BUST"

print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

#Question 10

def summer_69(numbers):
    total = 0
    ignore = False

    for num in numbers:

        if num == 6:
            ignore = True

        elif num == 9 and ignore:
            ignore = False

        elif not ignore:
            total += num

    return total

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

#Question 11

def spy_game(numbers):
    code = [0, 0, 7]

    for num in numbers:
        if num == code[0]:
            code.pop(0)

        if len(code) == 0:
            return True

    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
