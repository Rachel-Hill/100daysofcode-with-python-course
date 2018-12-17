import random

class Roll():

    def __init__(self, name, defeats):
        self.name = name
        self.defeats = defeats
        self.valid_rolls = ["Rock", "Paper", "Scissors"]

    def get_random(self):
        return random.choices("Rock", "Paper", "Scissors")

    def choose(self):
        valid_choice = False
        while not valid_choice:
            choice = input("Choose a roll (Rock, Paper, Scissors): ")
            if choice in self.valid_rolls:
                valid_choice = True
        return choice

    def can_defeat(self,roll):
        if (roll == self.defeats):
            return True
        return False



