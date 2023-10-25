from random import *

class Card:
	def __init__(self, value, suit):
		self.__suit = suit 
		self.__value = value
	
	def getCard(self):
		return [self.__value, self.__suit]	
	
class Deck:
	def __init__(self):
		self.__values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
		self.__suits = ["H","C","S","D"]
		self.__allcards = []
	
	def createDeck(self):
		for suit in self.__suits:
			for value in self.__values:
				self.__allcards.append(Card(value,suit))
				
		shuffle(self.__allcards)
	
	def returnDeck(self):
		return self.__allcards
		
	def getp1cards(self):
		return [self.__allcards[0].getCard() , self.__allcards[1].getCard()]
	
	def getaicards(self):
		return [self.__allcards[2].getCard(), self.__allcards[3].getCard()]
		
	def setCommunityCards(self):
		self.__comcards = [self.__allcards[4].getCard(), self.__allcards[5].getCard(), self.__allcards[5].getCard(), self.__allcards[5].getCard(), self.__allcards[5].getCard()]
		


deck1 = Deck()
deck1.createDeck()
print(deck1.returnDeck())


for x in range(len(deck1.returnDeck())):
	print(deck1.returnDeck()[x].getCard())

print()
#print(deck1.returnDeck()[0].getCard(),deck1.returnDeck()[1].getCard())

print(deck1.getp1cards()[0])
print(deck1.getp1cards())

