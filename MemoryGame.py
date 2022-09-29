import os
import random
from Live import set_difficulty
from time import sleep

difficulty = set_difficulty()


def generate_sequence():
    random_numbers_list = []
    for i in range(difficulty + 1):
        random_number = random.randrange(1, 102, 1)
        random_numbers_list.append(random_number)
    return random_numbers_list


def get_list_from_user():
    user_number_list = []
    for i in range(difficulty + 1):
        user_input = int(input(f"Please enter one of the number you saw "))
        user_number_list.append(user_input)
    return user_number_list


def is_list_equal(random_numbers_list, user_number_list):
    print(random_numbers_list)
    print(user_number_list)
    return random_numbers_list, user_number_list


def play_mem():
    gs = generate_sequence()
    print(gs)
    sleep(0.7)
    os.system('cls')
    gsu = get_list_from_user()
    print(f"The random generated numbers are {gs}")
    print(f"The numbers that you entered are {gsu}")
    is_list_equal(gs, gsu)
    winning = (gs == gsu)
    print(winning)
