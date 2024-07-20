import random

def play_game():
    """
    Play a game of Rock-Paper-Scissors.

    Returns:
        str: The result of the game (e.g. "You win!", "Computer wins!", "Tie!")
    """
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ").lower()

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

print(play_game())