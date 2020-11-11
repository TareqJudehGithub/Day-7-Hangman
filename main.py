from random import choice


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
game_over = False
# Randomly choose a word from the word_list:
chosen_word = choice(word_list)
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

# While "_" is still in display, keep repeating untill all strings are displayed instead:
while game_over == False and lives > 0:
  # Ask the user to guess a letter and assign their answer to a variable called guess:
  print("")
  guess = input("Guess a letter: ").lower()
  print("")

  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  if guess not in chosen_word:  
    print(f"Wrong answer! {guess} is not a match.")
    lives -= 1
    print("")
    print(f"Lives left: {lives}")
     # Display the hangman stages ASCII bases on lives left:
    print(stages[lives])
  else:
    correct = choice(
      [
        "Correct! keep going you got this!",
        f"Yay! {guess} is a correct answer!",
        "Bravo!"
      ])
    print(correct)
  print("")

  for position in range(len(chosen_word)):
    letter = chosen_word[position]

    if letter == guess:
      display[position] = letter

  print("")

  print(display)

  print("")

  if "_" not in display:
    game_over = True
    print("You Win!")
    print("".join(display))
  
  if lives == 0:
    print("Game Over!")



 
