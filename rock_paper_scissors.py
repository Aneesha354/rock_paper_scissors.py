import random

user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors (5 Rounds)")
print("Type 0 for Rock, 1 for Paper, 2 for Scissors")

for round in range(1, 6):
    print(f"\nRound {round}:")
    user_choice = int(input("Enter your choice (0, 1, or 2): "))

    if user_choice >= 3 or user_choice < 0:
        print("You entered an invalid choice! Computer gets 1 point.")
        computer_score += 1
    else:
        computer_choice = random.randint(0, 2)
        print("Computer's choice:", computer_choice)

        if computer_choice == user_choice:
            print("It's a draw")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose this round")
            computer_score += 1
        elif user_choice == 0 and computer_choice == 2:
            print("You win this round")
            user_score += 1
        elif computer_choice > user_choice:
            print("You lose this round")
            computer_score += 1
        elif user_choice > computer_choice:
            print("You win this round")
            user_score += 1

print("\nGame Over!")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("Congratulations! You won the game!")
elif user_score < computer_score:
    print("Computer won the game. Better luck next time!")
else:
    print("It's a tie!")
