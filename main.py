from random import choice
from hangman_words import word_list
from hangman_art import game_stages, logo
from replit import clear

stages = game_stages
words_list = word_list
game_over = False
print(logo)
print("")

# Randomly choose a word from the word_list:
chosen_word = choice(words_list)
# Creating a variable called 'lives' to keep track of the number of lives left:
lives = 6
print(f"Lives left: {lives}")
 # Display the hangman stages ASCII bases on lives left:
print(stages[lives])
print("")
# Creating an empty List called display:
display = []

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# For each letter in the chosen_word, add a "_" to 'display'.
for letter in range(len(chosen_word)):
  display += "_"
print(display)
print("")

# While "_" is still in display, keep repeating untill all strings are displayed instead:
while game_over == False and lives > 0:
  # Ask the user to guess a letter and assign their answer to a variable called guess:
  print("")
  guess = input("Guess a letter: ").lower()
  clear()
  print('''
  ''')

  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  if guess not in chosen_word:  
    wrong = choice(
      [
        f"Wrong answer! '{guess}' is not a match.",
        "NO NO NO!",
        "Wrong answer, keep trying!"
      ]
    )
    print(wrong)
    lives -= 1
    print("")
    print(f"Lives left: {lives}")
    if lives == 0:
      print("Game Over!")
     # Display the hangman stages ASCII bases on lives left:
    print(stages[lives])
    print('''
    ''')
  elif guess in display:
        print(f"You've already guessed letter '{guess}'.")
        print('''
        ''')
  else:
    correct = choice(
      [
        "Correct! keep going you got this!",
        f"Yay! '{guess}' is a correct answer!",
        "Bravo!"
      ])
    print(correct)
    print('''
    ''')

  for position in range(len(chosen_word)):
    letter = chosen_word[position]

    if letter == guess:
      display[position] = letter

  print("")

  print(display)

  print('''
  ''')

  if "_" not in display:
    game_over = True
    print("You Win!")
    print("".join(display))
  



 
