from cards import *

class Format: 
    def __init__(self,filename,mode): #Sets up constructor with filename and mode it will be opened with
        self.__file = open(filename,mode) 
        self.__pairhand = deck1.getaicards() # gets the ai's cards from the cards class
        #self.__allCards 

    def getCard(self):
        return self.__pairhand # returns the ai's 2 cards

    def cardRankKey(self,cards): 
        rank_order = 'AKQJT98765432'# poker order of cards
        return [rank_order.index(cards[0])] # returns the order as an index so they can be sorted in ascending order

    def orderCards(self):
        self.__pairhand.sort(key=self.cardRankKey) # sorts the 2 cards using the key

    def formatCards(self): 
        if self.__pairhand[0][1] == self.__pairhand[1][1]: # if the suits are equal
            add = "s" # they are suited
        else: 
            add = "o" # they are not suited
        return self.__pairhand[0][0] + self.__pairhand[1][0] + add # returns the two values and if they are suited or not

    def getEval(self):
        #self.__file.seek(0)
        self.__next = False #the file lines alternate between the cards and the next line is the evaluation

        for line in self.__file: # loops over each line in the file
            if line[0:3] == self.formatCards(): # if the line is equal to the ai's cards in the correct format
                self.__next = True # the next line is the evalutation for the card
            elif self.__next:
                return line # returns the evaluation

#Create object of class and define file name and type

f1 = Format('cardeval.txt',"r")
f1.orderCards()   # order the cards so they can be formated
#print(f1.getCard())
f1.formatCards() # format the cards
#print(f1.getEval()) # return the eval of the 2 cards.
