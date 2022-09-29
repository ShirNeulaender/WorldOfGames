import requests
import random
from Live import set_difficulty
from inputimeout import inputimeout, TimeoutOccurred

difficulty = set_difficulty()

generated_number = random.randint(1, 100)


def get_rate():
    exchange_rate_site = f"https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount={generated_number}"

    payload = {}
    headers = {
        "apikey": "t44ElVQBlOFs4LybEJND43lLNkOIXjEd"
    }

    response = requests.request("GET", exchange_rate_site, headers=headers, data=payload)
    return response.json()["info"]["rate"]


value_t = get_rate()
value_t = round(value_t, 2)


def get_money_interval():
    minimum = int(value_t - (5 - difficulty))
    maximum = int(value_t + (5 - difficulty))
    return minimum, maximum


def get_guess_from_user():
    try:
        user_input = inputimeout(
            prompt=f"You have 7 seconds to answer,what is the value of {generated_number} in USD? ", timeout=7)
        user_input = int(round(user_input, 2))

    except TimeoutOccurred:
        user_input = " "
        if user_input.isdigit() or user_input.replace(".", "", 1).isdigit():
            user_input = float(user_input)
        elif user_input == " ":
            pass
        else:
            user_input = 0
    return user_input


def play():
    minimum, maximum = get_money_interval()
    user_input = get_guess_from_user()
#    if user_input == " ":
#        print("It's been 7 seconds, sorry.")
#        return False
#    elif user_input == 0:
#        print("You needed to enter a number ")
#        return False
    print(f"The correct value is {value_t}₪,you needed to enter a number between {minimum} and {maximum}")
    mini = user_input > minimum
    maxi = user_input < maximum
    winning_status = (mini and maxi)
    print(winning_status)
    return winning_status
