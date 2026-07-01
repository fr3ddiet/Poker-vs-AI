class Data:
    def __init__(self):
        self.__pot = 0
        self.__bet = 5
        self.__aibet = 5
        self.__totalp1bet = 0
        self.__totalaibet = 0
        self.__hasRaised = 0 
        self.__player1bal = 500
        self.__player2bal = 500
        self.__playerTurn = 0
        self.__round = 0

    def handleCall(self):
        if self.__totalaibet == 0:
            self.__bet = 5
        else:
            if self.__totalaibet > self.__totalp1bet:
                self.__bet = self.__totalaibet - self.__totalp1bet # sets the minimum bet to 5 chips
            else:
                self.__bet = self.__totalp1bet - self.__totalaibet

            
        if self.__player1bal >= self.__bet: # makes sure the player has enough chips in the bank
            self.__totalp1bet += self.__bet
            self.__pot += self.__bet 
            self.__player1bal -= self.__bet
            #print("Call") # adds the bet to the pot and subtracts it from their balance
        else:
            print("no money")

        self.__playerTurn +=1 # increments the turn attribute inidicating its no longer hte players turn as they have made a choice

    def handleAICall(self,bet):
        if self.__player2bal >= bet:
            self.__totalaibet += bet
            self.__pot += bet
            self.__player2bal -= bet
        else:
            print("no money")

        self.__playerTurn +=1


    def handleRaise(self):
        # create 3 button for the different raises they only appear when raise is clicked once an option is selected the buttons go away
        self.__hasRaised = 1

        if self.__player1bal >= self.__bet: # makes sure the player has enough balance to make the bet
            self.__pot+= self.__bet 
            self.__player1bal -= self.__bet
            self.__totalp1bet += self.__bet
            if self.__bet > 0: # as the function is called multiple times it only increments the player turn once they click on the amount they want to raise not just the raise button
                self.__playerTurn +=1
                self.__hasRaised = 0

        #self.__bet  = 0
        print("Raise")

    def handleFold(self,id):
        #print("Fold")
        #deck1.increaseCount() #this is used to change the cards in the deck class
        self.__playerTurn = 0 # resets to player1 going first
        if id == "player":
            self.__player2bal += self.__pot  # as player2 won the value of the pot is added to their balance
        else:
            self.__player1bal += self.__pot
        self.__pot = 0 # the pot is then reset to 0 as it had been moved
        self.__totalp1bet = 0
        self.__totalaibet = 0

    def totalBet(self):
        if self.__totalp1bet == self.__totalaibet:
            return True
        else:
            return False
     
    def getRaised(self):
        return self.__hasRaised

    def setaibet(self,value):
        self.__aibet = value

    def getaibet(self):
        return self.__aibet
     
    def setBet(self,value):
        self.__bet = value

    def getBet(self):
        return self.__bet

    def getPlayer1bal(self):
        return self.__player1bal
     
    def getPlayer2bal(self):
        return self.__player2bal
     
    def getPot(self):
        return self.__pot
     
    def getTurn(self):
        return self.__playerTurn

    def incrementTurn(self):
        self.__playerTurn+=1

    def getRound(self):
        return self.__round

    def incrementRound(self,value):
        self.__round = value

    def checkEnd(self):
        return self.__round > 4 and self.__bet == self.__aibet

data1 = Data()