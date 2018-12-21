import random

class Roll():

    def __init__(self, name):
        self.name = name
        action = {'rock': 'smashes','paper':'covers','scissors':'cuts'}
        self.action = action[name]

    def can_defeat(self,roll):
        win = {'rock': 'scissors','paper':'rock','scissors':'paper'}
        if (roll.name == win[self.name]):
            return True
        return False



