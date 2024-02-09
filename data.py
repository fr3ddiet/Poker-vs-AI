class Data:
    def __init__(self):
        self.__pot = 0
        self.__bet = 0
        self.__aibet = 0 
        self.__hasRaised = 0 
        self.__player1bal = 500
        self.__player2bal = 500
        self.__playerTurn = 0

    def handleCall(self):
        self.__bet = (505 - self.__player2bal) # sets the minimum bet to 5 chips
        if self.__player1bal >= self.__bet: # makes sure the player has enough chips in the bank
            self.__pot += self.__bet 
            self.__player1bal -= self.__bet
            print("Call") # adds the bet to the pot and subtracts it from their balance
        else:
            print("no money")

        self.__playerTurn +=1 # increments the turn attribute inidicating its no longer hte players turn as they have made a choice

    def handleRaise(self):
        # create 3 button for the different raises they only appear when raise is clicked once an option is selected the buttons go away
        self.__hasRaised = 1

        if self.__player1bal >= self.__bet: # makes sure the player has enough balance to make the bet
            self.__pot+= self.__bet 
            self.__player1bal -= self.__bet
            if self.__bet > 0: # as the function is called multiple times it only increments the player turn once they click on the amount they want to raise not just the raise button
                self.__playerTurn +=1
                self.__hasRaised = 0

        #self.__bet  = 0
        print("Raise")

    def handleFold(self):
        print("Fold")
        #deck1.increaseCount() #this is used to change the cards in the deck class
        #print(deck1.getp1cards())
        #print(deck1.getaicards())  
        #print(deck1.getCommunityCards())
        self.__playerTurn = 0  # resets to player1 going first
        self.__player2bal += self.__pot  # as player2 won the value of the pot is added to their balance
        self.__pot = 0 # the pot is then reset to 0 as it had been moved

    def getRaised(self):
        return self.__hasRaised
    
    def setBet(self,value):
        self.__bet = value

    def getPlayer1bal(self):
        return self.__player1bal
    
    def getPlayer2bal(self):
        return self.__player2bal
    
    def getPot(self):
        return self.__pot
    
    def getTurn(self):
        return self.__playerTurn
