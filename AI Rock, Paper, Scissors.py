import random

print("Let's play rock paper scissors. First to three wins!")
player_name = input("Username: ")
print()

player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    print()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}")

    if player_choice == computer_choice:
      winner = "draw"
    elif player_choice == "rock" and computer_choice == "scissors":
      winner = "player"
    elif player_choice == "paper" and computer_choice == "rock":
      winner = "player"
    elif player_choice == "scissors" and computer_choice == "paper":
      winner = "player"
    else:
      winner = "computer"
    
    if winner == "player":
      player_wins += 1
      print("You won!")
      print()
    elif winner == "computer":
      computer_wins += 1
      print("You lost!")
      print()
    else:
      print("It's a draw")
      print()

    print("CURRENT SCORE:")
    print(f"Player: {player_wins}")
    print(f"Computer: {computer_wins}")
    print()
  
if player_wins > computer_wins:
  print(f"Congratulations, you won {player_name}!")
else:
  print("Sorry, you lost! Computer won!")