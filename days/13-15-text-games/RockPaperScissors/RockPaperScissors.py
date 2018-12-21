from player import Player
from roll import Roll
import random

def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)

def get_players_name():

    player_name = input("What is your name?  ")

    return player_name

def print_header():
    print('---------------------------------')
    print('        ROCK PAPER SCISSORS')
    print('---------------------------------')
    print()

def build_the_three_rolls():
    rock = Roll('rock')
    paper = Roll('paper')
    scissors = Roll('scissors')
    rolls = [rock, paper, scissors]
    return rolls

def get_player_roll():
    valid_choice = False
    while not valid_choice:
        choice = input("Choose Rock, Paper, or Scissors:  ").lower()
        if choice == 'rock':
            return Roll('rock')
        elif choice == 'paper':
            return Roll('paper')
        elif choice == 'scissors':
            return Roll('scissors')



def game_loop(player1, player2, rolls):
    count = 1
    while player1.score < 3 and player2.score < 3:
        p2_roll = random.choice(rolls)
        p1_roll = get_player_roll()
        win = p1_roll.can_defeat(p2_roll)
        if win:
            player1.score += 1
            print("{} {} {}. {} wins!".format(p1_roll.name, p1_roll.action, p2_roll.name, player1.name))
        elif p2_roll.name == p1_roll.name:
            print("it's a tie. Try again")
        else:
            player2.score += 1
            print("{} {} {}. Computer wins.".format(p2_roll.name, p2_roll.action, p1_roll.name))

        print("{}: {}  {}: {}".format(player1.name, player1.score, player2.name, player2.score))

    if player1.score == 3:
        print("Congrats, {}.  You are the champion!".format(player1.name))
    else:
        print(" ")
        print("Sorry. Computer wins the match.")

    # Compute who won

if __name__ == '__main__':
    main()