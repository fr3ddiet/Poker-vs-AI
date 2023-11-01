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
		self.__count = 0
	
	def createDeck(self):
		self.__allcards = []
		for suit in self.__suits:
			for value in self.__values:
				self.__allcards.append(Card(value,suit))
				
		shuffle(self.__allcards)
	
	def increaseCount(self):
		self.__count +=9
		if self.__count >= 36:
			shuffle(self.__allcards)
			self.__count = 0
		
	def getp1cards(self):
		return [self.__allcards[self.__count].getCard()[0] + self.__allcards[self.__count].getCard()[1] , self.__allcards[self.__count+1].getCard()[0] + self.__allcards[self.__count+1].getCard()[1]]
	
	def getaicards(self):
		return [self.__allcards[self.__count+2].getCard()[0] + self.__allcards[self.__count+2].getCard()[1], self.__allcards[self.__count+3].getCard()[0] + self.__allcards[self.__count+3].getCard()[1]]
		
	def getCommunityCards(self):
		self.__comcards = []
		x = 4
		while x < 9:
			self.__comcards.append(self.__allcards[self.__count + x].getCard()[0]+self.__allcards[self.__count + x].getCard()[1])
			x+=1
		return self.__comcards
		


deck1 = Deck()
deck1.createDeck()
#print(deck1.returnDeck())


#for x in range(len(deck1.returnDeck())):
	#print(deck1.returnDeck()[x].getCard())

#print()
#print(deck1.returnDeck()[0].getCard(),deck1.returnDeck()[1].getCard())


#print(deck1.getp1cards())
#print(deck1.getaicards())
#print(deck1.getCommunityCards())
