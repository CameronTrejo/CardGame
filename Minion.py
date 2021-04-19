# Child class of card
from Card import Card

class Minion(Card):
    def __init__(self, name, cost, attackPoints, healthPoints):
        Card.__init__(self, name, cost)
        self.attackPoints = attackPoints
        self.healthPoints = healthPoints

    def printCard(self):
        Card.printCard(self)
        print('Attack Points:', self.attackPoints)
        print('Health Points:', self.healthPoints)