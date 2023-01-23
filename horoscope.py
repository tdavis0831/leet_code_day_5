"""A horoscope game."""

import random

HOROSCOPE_DATA = {
    "animal": [
        "cat",
        "dog",
        "aardvark",
        "giraffe",
    ],
    "place": [
        "San Francisco",
        "The North Pole",
        "Timbuck2",
    ],
    "personality": [
        "adventurous",
        "persistent",
        "funny",
    ],
    "characteristic": [
        "conscientious",
        "creative",
        "capable",
    ],
}


def prints_greeting():
    """Prints the Introductory Greeting"""

    print("Welcome to my saloon.")
    print("Enter your birthday and I will show your horoscope.")


def get_user_birth():
    """Returns birthday as a list

    [month, day, year]
    """

    month = input("What month were you born in? ")
    day = input("What day of the month (1-31)? ")
    year = input("What year were you born? ")

    return [month, day, year]


def generate_horoscope(month, day, year):
    """Returns horoscope generated from the user's birthdates"""

    horoscope = (f"Here's your horoscope: \n"
        f"For someone born on {month} {day}, {year}. \n"
        f"You are {random.choice(HOROSCOPE_DATA['characteristic'])} and {random.choice(HOROSCOPE_DATA['personality'])}. \n"
        f"You will live in {random.choice(HOROSCOPE_DATA['place'])} and have a pet {random.choice(HOROSCOPE_DATA['animal'])}. \n")

    return horoscope


def ask_to_continue():
    """Ask user to continue"""

    playing = input("Do you want another horoscope?(type exit to exit) ")

    if playing == "exit" or playing == "no":
        return False

    return True


def run_horoscope():
    """Runs the horoscope game"""

    prints_greeting()

    playing = True

    while playing:

        birthday_info = get_user_birth()

        birth_month = birthday_info[0]

        birth_day = birthday_info[1]

        birth_year = birthday_info[2]

        a_horoscope = generate_horoscope(birth_month, birth_day, birth_year)

        print(a_horoscope)

        playing = ask_to_continue()


run_horoscope()
