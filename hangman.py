import random


words = ["hello"]

def choose_random_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    print("Добро пожаловать в игру 'Виселица'!")
    word = choose_random_word()
    guessed_letters = []
    attempts = 6

    while True:
        displayed = display_word(word, guessed_letters)
        print(displayed)

        if displayed == word:
            print("Поздравляю, ты угадал слово!")
            break

        if attempts == 0:
            print(f"Игра окончена. Загаданное слово было '{word}'.")
            break

        guess = input("Угадай букву: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Ты уже угадал эту букву.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Неверно. Осталось {attempts} попыток.")
        

hangman()
