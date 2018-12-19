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
    rock = Roll('Rock')
    paper = Roll('Paper')
    scissors = Roll('Scissors')
    valid_rolls = ['Rock','Paper','Scissors']

def game_loop(player1, player2, rolls):
    round1 = Roll()
    count = 1
    while count < 3:
        p2_roll = roll.
        p1_roll = input("{}, roll: 1..2..3..".format(player1.name))

        outcome = p1_roll.can_defeat(p2_roll)
        print(outcome)

        count += 1

    # Compute who won

if __name__ == '__main__':
    main()