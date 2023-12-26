######################
#    Hangman Game    #
######################

import random
import os
import hangman_art
import hangman_words

######################
#     Functions      #
######################
def showBoard(livesLeft):
    print(hangman_art.stages[livesLeft])

def checkWon(word):
    if "_" not in word:
        return True
    else:
        return False

def newGame():
    while True:
        try:
            answer = input('\nWould you like to play again? Y/N\n').lower()
            if answer.lower() == 'y':
                return(True)
                break
            elif answer.lower() == 'n':
                return(False)
                break
            else:
                print('Error:  Please enter Y or N.')
        except ValueError:
            print('Invalid choice:  Please enter Y or N.')
######################
#    Function End    #
######################
playAgain = True
while playAgain != False:

    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"
    os.system('clear')
    print(hangman_art.logo)
    while not end_of_game:
        showBoard(lives)
        guess = input("\nGuess a letter: ").lower()
        os.system('clear')

        if guess in display:
            print(f'\nYou\'ve already guessed letter {guess}. Please try again.')
        else:
            #Check guessed letter
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
        #Check if user is wrong.
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                showBoard(lives)
                print(f'You lose, the word was {chosen_word}.')
                if newGame() != True:
                    playAgain = False
                    break
            else:
                print(f'Sorry, letter {guess} is not in the word. You lose a life.')
    
        #Join all the elements in the list and turn it into a String.
        print()
        print(f"{' '.join(display)}")

        #Check if user has guessed all letters.
        if checkWon(display):
            end_of_game = True
            print("\nCongratulations, you won the game.")
            if newGame() != True:
                playAgain = False
            else:
                os.system('clear')

print('\nThanks for playing Hangman, see ya next time!')