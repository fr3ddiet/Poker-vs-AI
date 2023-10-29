from pygame import *
from cards import *
init()


#window infomation
displayw = 1000 
displayh = 600
screen = display.set_mode((displayw,displayh))

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
        self.__player1bal = 1000
        self.__player2bal = 1000

    def Button(self,x,y,text):
        if x /2 <= self.mouse[0] <= x/2 + 140 and y/2 <= self.mouse[1] < y/2 + 40:
            draw.rect(screen, (100,100,100), [x /2, y/2, 140, 50])
        else:
            draw.rect(screen, (200,200,200), [x /2, y/2, 140, 50])

        screen.blit(self.__font.render(text, True, (255,255,255)), (x / 2 + 20, y / 2 + 10))


    def handleCall(self):
        self.__bet = (1010 - self.__player2bal)
        
        self.__pot += self.__bet
        self.__player1bal -= self.__bet
        print("Call")

    def handleRaise(self):
        print("Raise")
        pass

    def handleFold(self):
        print("Fold")
        pass

    def displayBalance(self):
        screen.blit(self.__font.render(str(self.__player1bal), True, (255,255,255), (0,0,255)),(460,425))
        screen.blit(self.__font.render(str(self.__player2bal), True, (255,255,255), (0,0,255)),(460,175))

    def displayCards(self):
        self.__font = font.Font('freesansbold.ttf',35) # choosing the font and size

        draw.rect(screen, (0,0,0), Rect(425,478,150,80), 2)
        draw.rect(screen, (0,0,0), Rect(425,28,150,80), 2)
        screen.blit(self.__font.render(str(deck1.getp1cards()[0]), True, (255,255,255), (0,0,255)),(445,500)) #blit first player card from the deck class
        screen.blit(self.__font.render(str(deck1.getp1cards()[1]), True, (255,255,255), (0,0,255)),(510,500)) # blit second player card from the deck class

    def main(self):
        #variables
        stopped = False
        round = 0 

        while not stopped:
            screen.fill((0,0,255))
            self.displayCards()
            self.displayBalance()

            for e in event.get():
                if e.type == QUIT:
                    quit()

                if e.type == MOUSEBUTTONDOWN:
                    if 750 <= self.mouse[0] <= 750+140 and 150 <= self.mouse[1] <= 150+40: 
                        self.handleCall()

                    if 750 <= self.mouse[0] <= 750+140 and 250 <= self.mouse[1] <= 250+40: 
                        self.handleRaise()

                    if 750 <= self.mouse[0] <= 750+140 and 350 <= self.mouse[1] <= 350+40: 
                        self.handleFold()
                    
            self.mouse = mouse.get_pos()
            self.Button(1500,300,'Call')
            self.Button(1500,500,'Raise')
            self.Button(1500,700,'Fold')



            display.update()
            clock.tick(60)

screen1 = gameScreen(displayw,displayh)
screen1.main()



