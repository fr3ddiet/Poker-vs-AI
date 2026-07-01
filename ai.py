from format import *

class AI:
    def __init__(self,cards):
        self.__cards = cards
        self.__cards_without_triple = []
        self.__cards_without_pair = []
        self.__common_value = 0
        self.__straight = 0

    def find_most_common(self,cards1):
        self.__multiple = False # If there are no repeating values, it should return the highest value
        self.__value_count = {}
        self.__suit_count = {}

        for item in cards1: # loop over the cards
            card_value = item[0] # example card ["2C"] so value is first pos

            if card_value in self.__value_count: # if it exists as a key in the dictionary add one to the dictionary value
                self.__value_count[card_value] +=1
                self.__multiple = True
            else: # if it does not exist as a key
                self.__value_count[card_value] = 1 # adds a new key-value pair

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

    def calculate_straight(self): # method to find how many ascending/ descending cards there are. How many cards are 5 cards between eachother
        self.__card_values = [] #store the card values in int form. not str and int
        self.__rank_order = '23456789TJQKA' # order of card values

        self.__unique_cards = set() # set is used as in a straight the card values cannot be the same
        for item in self.__cards:
            self.__unique_cards.add(item[0])

        for item in self.__unique_cards: # loop over all cards including player cards and table
            self.__card_values.append(self.__rank_order.index(item[0]) + 2)  #checking card value.  see if a 'straight' can be made
        self.__card_values.sort()

        # two count variables as you need to check both ends of the array
        self.__count = 0  # check start of array
        self.__count_2 = 0 # check end of array

        first = self.__card_values[0] # first value of array
        last = self.__card_values[-1] # last value of array

        for item in self.__card_values:
            if abs(first - item) < 5:  # if the differnce is less than 5 the cards are apart of a potential straight
                self.__count += 1
            if abs(last - item) < 5: # if the current card is within a range of 5 values from the last card
                self.__count_2 +=1 # potential straight at the end of the array

        if self.__count_2 >= self.__count: #whichever end has the the highest number of cards that could form a straight
            return self.__card_values[-self.__count_2:], self.__count_2 # splice of array, last count2 elements
        else:
            return self.__card_values[:self.__count], self.__count # splice of array, first count elements


    def find_outs(self,cards):
        self.__cards = cards

        self.__common_value = self.find_most_common(self.__cards)[1]
        self.__straight = self.calculate_straight()[1]

        #print(self.__cards, "cards")
        #print(self.__straight)

        if self.find_most_common(self.__cards)[3] == 5 and self.calculate_straight()[1] == 5: # straight flush
            if self.calculate_straight()[0] == [10,11,12,13,14]: #royal flush rank = 1
                return -1, 1 # outs , card rank
            else:
                return -1, 2 # straight flush rank = 2

        elif self.__common_value == 4: # 4 of a kind, rank = 3
            return -1, 3 # outs are -1 because theyre are no cards to improve this hand


        elif self.__common_value == 3: # this is checking for if the hand is a 'full house' or just 3 of a kind
            self.__cards_without_triple = [] #a full house is a 3 of a kind and a 2 of a kind
            for item in self.__cards: # loop over each card
                if item[0] != self.find_most_common(self.__cards)[0]: # if the card is not the same value as the most common
                    self.__cards_without_triple.append(item) # adds it to a new array

            self.find_most_common(self.__cards_without_triple)

            if self.find_most_common(self.__cards_without_triple)[1] >= 2: # if this new array has two cards with the same value
                return -1, 4 # if must be a full house and the rank = 4
            elif data.get_round() >= 4:
                return -1, 7 # 3 of a kind if no more cards can be delt
            else:
                return 3 * len(self.__cards_without_triple), 4 # else they need this many outs for a full house
                # maybe take into account if they want o get a 4 of a kind or not

        elif self.find_most_common(self.__cards)[3] == 5: # flush rank = 5
            return -1, 5

        elif self.__straight == 5: # straight rank = 6
            return -1, 6

        elif 2 < self.__straight < 5 and self.__straight >= (5 - data.get_round()) and data.get_round() < 4: # if a straight is possible
            return (5 - self.__straight) * 4 , 6 # same rank

        elif self.__common_value == 2:
            print("2")
            self.__cards_without_pair = []
            for item in self.__cards:
                if item[0] != self.find_most_common(self.__cards)[0]: # if the card is not the same value as the most common
                    self.__cards_without_pair.append(item)

            self.find_most_common(self.__cards_without_pair)

            if self.find_most_common(self.__cards_without_pair)[1] == 2:
                return -1, 8 # two pair
            elif self.find_most_common(self.__cards_without_pair)[1] == 2 and data.get_round() < 4:
                return 3 * len(self.__cards_without_pair), 8
            elif self.find_most_common(self.__cards_without_pair)[1] != 2:
                return -1, 9
            else:
                return 3 * len(self.__cards_without_pair) , 9

        elif data.get_round() >=4:
            return -1, 10 # high card - worse ranking
        else:
            return 0,11

    def get_pot_odds(self):
        self.__call = data.get_bet() # sets call value as previous players bet
        self.__pot = data.get_pot() # gets pot odds

        if self.__call == 0: # if the player hasnt bet the call bet is 0
            return 0
        else:
            return self.__call / (self.__pot) # odds of call compared to pot

    def get_card_odds(self):
        potential = 52 - ( len(ai_formatter.order_cards()) + 2 )  # sets number of potential cards which can be selected from
        if self.find_outs(ai_formatter.order_cards())[0] == -1:
            return 1.00
        else:
            return (( self.find_outs(ai_formatter.order_cards())[0] ) / potential ) # finds odds using findOuts and the number of potential cards

    def calculate_bet(self):
        ai_formatter.order_pair()
        ai_formatter.format_cards()

        self.__hand_eval = ai_formatter.get_eval()
        self.__pot_odds = self.get_pot_odds() # sets attribute to pot odds
        self.__card_odds = self.get_card_odds()# sets attributes to card odds

        #print(self.__cards , "cards")
        #print(self.__pot_odds , "potval")
        #print(self.__card_odds, "cardval")
        #print(self.find_outs())

        if data.get_round() == 1 or data.get_round() == 0  : # if round is 0 use odds from cardeval.txt
            if self.__hand_eval < -0.1:
                return 0 # if the eval is less than -0.1 set bet to 0
            elif self.__hand_eval < 0.2 and self.__hand_eval > -0.1: #  if the eval is greater than zero but less than 0.2,
                return data.get_bet() # set the bet of the ai to equal the players bet
            else:
                return round((data.get_bet() * (1.3 + self.__hand_eval))/10) * 10 # adjusts the raised bet to be dependant on how good the pair is

        else:
            if self.__pot_odds > self.__card_odds: # if -ve val fold or set bet to 0
                return 0
            elif self.__pot_odds == self.__card_odds:
                return data.get_bet() # if the values are equal or if the pot value is only 5 smaller than cardval should call

            elif self.__card_odds > self.__pot_odds:
                #print(data.get_bet() * (1 + self.__card_odds *  10), data.get_bet(), "bets")
                return round ((data.get_bet()*( 1 + self.__card_odds))/10) * 10
                # adjusts raise value to be dependant on the card val



ai_player = AI(ai_formatter.order_cards())
human_player = AI(player_formatter.order_cards())
