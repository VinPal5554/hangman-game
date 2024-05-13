import random
import hangman_art
import hangman_words

has_finished = False
lives = 6

# Randomly select a word for the game
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

print(hangman_art.logo)

# Generate the blank equivalent of the chosen word
display = []
for element in range(len(chosen_word)):
    display += "_"

while not has_finished:
    guess = input("Please guess a letter: ").lower()

    # Iterate through each letter in word and check if guess is correct
    for position in range (len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(hangman_art.stages[lives])
    if lives == 0:
        has_finished = True
        print("You Lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        has_finished = True
        print("You Win!")