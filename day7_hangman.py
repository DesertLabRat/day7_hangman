import random
from hangman_words import word_list
import hangman_art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}")
print(hangman_art.logo)
lives = 6
correct_letters = []
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess not in alphabet:
        print("***** NOT IN ALPHABET TRY AGAIN *****")
        exit

    if guess in correct_letters:
        print("***** LETTER ALREADY USED *****")
    elif guess not in chosen_word:
        if lives == 0:
            game_over = True
            print(f"***** YOU LOST! THE WORD WAS {chosen_word} *****")
        else:
            print(f"***** {guess} NOT IN THE WORD; LOSE A LIFE *****")
            lives -= 1

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(hangman_art.stages[lives])
    print(display)
    print()
    if "_" not in display:
        game_over = True
        print("***** YOU WON! *****")

