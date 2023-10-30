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


#class
class gameScreen:
    def __init__(self,displayw,displayh):
        self.__displayw = displayw
        self.__displayh = displayh 
        self.__playerTurn = True # the player goes first, ai second
        self.__pot = 0
        self.__player1bal = 500
        self.__player2bal = 500

    def handleMouse(self):
        if 750 <= self.mouse[0] <= 750+140 and 150 <= self.mouse[1] <= 150+40: 
            self.handleCall() # if the person clicks on the top botton it will do the call function

        if 750 <= self.mouse[0] <= 750+140 and 250 <= self.mouse[1] <= 250+40: 
            self.handleRaise() # if the person clicks the middle button it will do the raise function

        if 750 <= self.mouse[0] <= 750+140 and 350 <= self.mouse[1] <= 350+40: 
            self.handleFold() # if the person clicks the bottom button it will do the fold function

    def Button(self,x,y,text):
        if x /2 <= self.mouse[0] <= x/2 + 140 and y/2 <= self.mouse[1] < y/2 + 40:
            draw.rect(screen, (150,150,150), [x /2, y/2, 140, 50])
            draw.rect(screen, white, [x /2, y/2, 140, 50],2)
        else:
            draw.rect(screen, grey, [x /2, y/2, 140, 50])
            draw.rect(screen, white, [x /2, y/2, 140, 50],2)

        screen.blit(self.__font.render(text, True, white), (x / 2 + 20, y / 2 + 10)) # blits text to screen depending on text input


    def handleCall(self):
        self.__bet = (505 - self.__player2bal) # sets the minimum bet to 5 chips
        if self.__player1bal >= self.__bet: # makes sure the player has enough chips in the bank
            self.__pot += self.__bet 
            self.__player1bal -= self.__bet
            print("Call") # adds the bet to the pot and subtracts it from their balance
        else:
            print("no money")

    def handleRaise(self):
        print("Raise")
        pass

    def handleFold(self):
        print("Fold")
        pass

    def displayRound(self):
        screen.blit(self.__font.render("Round: "+str(self.__round), True, white, green),(150+2,100+2)) # bilts the round number in the top left of the green rectangle

    def displayBalance(self):
        screen.blit(self.__font.render(str(self.__player1bal), True, white, green),(450+22,412)) #blits the player 1 balance to tge screen
        screen.blit(self.__font.render(str(self.__player2bal), True, white, green),(450+22,160)) #blits the player 2 balance to the screen

    def displayCards(self):
        self.__font = font.Font('freesansbold.ttf',32) # choosing the font and size

        draw.rect(screen, grey, Rect(425,460,150,80)) # draws grey rectangle where player cards are
        draw.rect(screen, grey, Rect(425,60,150,80)) # draws grey rectangle where ai cards would be but face down

        draw.rect(screen, white, Rect(425,460,150,80), 2) # draws white outline around grey player rectangle
        draw.rect(screen, white, Rect(425,60,150,80), 2) # draws white outline around grey ai rectangle

        screen.blit(self.__font.render(str(deck1.getp1cards()[0]), True, white, grey),(445,485)) #blit first player card from the deck class
        screen.blit(self.__font.render(str(deck1.getp1cards()[1]), True, white, grey),(510,485)) # blit second player card from the deck class

    def main(self):
        #variables
        stopped = False
        self.__round = 1 

        while not stopped:
            screen.fill(blue)
            draw.rect(screen, green, Rect(150,100,700,400))
            draw.rect(screen, white, Rect(150,100,700,400),2)
            self.displayCards()
            self.displayBalance()

            for e in event.get():
                if e.type == QUIT:
                    quit()

                if e.type == MOUSEBUTTONDOWN:
                    self.handleMouse()
                    
            self.mouse = mouse.get_pos()
            self.Button(1500,325,'Call')
            self.Button(1500,550,'Raise')
            self.Button(1500,775,'Fold')

            self.displayRound()

            display.update()
            clock.tick(60)


#object of the class and runs the main method
screen1 = gameScreen(displayw,displayh)
screen1.main()
