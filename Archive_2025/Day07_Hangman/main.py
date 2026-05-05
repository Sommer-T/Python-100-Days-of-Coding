import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
display = ["_"] * word_length

guessed_letters = []

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.")
        continue
    else:
        guessed_letters.append(guess)

    # Check guessed letter
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"'{guess}' is not in the word. You lose a life.")
        lives -= 1

    print(" ".join(display))
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("🎉 You win!")

    if lives == 0:
        end_of_game = True
        print(f"💀 You lose! The word was: {chosen_word}")