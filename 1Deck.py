import random
deck = []


class Deck:
	def __init__(self,deck):
		self.__playerCards = []
		self.__communityCards = []
		self.__cardDeck = deck
		
	def shuffleCards(self):
		for x in range(26):
			x1 = random.randint(0,len(self.__cardDeck))
			x2 = random.randint(0,len(self.__cardDeck))
			temp = self.__cardDeck[x1]
			self.__cardDeck[x1] = self.__cardDeck[x2]
			self.__cardDeck[x2] = temp 
	
	def setPlayerCards(self):
		pass
		
	def setCommunityCards(self):
		pass
		
	def getPlayerCards(self):
		pass
		
	def getCommunityCards(self):
		pass
		
