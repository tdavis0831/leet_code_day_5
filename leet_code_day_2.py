print(
    "Starting your Mars Adventure! \n Booting up... \n All systems go! \n Let's start!"
)

print()

name = input("What's your name?  ")
name = name.title()

print()

print(f"Hi {name} --- Welcome to your Mars Adventure!")
print("Yesterday, your received a call from your good friend at NASA.")
print("They need someone to go to Mars this weekend and YOU'VE been chosen!!")

print()

excited = input("Are you excited? Type Y or N  ")
excited = excited.upper()

if excited == "Y":
    print("I knew you'd say that. It's so cool that you're going to Mars!")
else:
    print("Well, it's too late to back out now.")
print()
print("It's time to pack for your trip to Mars.")
print()

#SUITCASES
suitcases = int(input("How many suitcases do you plan to bring?  "))

while True:

    if suitcases > 2:
        print("That's way too many. You'll have to pack more lightly.")
        suitcases = int(input("How many suitcases do you plan to bring?  "))

    if suitcases <= 2:
        print("Perfect. You'll certainly fit in the spaceship!")
        break

#COMPANION ANIMAL
print()
print("You're allowed to bring one companion animal with you.")

# print()

animal_type = input("What kind of companion animal would you like to bring?  ")
animal_type = (animal_type.title())

animal_name = input("What's your companion name?  ")
animal_name = (animal_name.title())

print()

print(f"Cool! so you're bringing {animal_name} the {animal_type}")

print()

#DECOR

print("Nasa can help you to decorate your space ship")
print("You have a few options for the interior decor to choose:")
print("A) Minimalist. Not much decoration, just the necessary.")
print("B) Vintage. Some touch of the 80's")
print("C) Hippie style!")

decor_choice = input("Which decoration would you like to choose? A, B or C  ")
decor_choice = (decor_choice.lower())

if decor_choice == "A":
    decor = "Minimalist"

if decor_choice == "B":
    decor = "Vintage"

if decor_choice == "C":
    decor = "Hippie Style"

print()

print("I can see it now:")
print(    f"{name} and {animal_name} the {animal_type} surfing the celestial abyss...")
print(f"in a {decor} spaceship!")

print()

mars = input("Let's go! Press ENTER")
#COUNTDOWN

import time

timer = 5

while timer > 0:
    print(timer, "...")
    time.sleep(1)
    timer = timer - 1

print("**** LIFTOFF ****")

print()

print("Record your observations:")
print()


def observation():
    observation = input("What do you see?  ")


while observation:
    observation = input("What do you see? ")
    observation = observation.title()

    if observation == "":
        break

    if not observation.endswith("."):
        observation = (f"{observation}.")
        print(f"Noted: {observation}")

print()

print("Finished observations.")

print()

# LANDED ON MARS

print(
    "You're about to land on Mars! \n ... \n The landing was successful. \n Time to disembark! \n ...but first, you need the door code to unlock the ship."
)

print()

correct_code = "8888"
numb_wrong_guess = 0
guess_code = input("Guess the code:   ")

while True:
    if guess_code == correct_code:
        break
        print("Correct! Welcome to Mars!")

    if not guess_code == correct_code:
        print("Sorry, you guessed wrong. Try again")
        numb_wrong_guess = numb_wrong_guess + 1
        print(f"Wrong guess: {numb_wrong_guess}")
        guess_code = input("Guess the code:  ")

    if guess_code != correct_code:
        print("Invalid door code. Enter 4 numbers only.")
        print(f"Wrong guess: {numb_wrong_guess +1}")
        guess_code = input("Guess the code:  ")

print("Welcome to Mars!")

print()

print(
    "Everything is so beautiful.. You're mesmerized by how red and super-bright it is..."
)
print("Oh no! The 'whoosh-whoosh' of a stun laser!")
print("Wait, that is...\nDARTH COBOL!")
print(
    "It looks like you'll have to duel her...\nFortunately, NASA equipped you with your own stun laser."
)
print(
    "Stun lasers don't always hit their targets. You only have one-in-two chance of hitting her. \nFortunately her laer is terrible and she'll always miss you."
)

print()

import random

health = 4

while health > 0:
    fire = input("Press ENTER to fire:")
    fire_shot = random.randint(1, 2)

    if fire_shot == 1:
        print("You hit Darth COBOL!")
        health = health - 1
        print(f"Darth COBOL health: {health}")
        print()

    if fire_shot == 2:
        print("You miss!")
        print(f"Darth COBOL health: {health}")
        print()

print()

print("After defeating Darth COBOL, it's finally time to go back home!")
print()

import time

numb_times = 0
liftoff = input("Are you ready to go back? Press ENTER")
print()

while numb_times < 3:

    timer = 5

    while timer > 0:
        print(timer, "...")
        time.sleep(1)
        timer = timer - 1
    numb_times = numb_times + 1

print("*** LIFT OFF ***")
