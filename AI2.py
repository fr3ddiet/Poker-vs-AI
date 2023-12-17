from cards import *

class AI:
    def __init__(self,j):
        self.__Cards = j
        #self.__minbet = screen1.getBet()
        #self.__eval : Format

        self.__value_count = {} # dictionary to count repeating values and suits 
        self.__suit_count = {}

    def findMostCommon(self,cards1):
        self.__multiple = False # If there are no repeating values, it should return the highest value

        for item in cards1: # loop over the cards
            cardValue = item[0] # ["2C"] so value is first pos
            if cardValue in self.__value_count: # if it exists as a key in the dictionary add one to the dictionary value
                self.__value_count[cardValue] +=1
                self.__multiple = True
            else: # if it does not exist as a key 
                self.__value_count[cardValue] = 1 # adds a new key-value pair

            suit = item[1]  # same as value but checks suit
            if suit in self.__suit_count:
                self.__suit_count[suit] +=1
            else:
                self.__suit_count[suit] = 1

        if self.__multiple == False:
            max_value = list(self.__value_count.keys())[-1]
        else:
            max_value = max(self.__value_count, key = self.__value_count.get) # 
            #get method returns the dictionary value which is assosiated with the key.
            #max method then returns the largest dictionary value

        max_suit = max(self.__suit_count, key = self.__suit_count.get) # 

        return max_value, int(self.__value_count[max_value]), max_suit, int(self.__suit_count[max_suit])

    def calculateStraight(self): # method to find how many ascending/ descending cards there are. How many cards are 5 cards between eachother
        self.__cardvalues = [] #store the card values in int form. not str and int 
        self.__rankOrder = '23456789TJQKA' # order of card values

        self.__uniquecard = set() # set is used as in a straight the card values cannot be the same
        for item in self.__Cards:
            self.__uniquecard.add(item[0])
        
        for item in self.__uniquecard: # loop over all cards including player cards and table
            self.__cardvalues.append(self.__rankOrder.index(item[0]) + 2)  #checking card value.  see if a 'straight' can be made
        self.__cardvalues.sort()

        # two count variables as you need to check both ends of the array
        self.__count = 0  # check start of array
        self.__count2 = 0 # check end of array

        first = self.__cardvalues[0]
        last = self.__cardvalues[-1]

        for item in self.__cardvalues:
            if abs(first - item) < 5:  # if the differnce is less than 5 the cards are apart of a potential straight
                self.__count += 1
            if abs(last - item) < 5: # if the current card is within a range of 5 values from the last card
                self.__count2 +=1 # potential straight at the end of the array

        if self.__count2 > self.__count: #whichever end has the the highest number of cards that could form a straight
            return self.__cardvalues[-self.__count2:], self.__count2 # splice of array, last count2 elements
        else:
            return self.__cardvalues[:self.__count], self.__count # splice of array, first count elements

    def findOuts(self):
        '''
        if self.findMostCommon(self.__Cards)[3] == 5 and self.calculateStraight()[1] == 5: # straight flush
            if self.calculateStraight()[0] == [10,11,12,13,14]: #royal flush rank = 1
                return -1, 1
            else: # straight flush rank = 2
                return -1, 2 
        '''

        if self.findMostCommon(self.__Cards)[1] == 4: # 4 of a kind rank = 3
            return -1, 3
        
        elif self.findMostCommon(self.__Cards)[1] == 3:
            self.__Cards2 = []
            for item in self.__Cards:
                if item[0] != self.findMostCommon()[0]:
                    self.__Cards2.append(item)

            if self.findMostCommon(self.__Cards2)[1] == 2: #full house rank = 4
                return -1 
            else:
                return 3 * len(self.__Cards2)

        elif self.findMostCommon(self.__Cards)[3] == 5: # flush rank = 5
            return -1

        elif self.calculateStraight()[1] == 5: # straight rank = 6
            return -1

        elif 2 < self.calculateStraight()[1] < 5:
            return ( 5 - self.calculateStraight()[1] ) * 4 

        elif self.findMostCommon(self.__Cards)[3] > self.findMostCommon(self.__Cards)[1]:
            return 13 - self.findMostCommon(self.__Cards)[3]
        else:
            return 4 - self.findMostCommon(self.__Cards)[1] 

j = ["2C","3H","4S","JH","JC"]
ai1 = AI(j)
print(ai1.findOuts())

# pair : 4 of a kind , one-overcard(unsuited) : 4 of a kind, straight possible (how many cards are in a 5 card range): straight
# 2 pair : full house, 3 same card : full house / 4 of a kind,flush draw (how many of suit): flush 
# straight and flush possible : straight flush 
