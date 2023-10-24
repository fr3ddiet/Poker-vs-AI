class Card:
	def __init__(self, value, suit):
		self.__suit = suit
		self.__value = value
		self.__values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
		self.__suits = ["H","C","S","D"]
	
	
	def createCard(self):
		self.__cards = [self.Card(value, suit) for value in self.__values for suit in self.__suits]
	
	def getCard(self):
		return self.__cards
	
	def getCards(self):
		return self.__cards
		
		
	
card1 = Card(0,0)
card1.createCard()
card1.getCards()

