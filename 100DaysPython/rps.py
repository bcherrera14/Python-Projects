import random

rps = ["ROCK", "PAPER", "SCISSORS"]

user_choice = rps[int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))]
comp_choice = rps[random.randint(0,2)]

print(f"Me: {user_choice} vs Computer: {comp_choice}")

if user_choice == "ROCK":
    if comp_choice == "PAPER":
        print("You Lose.")
    elif comp_choice == "SCISSORS":
        print("You Win!")
    else:
        print("It's a Draw.")

if user_choice == "PAPER":
    if comp_choice == "ROCK":
        print("You Win!")
    elif comp_choice == "SCISSORS":
        print("You Lose.")
    else:
        print("It's a Draw.")

if user_choice == "SCISSORS":
    if comp_choice == "ROCK":
        print("You Lose.")
    elif comp_choice == "PAPER":
        print("You Win!")
    else:
        print("It's a Draw.")


