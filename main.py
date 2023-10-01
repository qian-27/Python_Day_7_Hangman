import random
from hangman_art import logo, stages
from hangman_words import word_list
# from replit import clear

#Print the hangman logo at the start of the game.
print(logo)

#Randomly choose a word from the word_list
chosen_word = random.choice(word_list)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"

# Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters or lost all 6 lives.
end_of_game = False
while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    # Clear the ASCII art from previous 'stages'
    # clear()
    
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    #If the guess letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not int the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
