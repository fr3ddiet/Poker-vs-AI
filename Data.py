class Data:
    def __init__(self):
        self.__pot = 0
        self.__bet = 5
        self.__ai_bet = 5
        self.__total_p1_bet = 0
        self.__total_ai_bet = 0
        self.__has_raised = 0
        self.__player_1_balance = 500
        self.__player_2_balance = 500
        self.__player_turn = 0
        self.__round = 0

    def handle_call(self):
        if self.__total_ai_bet == 0:
            self.__bet = 5
        else:
            if self.__total_ai_bet > self.__total_p1_bet:
                self.__bet = self.__total_ai_bet - self.__total_p1_bet # sets the minimum bet to 5 chips
            else:
                self.__bet = self.__total_p1_bet - self.__total_ai_bet

        if self.__player_1_balance >= self.__bet: # makes sure the player has enough chips in the bank
            self.__total_p1_bet += self.__bet
            self.__pot += self.__bet
            self.__player_1_balance -= self.__bet
            #print("Call") # adds the bet to the pot and subtracts it from their balance
        else:
            print("no money")

        self.__player_turn +=1 # increments the turn attribute inidicating its no longer hte players turn as they have made a choice

    def handle_ai_call(self,bet):
        if self.__player_2_balance >= bet:
            self.__total_ai_bet += bet
            self.__pot += bet
            self.__player_2_balance -= bet
        else:
            print("no money")

        self.__player_turn +=1


    def handle_raise(self):
        # create 3 button for the different raises they only appear when raise is clicked once an option is selected the buttons go away
        self.__has_raised = 1

        if self.__player_1_balance >= self.__bet: # makes sure the player has enough balance to make the bet
            self.__pot+= self.__bet
            self.__player_1_balance -= self.__bet
            self.__total_p1_bet += self.__bet
            if self.__bet > 0: # as the function is called multiple times it only increments the player turn once they click on the amount they want to raise not just the raise button
                self.__player_turn +=1
                self.__has_raised = 0

        #self.__bet  = 0
        print("Raise")

    def handle_fold(self, folded_player):
        #print("Fold")
        #deck.increase_count() #this is used to change the cards in the deck class
        self.__player_turn = 0 # resets to player1 going first
        if folded_player == "player":
            self.__player_2_balance += self.__pot  # as player2 won the value of the pot is added to their balance
        else:
            self.__player_1_balance += self.__pot
        self.__pot = 0 # the pot is then reset to 0 as it had been moved
        self.__total_p1_bet = 0
        self.__total_ai_bet = 0

    def total_bet(self):
        if self.__total_p1_bet == self.__total_ai_bet:
            return True
        else:
            return False

    def get_raised(self):
        return self.__has_raised

    def set_ai_bet(self,value):
        self.__ai_bet = value

    def get_ai_bet(self):
        return self.__ai_bet

    def set_bet(self,value):
        self.__bet = value

    def get_bet(self):
        return self.__bet

    def get_player_1_balance(self):
        return self.__player_1_balance

    def get_player_2_balance(self):
        return self.__player_2_balance

    def get_pot(self):
        return self.__pot

    def get_turn(self):
        return self.__player_turn

    def increment_turn(self):
        self.__player_turn+=1

    def get_round(self):
        return self.__round

    def increment_round(self,value):
        self.__round = value

    def check_end(self):
        return self.__round > 4 and self.__bet == self.__ai_bet

data = Data()
