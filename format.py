from cards import *
from data import *

class Format: 
    def __init__(self,filename,mode,pair): #Sets up constructor with filename and mode it will be opened with
        self.__file = open(filename,mode)  # gets the ai's cards from the cards class
        self.__pairhand = pair
        self.__allcards = self.setCommunityCards() + self.__pairhand
    
    def setCommunityCards(self):
        d = {0 : 0, 1 : 0 ,2 : 3, 3 : 4, 4: 5, 5 : 5,}
        num = d[data1.getRound()]
        return deck1.getCommunityCards()[0 : num]
            
    def getCard(self):
        return deck1.getaicards()# returns all cards

    def setpair(self):
        self.__pairhand = deck1.getaicards()

    def cardRankKey(self,cards): 
        rank_order = 'AKQJT98765432'# poker order of cards
        return [rank_order.index(cards[0])] # returns the order as an index so they can be sorted in ascending order

    def orderCards(self):
        self.__allcards = self.setCommunityCards() + self.__pairhand
        self.__allcards.sort(key=self.cardRankKey) # sorts all the cards using the key
        return self.__allcards

    def orderPair(self):
        self.__pairhand.sort(key=self.cardRankKey) # sorts the 2 cards using the key
        return self.__pairhand

    def formatCards(self): 
        self.__pairhand.sort(key=self.cardRankKey)

        if self.__pairhand[0][1] == self.__pairhand[1][1]: # if the suits are equal
            add = "s" # they are suited
        else: 
            add = "o" # they are not suited
        return self.__pairhand[0][0] + self.__pairhand[1][0] + add # returns the two values and if they are suited or not

    def getEval(self):
        self.__file.seek(0)
        form = self.formatCards()
        self.__next = False #the file lines alternate between the cards and the next line is the evaluation

        for line in self.__file: # loops over each line in the file
            #print(line)
            if line[0:3] == form: # if the line is equal to the ai's cards in the correct format
                self.__next = True # the next line is the evalutation for the card
            elif self.__next:
                return float(line[:-1]) 


#Create object of class and define file name and type
f1 = Format('cardeval.txt',"r",deck1.getaicards())

#print(deck1.getaicards())
#print(f1.getEval()) # return the eval of the 2 cards.
playerf2 = Format('cardeval.txt', 'r', deck1.getp1cards())
