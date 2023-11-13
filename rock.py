import random
import string

# define our options
myTuple = ("rock", "paper", "scissors")

for i in range(5):

    # get user input
    userChoice = input("Make your choice: ")
    userChoice = userChoice.lower()

    # make sure input is valid
    while userChoice not in myTuple:
        userChoice = input("Make your choice (rock, paper, or scissors): ")
        userChoice = userChoice.lower()

    # generate a random choice for the computer
    compChoice = random.choice(myTuple)
    print("The computer has chosen", compChoice)

    # compare user and computer choices and determine a winner
    if userChoice == compChoice:
        print("It's a tie!")
    elif userChoice == "rock" and compChoice == "paper":
        print("You lose...")
    elif userChoice == "rock" and compChoice == "scissors":
        print("You win!")
    elif userChoice == "paper" and compChoice == "rock":
        print("You win!")
    elif userChoice == "paper" and compChoice == "scissors":
        print("You lose...")
    elif userChoice == "scissors" and compChoice == "rock":
        print("You lose...")
    elif userChoice == "scissors" and compChoice == "paper":
        print("You win!")
