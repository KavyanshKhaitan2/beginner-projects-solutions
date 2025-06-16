#### Rock Paper Scissors Game ####
# Create a rock-paper-scissors game.
#
# Tasks:
# [-] Ask the player to pick rock, paper or scissors.
# [-] Have the computer chose its move.
# [-] Compare the choices and decide who wins.
# [-] Print the results.
#
# Subgoals:
# [-] Give the player the option to play again.
# [-] Keep a record of the score (e.g. Player: 3 / Computer: 6).

import random
from typing import Literal

player_score = 0
computer_score = 0

WINNER_PLAYER = 'p'
WINNER_TIE = 't'
WINNER_COMPUTER = 'c'

def check_moves(
    player_move: Literal["r", "p", "s"], computer_move: Literal["r", "p", "s"]
):
    player_winning_positions = [
        ("r", "s"),
        ("p", "r"),
        ("s", "p")
    ]
    if player_move == computer_move:
        return WINNER_TIE
    
    if (player_move, computer_move) in player_winning_positions:
        return WINNER_PLAYER
    else:
        return WINNER_COMPUTER

while True:
    print("#########################")
    print("## Rock Paper Scissors ##")
    print("#########################")
    print()
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")
    print()
    
    
    print("Select your move")
    print(" - [R]ock")
    print(" - [P]aper")
    print(" - [S]cissors")
    
    player_move = input("(RrPpSs): ").lower()
    print()
    print()
    if player_move == "":
        continue
    computer_move = random.choice("rps")
    
    winner = check_moves(player_move, computer_move)
    if winner == WINNER_PLAYER:
        win_message = "You won."
        player_score += 1
    if winner == WINNER_COMPUTER:
        win_message = "Computer won."
        computer_score += 1
    if winner == WINNER_TIE:
        win_message = "It was a tie!"
    
    print("#########################")
    print("## Rock Paper Scissors ##")
    print("#########################")
    print()
    print()
    print()
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")
    print()
    print(win_message)
    print()
    
    inp = input("Do you want to play again? (Yn): ")
    print()
    print()
    if inp.lower() == "n":
        print("Bye!")
        break
    