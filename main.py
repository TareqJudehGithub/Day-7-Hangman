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

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess # lowercase.
guess = input("Guess a letter: ").lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
check_answer = guess in chosen_word
if check_answer:
  print("Right")
else:
  print("Wrong")

print("")

#If the letter at that position matches 'guess' then reveal that letter in the display at that position.

for position in range(len(chosen_word)):
  letter = chosen_word[position]

  if letter == guess:
    print(f" {letter} letter position is : {position}")
    display[position] = letter

print("")

# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

print(display)



 
