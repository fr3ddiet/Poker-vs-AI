# imports and initalise pygame
from a import *
from pygame import *
init()

#window infomation and sets up the screen
displayw = 1000 
displayh = 600
screen = display.set_mode((displayw,displayh))

# sets all the colours used in the program
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
        
    def handleMouse(self):
        if data1.getTurn() % 2 == 0 and data1.checkEnd() != True: # only allow the buttons to work if its the players turn
            if 750 <= self.__mouse[0] <= 750+140 and 325 // 2  <= self.__mouse[1] <= 325 // 2 + 40: 
                data1.handleCall() # if the person clicks on the top botton it will do the call function

            if 750 <= self.__mouse[0] <= 750+140 and 550 // 2 <= self.__mouse[1] <= 550 // 2 +40: 
                data1.setBet(0)
                data1.handleRaise()# if the person clicks the middle button it will do the raise function

            if 750 <= self.__mouse[0] <= 750+140 and 775 // 2 <= self.__mouse[1] <= 775 // 2+40: 
                data1.handleFold("player") # if the person clicks the bottom button it will do the fold function
                deck1.increaseCount()

            if 655 <= self.__mouse[0] <= 655 + 75 and 525 <= self.__mouse[1] <= 525 + 50: 
                data1.setBet(25)
                data1.handleRaise()

            if 770 <= self.__mouse[0] <= 770 + 75 and 525 <= self.__mouse[1] <= 525 + 50: 
                data1.setBet(50)
                data1.handleRaise()

            if 885 <= self.__mouse[0] <= 885 + 75 and 525 <= self.__mouse[1] <= 525 + 50: 
                data1.setBet(100)
                data1.handleRaise()

    def Button(self,x,y,text,x2,y2):
        if data1.getTurn() % 2 == 0 and data1.checkEnd() != True: # if its the players turn
            if x <= self.__mouse[0] <= x + x2 and y <= self.__mouse[1] < y + y2: # if the mouse is hovering over the button make the background colour of the button darker
                draw.rect(screen, (150,150,150), [x , y, x2, y2])
                draw.rect(screen, white, [x , y, x2, y2],2)
            else: # make the background colour of the button lighter when it isnt hovered over
                draw.rect(screen, grey, [x , y, x2, y2])
                draw.rect(screen, white, [x , y, x2, y2],2)

            screen.blit(self.__font.render(text, True, white), (x + 20, y + 10)) # blits text to screen depending on function text input
        else: # if its not the players turn grey out the buttons indiciating they cannot be used as you cannot make a decision for the ai
            draw.rect(screen, grey, [x , y, x2, y2])
            draw.rect(screen, white, [x , y, x2, y2],2)

    def raiseButton(self):
        if data1.getRaised() == 1:
            self.Button(655,525,"25",75,50)
            self.Button(770,525,"50",75,50)
            self.Button(885,525,"100",100,50)

    def aiturn(self):
        if data1.getTurn() % 2 == 1:
            data1.setaibet(ai1.calculateBet())
 
            if data1.getaibet() == 0 and not data1.totalBet():
                data1.handleFold("ai")
                deck1.increaseCount()
                print("ai folded",)
            else:
                data1.handleAICall(data1.getaibet())
            

    
    def checkWin(self):
        if data1.getRound() == 5:
            #print("A")
            time.wait(1000) # waits a second before the game ends
            ai = ai1.findOuts(f1.orderCards()) # ai card hand value is findOuts[1]
            p1 = pl1.findOuts(playerf2.orderCards()) # user card hand value is findOuts[1]
            print(f1.orderCards(),playerf2.orderCards()) # prints ai cards then players
            print(ai,p1) # prints ai value then user value

            if ai[0] == -1 and p1[0] == -1:
                if ai[1] < p1[1]:
                    data1.handleFold("player")
                    print('ai win')
                else:
                    data1.handleFold("ai")
                    print('user win') 

            elif ai[0] == -1:
                data1.handleFold("player")
                print('ai win')

            elif p1[0] == -1:
                data1.handleFold("ai")
                print('user win')

            deck1.increaseCount()


    def displayRound(self):
        screen.blit(self.__font.render("Round: "+str(data1.getRound()), True, white, green),(150+5,100+5)) # bilts the round number in the top left of the green rectangle
        
    def displayBalance(self):
        screen.blit(self.__font.render(str(data1.getPlayer1bal()), True, white, green),(450+22,412)) #blits the player 1 balance to tge screen
        screen.blit(self.__font.render(str(data1.getPlayer2bal()), True, white, green),(450+22,160)) #blits the player 2 balance to the screen
        screen.blit(self.__font.render(str(data1.getPot()), True, white, green),(205,275))

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
        if data1.getRound() >= 2:
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[0]), True, white, green),(330 + 28,275))
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[1]), True, white, green),(390 + 28,275))
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[2]), True, white, green),(450 + 28,275))
        
        if data1.getRound() >= 3:
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[3]), True, white, green),(510 + 28,275))

        if data1.getRound() >=4:
            screen.blit(self.__font.render(str(deck1.getCommunityCards()[4]), True, white, green),(570 + 28,275))

    def main(self):
        #variable to control game loop
        stopped = False

        while not stopped:
            #sets round number based off how many player turns have occured
            data1.incrementRound(1 + data1.getTurn() // 2)

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

                if e.type == KEYDOWN:  # 
                    if e.key == K_1: # uses button 1
                        print("a")

                    
            # uses the button function to make the 3 call, raise and fold buttons
            self.Button(750,163,'Call',150,50) 
            self.Button(750,275,'Raise',150,50)
            self.Button(750,388,'Fold',150,50)

            self.raiseButton()
            self.aiturn()


            self.checkWin()

            # sets the clock and updates the display
            clock.tick(60)
            display.update()


#creates object of the class and then runs the main method
screen1 = gameScreen(displayw,displayh)
screen1.main()
