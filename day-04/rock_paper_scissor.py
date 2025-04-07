# 07 April 2025

# Rock paper scissor

import random

computer_choice = random.choice(["rock", "paper", "scissors"])

user_choice = (input("Rock, Paper, Scissors? ")).lower()

print(f"Computer chose: {computer_choice}! You chose {user_choice}")

if computer_choice == 'rock' and user_choice == 'rock':
    print("It's a draw!")
elif computer_choice == 'rock' and user_choice == 'paper':
    print("You win!")
elif computer_choice == 'rock' and user_choice == 'scissors':
    print("You lost!")
elif computer_choice == 'paper' and user_choice == 'paper':
    print("It's a draw!")
elif computer_choice == 'paper' and user_choice == 'rock':
    print("You lost!")
elif computer_choice == 'paper' and user_choice == 'scissors':
    print("You win!")
elif computer_choice == 'scissors' and user_choice == 'scissors':
    print("It's a draw!")
elif computer_choice == 'scissors' and user_choice == 'paper':
    print("You lost!")
elif computer_choice == 'scissors' and user_choice == 'rock':
    print("You win!")
else:
    print("Input Error.")