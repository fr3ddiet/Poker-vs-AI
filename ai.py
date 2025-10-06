from format import *

class AI:
    def __init__(self,cards):
        self.__Cards = cards
        self.__Cards2 = []
        self.__Cards3 = []
        self.__common_value = 0
        self.__straight = 0

    def findMostCommon(self,cards1):
        self.__multiple = False # If there are no repeating values, it should return the highest value
        self.__value_count = {}
        self.__suit_count = {}

        for item in cards1: # loop over the cards
            cardValue = item[0] # example card ["2C"] so value is first pos
            
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

        #if self.__multiple == False:
         #   max_value = list(self.__value_count.keys())[-1] # last value as its largest
        #else:
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

        if self.__count2 >= self.__count: #whichever end has the the highest number of cards that could form a straight
            return self.__cardvalues[-self.__count2:], self.__count2 # splice of array, last count2 elements
        else:
            return self.__cardvalues[:self.__count], self.__count # splice of array, first count elements


    def findOuts(self,cards):
        self.__Cards = cards

        self.__common_value = self.findMostCommon(self.__Cards)[1]
        self.__straight = self.calculateStraight()[1]

        #print(self.__Cards, "cards")
        #print(self.__straight)

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

            self.findMostCommon(self.__Cards2)

            if self.findMostCommon(self.__Cards2)[1] >= 2: # if this new array has two cards with the same value
                return -1, 4 # if must be a full house and the rank = 4
            elif data1.getRound() >= 4:
                return -1, 7 # 3 of a kind if no more cards can be delt
            else:
                return 3 * len(self.__Cards2), 4 # else they need this many outs for a full house
                # maybe take into account if they want o get a 4 of a kind or not

        elif self.findMostCommon(self.__Cards)[3] == 5: # flush rank = 5
            return -1, 5

        elif self.__straight == 5: # straight rank = 6
            return -1, 6

        elif 2 < self.__straight < 5 and self.__straight >= (5 - data1.getRound()) and data1.getRound() < 4: # if a straight is possible
            return (5 - self.__straight) * 4 , 6 # same rank

        elif self.__common_value == 2:
            print("2")
            self.__Cards3 = []
            for item in self.__Cards:
                if item[0] != self.findMostCommon(self.__Cards)[0]: # if the card is not the same value as the most common
                    self.__Cards3.append(item)

            self.findMostCommon(self.__Cards3)

            if self.findMostCommon(self.__Cards3)[1] == 2:
                return -1, 8 # two pair
            elif self.findMostCommon(self.__Cards3)[1] == 2 and data1.getRound() < 4:
                return 3 * len(self.__Cards3), 8 
            elif self.findMostCommon(self.__Cards3)[1] != 2:
                return -1, 9 
            else:
                return 3 * len(self.__Cards3) , 9

        elif data1.getRound() >=4:
            return -1, 10 # high card - worse ranking
        else:
            return 0,11

    def getPotOdds(self):
        self.__call = data1.getBet() # sets call value as previous players bet
        self.__pot = data1.getPot() # gets pot odds 

        if self.__call == 0: # if the player hasnt bet the call bet is 0 
            return 0
        else:
            return self.__call / (self.__pot) # odds of call compared to pot

    def getCardOdds(self):
        potential = 52 - ( len(f1.orderCards()) + 2 )  # sets number of potential cards which can be selected from
        if self.findOuts(f1.orderCards())[0] == -1:
            return 1.00
        else: 
            return (( self.findOuts(f1.orderCards())[0] ) / potential ) # finds odds using findOuts and the number of potential cards

    def calculateBet(self):
        f1.orderPair()
        f1.formatCards()

        self.__eval = f1.getEval()
        self.__potval = self.getPotOdds() # sets attribute to pot odds
        self.__cardval = self.getCardOdds()# sets attributes to card odds

        #print(self.__Cards , "cards")
        #print(self.__potval , "potval")
        #print(self.__cardval, "cardval")
        #print(self.findOuts())

        if data1.getRound() == 1 or data1.getRound() == 0  : # if round is 0 use odds from cardeval.txt
            if self.__eval < -0.1:
                return 0 # if the eval is less than -0.1 set bet to 0 
            elif self.__eval < 0.2 and self.__eval > -0.1: #  if the eval is greater than zero but less than 0.2,
                return data1.getBet() # set the bet of the ai to equal the players bet
            else: 
                return round((data1.getBet() * (1.3 + self.__eval))/10) * 10 # adjusts the raised bet to be dependant on how good the pair is

        else:
            if self.__potval > self.__cardval: # if -ve val fold or set bet to 0 
                return 0
            elif self.__potval == self.__cardval:
                return data1.getBet() # if the values are equal or if the pot value is only 5 smaller than cardval should call
 
            elif self.__cardval > self.__potval:
                #print(data1.getBet() * (1 + self.__cardval *  10), data1.getBet(), "bets")
                return round ((data1.getBet()*( 1 + self.__cardval))/10) * 10
                # adjusts raise value to be dependant on the card val
            


ai1 = AI(f1.orderCards())
pl1 = AI(playerf2.orderCards())
