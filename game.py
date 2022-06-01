import random

user = input("Enter a choice (R, P, S): \n")
possible_actions = ["R", "P", "S"]
computer = random.choice(possible_actions)
print(f"\nYou chose {user}, computer chose {computer}.\n")

if user == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user == "R":
    if computer == "S":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "P":
    if computer == "R":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "S":
    if computer == "P":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
        
        
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
    	print(user)
