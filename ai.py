from cards import *
from gameScreen import *

class ai:
    def __init__(self):
        self.__cards = deck1.getaicards()
        self.__communityCards = deck1.getCommunityCards()
        self.__call = screen1.getBet()
        self.__pot = screen1.getPot()

    def getPotOdds(self):
        return [self.__pot / self.__call, ":", 1]

    def firstRound(self):
        pass


    


