from cards import *
from data import *

class Format:
    def __init__(self,filename,mode,pair): #Sets up constructor with filename and mode it will be opened with
        self.__file = open(filename,mode)  # gets the ai's cards from the cards class
        self.__pair_hand = pair
        self.__all_cards = self.set_community_cards() + self.__pair_hand

    def set_community_cards(self):
        d = {0 : 0, 1 : 0 ,2 : 3, 3 : 4, 4: 5, 5 : 5,}
        num = d[data.get_round()]
        return deck.get_community_cards()[0 : num]

    def get_card(self):
        return deck.get_ai_cards()# returns all cards

    def set_pair(self):
        self.__pair_hand = deck.get_ai_cards()

    def card_rank_key(self,cards):
        rank_order = 'AKQJT98765432'# poker order of cards
        return [rank_order.index(cards[0])] # returns the order as an index so they can be sorted in ascending order

    def order_cards(self):
        self.__all_cards = self.set_community_cards() + self.__pair_hand
        self.__all_cards.sort(key=self.card_rank_key) # sorts all the cards using the key
        return self.__all_cards

    def order_pair(self):
        self.__pair_hand.sort(key=self.card_rank_key) # sorts the 2 cards using the key
        return self.__pair_hand

    def format_cards(self):
        self.__pair_hand.sort(key=self.card_rank_key)

        if self.__pair_hand[0][1] == self.__pair_hand[1][1]: # if the suits are equal
            add = "s" # they are suited
        else:
            add = "o" # they are not suited
        return self.__pair_hand[0][0] + self.__pair_hand[1][0] + add # returns the two values and if they are suited or not

    def get_eval(self):
        self.__file.seek(0)
        form = self.format_cards()
        self.__next_line_is_eval = False #the file lines alternate between the cards and the next line is the evaluation

        for line in self.__file: # loops over each line in the file
            #print(line)
            if line[0:3] == form: # if the line is equal to the ai's cards in the correct format
                self.__next_line_is_eval = True # the next line is the evalutation for the card
            elif self.__next_line_is_eval:
                return float(line[:-1])


#Create object of class and define file name and type
ai_formatter = Format('cardeval.txt',"r",deck.get_ai_cards())

#print(deck.get_ai_cards())
#print(ai_formatter.get_eval()) # return the eval of the 2 cards.
player_formatter = Format('cardeval.txt', 'r', deck.get_p1_cards())
