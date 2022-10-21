
### Setup Section ###

from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]
    secretWord = actual
    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if letter in secretWord: 

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secretWord[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:

        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
        
    # ...but if the letter is not in the word at all...
    else:
      
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
      
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")


# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###
    
# introduce the rules and the game to the user 
print("Hello welcome to Wordle!!")
print()
print("here are the rules to the game: ")
print()
print("You have to guess a six letter word: ")
print()
print("You only will only have six tries: ")
print()
print("If you guess the correct letter it wil be green: ")
print()
print("If you misplace a letter it will be yellow: ")
print()
print("If you input a wrong letter it will display red: ")
print()
#Tools to help create the game 
def getSixLetterInput():
  guess1 = " "
  while len(guess1) !=6: 
    guess1 = input("Please enter a six letter word:")
  return guess1.lower()
# count variable to hold guesses
guessCount = 0
secretWord = "jazzed"
userGuess = " "
    #create loops to show outcomes of Wordle
while guessCount <=6 and userGuess != secretWord:
     userGuess = getSixLetterInput()
     printGuessAccuracy(userGuess, secretWord) 
     guessCount +=1 
if userGuess == secretWord:
  print("Congraulations YOU WON!!!! Play again? ")
else: userGuess != secretWord
  
print("You lose... Would you like to play again? ")
