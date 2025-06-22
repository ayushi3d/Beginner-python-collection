import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Type Rock / Paper / Scissors or Q to quit.\n")

while True:
    user_input = input("👉 Your move: ").lower()
    if user_input == "q":
        print("\nThanks for playing!")
        break

    if user_input not in options:
        print("❌ Invalid input. Try again.\n")
        continue

    computer_pick = random.choice(options)
    print(f"🖥️ Computer picked: {computer_pick.capitalize()}")

    if user_input == computer_pick:
        print("😐 It's a tie!\n")
    elif (
        (user_input == "rock" and computer_pick == "scissors") or
        (user_input == "paper" and computer_pick == "rock") or
        (user_input == "scissors" and computer_pick == "paper")
    ):
        print("✅ You won!\n")
        user_wins += 1
    else:
        print("❌ You lost!\n")
        computer_wins += 1

# Final results
print("🏁 Final Score:")
print(f"✨ You won {user_wins} time{'s' if user_wins != 1 else ''}.")
print(f"💻 Computer won {computer_wins} time{'s' if computer_wins != 1 else ''}.")
print("👋 Goodbye!")
