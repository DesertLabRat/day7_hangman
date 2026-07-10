import random
from hangman_words import word_list
import hangman_art


chosen_word = random.choice(word_list)
print(hangman_art.logo)
lives = 6
guessed_letters = set()

while lives > 0:
    print(f"***** GUESSED LETTERS: {' '.join(sorted(guessed_letters))} *****")
    guess = input("Guess a letter: ").lower()
    print()
    display = ""

    if len(guess) != 1 or not guess.isalpha():
        print("***** INVALID INPUT TRY AGAIN *****")
        continue

    if guess in guessed_letters:
        print("***** LETTER ALREADY USED *****")
        continue
    elif guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"***** YOU LOST! THE WORD WAS {chosen_word} *****")
            break
        else:
            print(f"***** {guess} NOT IN THE WORD; LOSE A LIFE *****")

    guessed_letters.add(guess)

    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif letter in guessed_letters:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        game_over = True
        print(f"***** YOU WON! THE WORD WAS {chosen_word} *****")
        break
    else:
        print(hangman_art.stages[lives])
        print(" ".join(display))
        print()


