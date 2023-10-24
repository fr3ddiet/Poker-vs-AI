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
	
	def createCard(self):
		for suit in self.__suits:
			for value in self.__values:
				self.__allcards.append(Card(value,suit))
	
	def returnDeck(self):
		return self.__allcards
		
		

deck1 = Deck()
deck1.createCard()
print(deck1.returnDeck())

for x in range(len(deck1.returnDeck())):
	print(deck1.returnDeck()[x].getCard())
		
	

