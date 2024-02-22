# import random

# def dice_game():
#     score = 0
#     round = 1
#     print("\nWelcome to Dice Game!")
#     while round <= 3:
#         print("\nRound", round)
#         print("Press '1' to roll the dice.")
#         roll = input("Enter '1' to roll the dice: ")
#         if roll == '1':
#             dice_result = random.randint(1, 6)
#             print("You rolled a", dice_result)
#             if dice_result % 2 == 0:
#                 score += dice_result
#                 print("Your current score is", score)
#             else:
#                 score -= dice_result
#                 print("Your current score is", score)
#                 if score < 0:
#                     score = 0
#                     print("Your score is now", score)
#             round += 1
#         else:
#             print("Invalid input!")
#     print("\nGame Over! Your final score is", score)
#     if score > 100:
#         print("Congratulations! You won the game.")
#     else:
#         print("Better luck next time.")

# dice_game()

import random
def dice_roll():
    roll=random.randint(1,6)
    return roll
while True:
    players=input("Enter the Number of players (2 - 4) : ")
    if players.isdigit():
        players=int(players)
        if 2<= players<=4 :
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid , Please Try again.")
max_score=50
player_scores=[0 for _ in range(players)]
while max(player_scores)< max_score:
    for player_idx in range(players):
        print("\nPlayer number",player_idx+1,"turn has just started!")
        print("Your Total Score is: ",player_scores[player_idx],"\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower()!='y':
                break
            roll = dice_roll()
            if roll == 1:
                print("You rolled a 1! Turn done!")
                break
            else:
                print("You rolled a ", roll)
                current_score+=roll
            print("Your Score is: ",current_score)
        player_scores[player_idx]+=current_score
        print("Final scores are as follows:",player_scores[player_idx])

max_score=max(player_scores)
winning_idx=player_scores.index(max_score)
print("\nThe winner is Player", winning_idx + 1," with a total of",max_score,"points! Congrats!")