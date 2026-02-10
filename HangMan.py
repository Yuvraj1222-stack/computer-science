# Hangman Game
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print("Welcome to Hangman.")
print("Please save his life by guessing the correct word.")

play_again = "y"
while play_again == "y":
    hang = 0
    secret_word = "computerscience"      
    guessed_letters = []      
    turns = 7                 

    print("\nGuess the word:")

    while turns > 0:
        display = ""

    
        for ch in secret_word:
            if ch in guessed_letters:
                display = display + ch
            else:
                display = display + "_"

        print("\nWord:", display)
        print("Lifes left:", turns)

    
        if "_" not in display:
            print("You guessed the word! You win!")
            
            break

        guess = input("Enter a character: ").lower()

    
        if guess in guessed_letters:
            print("You already guessed this letter.")
            print(HANGMANPICS[hang])
            continue

        guessed_letters.append(guess)

    
        if guess in secret_word:
            print("Good guess!")
            print(HANGMANPICS[hang])
        else:
            print("Wrong guess!")
            turns = turns - 1
            hang=hang+1
            print(HANGMANPICS[hang])


    if turns == 0:
        print("\nYou ran out of Lifes.")
        print("The secret word was:", secret_word)

    play_again = input("\nDo you want to play again? (y/n): ").lower()

print("Thank you for playing Hangman!")