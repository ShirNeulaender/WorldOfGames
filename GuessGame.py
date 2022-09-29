import random
from Live import set_difficulty

difficulty = set_difficulty()


def generate_number():
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user():
    user_guess = 0
    while user_guess < 1 or user_guess > difficulty:
        user_guess = input(f"Please guess a number between 1 to {difficulty} \n")
        return int(user_guess)


def compare_results(secret_number, user_guess):
    print(secret_number)
    print(user_guess)
    return secret_number == user_guess


def play_game():
    gn = generate_number()
    gsn = get_guess_from_user()
    print(f"The generated number is - {gn}")
    print(f"Your guess is - {gsn}")
    win = compare_results(gn, gsn)
    print(win)
