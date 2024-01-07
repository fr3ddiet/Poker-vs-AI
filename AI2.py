from format import *

class AI:
    def __init__(self,j):
        self.__Cards = j
        self.__eval = f1.getEval()

        # dictionary to count repeating values and suits 

    def getEval(self):
        return self.__eval

    def findMostCommon(self,cards1):
        self.__multiple = False # If there are no repeating values, it should return the highest value
        self.__value_count = {}
        self.__suit_count = {}

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
            max_value = list(self.__value_count.keys())[-1] # last value
        else:
            max_value = max(self.__value_count, key = self.__value_count.get) # 
            #get method returns the dictionary value which is assosiated with the key.
            #max method then returns the largest dictionary value

        max_suit = max(self.__suit_count, key = self.__suit_count.get) 

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

        first = self.__cardvalues[0] # first value of array
        last = self.__cardvalues[-1] # last value of array

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
        self.__common_value = self.findMostCommon(self.__Cards)[1]
        self.__straight = self.calculateStraight()[1]

        if self.findMostCommon(self.__Cards)[3] == 5 and self.calculateStraight()[1] == 5: # straight flush
            if self.calculateStraight()[0] == [10,11,12,13,14]: #royal flush rank = 1
                return -1, 1 # outs , card rank
            else:
                return -1, 2 # straight flush rank = 2

        elif self.__common_value == 4: # 4 of a kind, rank = 3
            return -1, 3 # outs are -1 because theyre are no cards to improve this hand
        
        elif self.__common_value == 3: # this is checking for if the hand is a 'full house' or just 3 of a kind
            self.__Cards2 = [] #a full house is a 3 of a kind and a 2 of a kind
            for item in self.__Cards: # loop over each card
                if item[0] != self.findMostCommon(self.__Cards)[0]: # if the card is not the same value as the most common
                    self.__Cards2.append(item) # adds it to a new array

            #print(self.findMostCommon(self.__Cards2))

            if self.findMostCommon(self.__Cards2)[1] == 2: # if this new array has two cards with the same value
                return -1, 4 # if must be a full house and the rank = 4
            else:
                return 3 * len(self.__Cards2), 4 # else they need this many outs for a full house
                # maybe take into account if they want o get a 4 of a kind or not

        elif self.findMostCommon(self.__Cards)[3] == 5: # flush rank = 5
            return -1, 5

        elif self.__straight == 5: # straight rank = 6
            return -1, 6

        elif 2 < self.__straight < 5: # if a straight is possible
            return (5 - self.__straight) * 4 , 6 # same rank

        elif self.findMostCommon(self.__Cards)[3] > self.__common_value: # if there are more suits than values
            return 13 - self.findMostCommon(self.__Cards)[3] # 13 cards with same suit
        else:
            return 4 - self.findMostCommon(self.__Cards)[1] # 4 cards with same value

j = ["2C","2H","2S","JH","JC"]
ai1 = AI(j)
print(ai1.findOuts())
print(j)

#print(ai1.getEval())

# pair : 4 of a kind , one-overcard(unsuited) : 4 of a kind, straight possible (how many cards are in a 5 card range): straight
# 2 pair : full house, 3 same card : full house / 4 of a kind,flush draw (how many of suit): flush 
# straight and flush possible : straight flush 
