import random
# indicator of a list is []
choices = ["rock", "paper", "scissors"]
playerChoice = input("Enter your choice (1-Rock, 2-Paper, 3-scissors): ")
playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be betrween 1 and 3!")
else:
    computerChoice = random.randint(1,3)
    if playerChoice == computerChoice:
        print("It's a Tie")
    elif playerChoice == 1 and computerChoice == 3:
        print ("Rock beats scissors - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print ("Paper beats Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2:
        print ("Scissors beats Paper - You win!")
    else:
        print(" You lose!")