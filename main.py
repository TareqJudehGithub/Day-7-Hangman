from random import choice

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
display = []

# For each letter in the chosen_word, add a "_" to 'display'.
for letter in range(len(chosen_word)):
  display += "_"
  
print(display)

# While "_" is still in display, keep repeating untill all strings are displayed instead:
while "_" in display:

  # Ask the user to guess a letter and assign their answer to a variable called guess:
  guess = input("Guess a letter: ").lower()

  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  if guess not in chosen_word:  
    print(f"{guess} is not in {chosen_word}.")

  for position in range(len(chosen_word)):
    letter = chosen_word[position]

    if letter == guess:
      print(f" {letter} letter position is : {position}")
      display[position] = letter

  print("")

  print(display)

print("")
if "_" not in display:
  print("You Win!")



 
