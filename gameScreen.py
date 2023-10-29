from pygame import *
from cards import *
init()


#window infomation
displayw = 900 
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
        self.__playerTurn = 0
    
    def displayCards(self):
        self.__font = font.Font('freesansbold.ttf',36) # choosing the font and size

        screen.blit(self.__font.render(str(deck1.getp1cards()[0]), True, (255,255,255), (0,0,0)),(60,60)) #blit first player card from the deck class
        screen.blit(self.__font.render(str(deck1.getp1cards()[1]), True, (255,255,255), (0,0,0)),(120,60)) # blit second player card from the deck class

    def main(self):
        #variables
        stopped = False

        while not stopped:
            screen.fill((0,0,255))
            self.displayCards()

            for e in event.get():
                if e.type == QUIT:
                    quit()


            display.update()
            clock.tick(60)

screen1 = gameScreen(displayw,displayh)
screen1.main()

