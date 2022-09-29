def set_difficulty():
    difficulty = int(input("Please choose a level of difficulty from 1 to 5: "))
    return difficulty


def welcome(name=input("please enter your name: ")):
    print("Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    return name


def load_game():
    games = int(input("Please choose a game to play:\n 1. Memory Game - a sequence of numbers will appear for 1 second "
                      "and you have to guess it back \n 2. Guess Game - guess a number and see if you chose like the "
                      "computer\n 3. Currency Roulette - try and guess the value of a random amount of USD in ILS: \n "))

    while games not in range(1, 3):
        games = input("Please choose the game to play, 1,2,3 ")

    difficulty = set_difficulty()

    while difficulty not in range(1, 5):
        difficulty = input("Please choose a level of difficulty from 1 to 5: ")