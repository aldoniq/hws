import random

number = random.randint(1, 100)

print("Welcome to the 'Guess the Number' game!")
print("I'm thinking of a number between 1 and 100. Try to guess it.")

attempts = 0

while True:

    guess = input("Enter a number: ")
    
    attempts += 1
    
    try:
        assumption = int(guess)
    except ValueError:
        print("Please enter an integer.")
        continue
    
    if assumption < number:
        print("My number is higher. Try again.")
    elif assumption > number:
        print("My number is lower. Try again.")
    else:
        print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
        break
