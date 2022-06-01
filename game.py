import random

user = input("Enter a choice (rock, paper, scissors): \n")
possible_actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)
print(f"\nYou chose {user}, computer chose {computer}.\n")

if user == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
        
        
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
    	print(user)
