# imports and initalise pygame
from pygame import *
from cards import *
init()

#window infomation and sets up the screen
displayw = 1000 
displayh = 600
screen = display.set_mode((displayw,displayh))

# sets all the colours used in the progra
blue = (51, 102, 255)
green = (10, 153, 10)
white = (255, 255, 255)
grey = (200, 200, 200)

#clock
clock = time.Clock()

#load images


# gameScreen class
class gameScreen:
    def __init__(self,displayw,displayh):
        # setting up display 
        self.__displayw = displayw
        self.__displayh = displayh 

        self.__playerTurn = 0 # used to indicate whose turn it is 
        
        #handle all the attributes for the chips 
        self.__pot = 0
        self.__player1bal = 500
        self.__player2bal = 500

    def handleMouse(self):
        if self.__playerTurn % 2 == 0: # only allow the buttons to work if its the players turn
            if 750 <= self.__mouse[0] <= 750+140 and 325 // 2  <= self.__mouse[1] <= 325 // 2 + 40: 
                self.handleCall() # if the person clicks on the top botton it will do the call function

            if 750 <= self.__mouse[0] <= 750+140 and 550 // 2 <= self.__mouse[1] <= 550 // 2 +40: 
                self.handleRaise() # if the person clicks the middle button it will do the raise function

            if 750 <= self.__mouse[0] <= 750+140 and 775 // 2 <= self.__mouse[1] <= 775 // 2+40: 
                self.handleFold() # if the person clicks the bottom button it will do the fold function

    def Button(self,x,y,text):
        if self.__playerTurn % 2 == 0: # if its the players turn
            if x <= self.__mouse[0] <= x + 140 and y <= self.__mouse[1] < y + 40: # if the mouse is hovering over the button make the background colour of the button darker
                draw.rect(screen, (150,150,150), [x , y, 140, 50])
                draw.rect(screen, white, [x , y, 140, 50],2)
            else: # make the background colour of the button lighter when it isnt hovered over
                draw.rect(screen, grey, [x , y, 140, 50])
                draw.rect(screen, white, [x , y, 140, 50],2)

            screen.blit(self.__font.render(text, True, white), (x + 20, y + 10)) # blits text to screen depending on function text input
        else: # if its not the players turn grey out the buttons indiciating they cannot be used as you cannot make a decision for the ai
            draw.rect(screen, grey, [x , y, 140, 50])
            draw.rect(screen, white, [x , y, 140, 50],2)


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
        print("Raise")

    def handleFold(self):
        print("Fold")

    def aiturn(self):
        if self.__playerTurn % 2 == 1:
            self.__playerTurn+=1

    def displayRound(self):
        screen.blit(self.__font.render("Round: "+str(self.__round), True, white, green),(150+2,100+2)) # bilts the round number in the top left of the green rectangle
        
    def displayBalance(self):
        screen.blit(self.__font.render(str(self.__player1bal), True, white, green),(450+22,412)) #blits the player 1 balance to tge screen
        screen.blit(self.__font.render(str(self.__player2bal), True, white, green),(450+22,160)) #blits the player 2 balance to the screen

    def displayPlayerCards(self):
        self.__font = font.Font('freesansbold.ttf',32) # choosing the font and size of the text

        draw.rect(screen, grey, Rect(425,460,150,80)) # draws grey rectangle where player cards are
        draw.rect(screen, grey, Rect(425,60,150,80)) # draws grey rectangle where ai cards would be but face down

        draw.rect(screen, white, Rect(425,460,150,80), 2) # draws white outline around grey player rectangle
        draw.rect(screen, white, Rect(425,60,150,80), 2) # draws white outline around grey ai rectangle
         
        screen.blit(self.__font.render(str(deck1.getp1cards()[0]), True, white, grey),(445,485)) #blit first player card from the deck class
        screen.blit(self.__font.render(str(deck1.getp1cards()[1]), True, white, grey),(510,485)) # blit second player card from the deck class
        
    def displayTableCards(self):
        # uses the community cards from the cards.py file. displays them based on the round of the game
        if self.__round >= 2:
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[0]), True, white, green),(330 + 28,275))
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[1]), True, white, green),(390 + 28,275))
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[2]), True, white, green),(450 + 28,275))
        
        if self.__round >= 3:
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[3]), True, white, green),(510 + 28,275))

        if self.__round >=4:
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[4]), True, white, green),(570 + 28,275))

    def main(self):
        #variable to control game loop
        stopped = False

        while not stopped:
            #sets round number based off how many player turns have occured
            self.__round = 1 + self.__playerTurn // 2

            #sets up background
            screen.fill(blue) #background colour
            draw.rect(screen, green, Rect(150,100,700,400)) # draws green table
            draw.rect(screen, white, Rect(150,100,700,400),2) # white table outline
            
            # displays all cards and balances
            self.displayPlayerCards()
            self.displayBalance()
            self.displayTableCards()
            self.displayRound()

            #gets mouse pos for the event handler
            self.__mouse = mouse.get_pos()

            #loop for pygame events
            for e in event.get():
                if e.type == QUIT: # to quit the game
                    quit()

                if e.type == MOUSEBUTTONDOWN: # if they left click the mouse
                    self.handleMouse()

                if e.type == KEYDOWN:  # simulate/skip ai turn as ai hasnt been developed yet
                    if e.key == K_1: # uses button 1
                        self.aiturn()
                    
            # uses the button function to make the 3 call, raise and fold buttons
            self.Button(750,163,'Call') 
            self.Button(750,275,'Raise')
            self.Button(750,388,'Fold')

            # sets the clock and updates the display
            clock.tick(60)
            display.update()


#creates object of the class and then runs the main method
screen1 = gameScreen(displayw,displayh)
screen1.main()
