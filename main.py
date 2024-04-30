import random

options = ("rock", "paper", "scissor")

running = True

while running:

    cpu =random.choice(options)

    player = None

    while player not in options:

        player = input("Enter choice...Rock, Paper, Scissor: ").lower()

        print(f"player: {player}")
        print(f"cpu: {cpu}")

        if player == cpu:

            print("It's a tie!!")
        elif player == "scissor" and cpu == "paper":

            print("you win")
        elif player == "paper" and cpu == "rock":

            print("you win")
        elif player == "rock" and cpu == "scissor":

            print("you win")
        else:

            print("you lose!!")

        ask = input("Do you want to continue? (y/n): ").lower()
        if ask == "n" or ask == "no":

            running = False
        elif ask == "y" or ask == "yes":

            running = True
        else:
            print("you entered unknown data")
            running = False
print("Thanks for playing")