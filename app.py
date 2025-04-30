import random;

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or\
            (player_choice == "scissors" and computer_choice == "paper") or\
            (player_choice == "paper" and computer_choice == "rock"):
            return "Win"
    else: 
        return "lose"

def play_round():
     choices = ["rock", "paper", "scissors"]

     #getting player input 
     player_choice = input("Enter rock,paper,scissors: ").lower()

     if player_choice not in choices:
          print("invalid Choice")
          return None
     
     computer_choice = random.choice(choices)
     print(f"Computer choices: {computer_choice}")

     result = determine_winner(player_choice, computer_choice)

    if result == "tie":
          print("It is tie")
    elif result == "win":
        print("win")
    else:
        print("you lose")
    return result


def main:
    player_score = 0
    rounds_played = 0

    while True:
        result = play_round()

        if result == "win":
            player_score += 1
        rounds_played += 1

        play_again = input ("do you want to play again?").lower()
        if play_again != yes:
            break

        print(f"Game over {rounds_played} rounds and won {player_score} times")

if __name__ == "__main__":
    main()