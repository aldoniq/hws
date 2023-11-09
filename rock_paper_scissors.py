import random
from colorama import Fore, Back, Style, init


def get_user_choice():
    while True:
        user_choice = input("Выбери из этого списка:\n\t1) камень,\n\t2) ножницы,\n\t3) бумага\n -->").lower()

        choices = {
            "1":"камень",
            "2":"ножницы",
            "3":"бумага"
        }

        if user_choice in choices:
                user_choice = choices[user_choice]
                return user_choice
        else:
            print(Fore.RED + 'Выберите варианты которые представлены в списке.')
            print(Style.RESET_ALL)


def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return Fore.YELLOW + "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or (user_choice == "ножницы" and computer_choice == "бумага") or (user_choice == "бумага" and computer_choice == "камень"):
        return Fore.GREEN + "Поздравляю, ты победил!"
    else:
        return Fore.RED + "Компьютер победил."
    

init(autoreset=True)
print("Добро пожаловать в игру "+ Fore.GREEN + "'Камень, ножницы, бумага'")
print(Style.RESET_ALL)


while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Ты выбрал {user_choice}, компьютер выбрал {computer_choice}.")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    play_again = input("Хочешь сыграть еще раз? (y/n): ").lower()
    if play_again != "y":
        break
