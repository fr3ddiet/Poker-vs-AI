from random import * 

class Card:  
    def __init__(self, value, suit): #class for each card 
        self.__suit = suit #attributes needed for each card 
        self.__value = value 

    def getCard(self): #method to be able to access the cards from the object 
        return [self.__value, self.__suit]   
	    
class Deck: #class of all cards 

    def __init__(self): #values and suits are used to loop over to create all 52 cards in a 
     # standard deck 
        self.__values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]  
        self.__suits = ["H","C","S","D"] 
        self.__count = 0 

    def createDeck(self): #empty array to start 
        self.__allcards = [] 
        for suit in self.__suits:  
            for value in self.__values: #goes over all card types and creates an instance of  
            # the card class for each card and adds it to the list 
                self.__allcards.append(Card(value,suit))  
		    
        shuffle(self.__allcards) #the cards are then shuffled to ensure the game is fair 

    # increments count so new cards can be delt when it reaches the end of the deck it sets  
    # count back to be 0 and shuffles the deck so the cards aren't the same 
    def increaseCount(self): 
        self.__count +=9 
        if self.__count >= 36: 
            shuffle(self.__allcards) 
            self.__count = 0 

    # accesses array of card objects, gets the values of each card using the getcard method  
    # and then returns it using an array 
    def getp1cards(self): 
        return [self.__allcards[self.__count].getCard()[0]  
        + self.__allcards[self.__count].getCard()[1],  
        self.__allcards[self.__count+1].getCard()[0]  
        + self.__allcards[self.__count+1].getCard()[1]] 
	    
    def getaicards(self): 
        return [self.__allcards[self.__count+2].getCard()[0] 
        + self.__allcards[self.__count+2].getCard()[1], 
        self.__allcards[self.__count+3].getCard()[0]  
        + self.__allcards[self.__count+3].getCard()[1]] 

    # same processes as getting the player cards, but it creates an array which has 5 cards in 
    # compared to 2 cards 

    def getCommunityCards(self): 
        self.__comcards = [] 
        x = 4 
        while x < 9: 
            self.__comcards.append(self.__allcards[self.__count + x].getCard() 
            [0]+self.__allcards[self.__count + x].getCard()[1]) 
            x+=1 
        return self.__comcards 

#create object of deck class and use main method to create the actual deck 
deck1 = Deck() 
deck1.createDeck() 

# testing all the methods worked as expected 
print(deck1.getp1cards()) 
print(deck1.getaicards()) 
print(deck1.getCommunityCards()) 
