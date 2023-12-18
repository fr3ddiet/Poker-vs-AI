from cards import *

class Format: 
    def __init__(self,filename,mode): 
        self.__file = open(filename,mode) 
        #self.__pairhand = deck1.getAICards() 
        self.__Cards = "44o"
        self.__eval = 0  

    def cardRankKey(self): 
        rank_order = 'AKQJT98765432'
        return rank_order.index(self.__Cards[0])

    def orderCards(self): 
        self.__Cards.sort(key=self.cardRankKey)

    def formatCards(self): 
        if self.__pairhand[0][1] == self.__pairhand[1][1]: 
            add = "s" 
        else: 
            add = "o" 
        return self.__pairhand[0][0] + self.__pairhand[1][0] + add 

    def getEval(self):
        print("a")
        self.__file.seek(0)
        self.__next = False

        for line in self.__file:
            if line[0:3] == self.__Cards:
                self.__next = True
            elif self.__next:
                return line

f1 = Format('cardeval.txt',"r")
print(f1.getEval())
