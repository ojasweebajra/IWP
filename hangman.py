import random

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

words = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar", "coyote", "crow"]

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print("Missed letters: ", end = " ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=" ")
    print()

def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter:")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You've already guessed that letter. CHose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        else:
            return guess

def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

print("HANGMAN")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters+ guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes! The secret word is " + secretWord + " yOU'VE WON!")
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS)- 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("You've run out of guesses. \n After " + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guesses, the word was " + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
