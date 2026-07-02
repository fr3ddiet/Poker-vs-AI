# imports and initalise pygame
from ai import *
from pygame import *
init()

#window infomation and sets up the screen
display_width = 1000
display_height = 600
screen = display.set_mode((display_width,display_height))

# sets all the colours used in the program
blue = (51, 102, 255)
green = (10, 153, 10)
white = (255, 255, 255)
grey = (200, 200, 200)

#clock
clock = time.Clock()

#load images


# GameScreen class
class GameScreen:
    def __init__(self,display_width,display_height):
        # setting up display
        self.__display_width = display_width
        self.__display_height = display_height

        self.__ai_formatter = Format('cardeval.txt',"r",deck.get_ai_cards())
        self.__player_formatter = Format('cardeval.txt','r',deck.get_p1_cards())
        self.__ai_player = AI(self.__ai_formatter.order_cards(),self.__ai_formatter)
        self.__human_player = AI(self.__player_formatter.order_cards(),self.__player_formatter)

    def handle_mouse(self):
        if data.get_turn() % 2 == 0 and data.check_end() != True: # only allow the buttons to work if its the players turn
            if 750 <= self.__mouse[0] <= 750+140 and 325 // 2  <= self.__mouse[1] <= 325 // 2 + 40:
                data.handle_call() # if the person clicks on the top botton it will do the call function

            if 750 <= self.__mouse[0] <= 750+140 and 550 // 2 <= self.__mouse[1] <= 550 // 2 +40:
                data.set_bet(0)
                data.handle_raise()# if the person clicks the middle button it will do the raise function

            if 750 <= self.__mouse[0] <= 750+140 and 775 // 2 <= self.__mouse[1] <= 775 // 2+40:
                data.handle_fold("player") # if the person clicks the bottom button it will do the fold function
                deck.increase_count()

            if 655 <= self.__mouse[0] <= 655 + 75 and 525 <= self.__mouse[1] <= 525 + 50:
                data.set_bet(25)
                data.handle_raise()

            if 770 <= self.__mouse[0] <= 770 + 75 and 525 <= self.__mouse[1] <= 525 + 50:
                data.set_bet(50)
                data.handle_raise()

            if 885 <= self.__mouse[0] <= 885 + 75 and 525 <= self.__mouse[1] <= 525 + 50:
                data.set_bet(100)
                data.handle_raise()

    def button(self,x,y,text,x2,y2):
        if data.get_turn() % 2 == 0 and data.check_end() != True: # if its the players turn
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

    def raise_button(self):
        if data.get_raised() == 1:
            self.button(655,525,"25",75,50)
            self.button(770,525,"50",75,50)
            self.button(885,525,"100",100,50)

    def ai_turn(self):
        if data.get_turn() % 2 == 1:
            data.set_ai_bet(self.__ai_player.calculate_bet())

            if data.get_ai_bet() == 0 and not data.total_bet():
                data.handle_fold("ai")
                deck.increase_count()
                print("ai folded",)
            else:
                data.handle_ai_call(data.get_ai_bet())



    def check_win(self):
        if data.get_round() == 5:
            #print("A")
            time.wait(1000) # waits a second before the game ends
            ai = self.__ai_player.find_outs(self.__ai_formatter.order_cards()) # ai card hand value is findOuts[1]
            p1 = self.__human_player.find_outs(self.__player_formatter.order_cards()) # user card hand value is findOuts[1]
            print(self.__ai_formatter.order_cards(),self.__player_formatter.order_cards()) # prints ai cards then players
            print(ai,p1) # prints ai value then user value

            if ai[0] == -1 and p1[0] == -1:
                if ai[1] < p1[1]:
                    data.handle_fold("player")
                    print('ai win')
                else:
                    data.handle_fold("ai")
                    print('user win')

            elif ai[0] == -1:
                data.handle_fold("player")
                print('ai win')

            elif p1[0] == -1:
                data.handle_fold("ai")
                print('user win')

            deck.increase_count()


    def display_round(self):
        screen.blit(self.__font.render("Round: "+str(data.get_round()), True, white, green),(150+5,100+5)) # bilts the round number in the top left of the green rectangle

    def display_balance(self):
        screen.blit(self.__font.render(str(data.get_player_1_balance()), True, white, green),(450+22,412)) #blits the player 1 balance to tge screen
        screen.blit(self.__font.render(str(data.get_player_2_balance()), True, white, green),(450+22,160)) #blits the player 2 balance to the screen
        screen.blit(self.__font.render(str(data.get_pot()), True, white, green),(205,275))

    def display_player_cards(self):
        self.__font = font.Font('freesansbold.ttf',32) # choosing the font and size of the text

        draw.rect(screen, grey, Rect(425,460,150,80)) # draws grey rectangle where player cards are
        draw.rect(screen, grey, Rect(425,60,150,80)) # draws grey rectangle where ai cards would be but face down

        draw.rect(screen, white, Rect(425,460,150,80), 2) # draws white outline around grey player rectangle
        draw.rect(screen, white, Rect(425,60,150,80), 2) # draws white outline around grey ai rectangle

        screen.blit(self.__font.render(str(deck.get_p1_cards()[0]), True, white, grey),(445,485)) #blit first player card from the deck class
        screen.blit(self.__font.render(str(deck.get_p1_cards()[1]), True, white, grey),(510,485)) # blit second player card from the deck class

    def display_table_cards(self):
        # uses the community cards from the cards.py file. displays them based on the round of the game
        if data.get_round() >= 2:
            screen.blit(self.__font.render(str(deck.get_community_cards()[0]), True, white, green),(330 + 28,275))
            screen.blit(self.__font.render(str(deck.get_community_cards()[1]), True, white, green),(390 + 28,275))
            screen.blit(self.__font.render(str(deck.get_community_cards()[2]), True, white, green),(450 + 28,275))

        if data.get_round() >= 3:
            screen.blit(self.__font.render(str(deck.get_community_cards()[3]), True, white, green),(510 + 28,275))

        if data.get_round() >=4:
            screen.blit(self.__font.render(str(deck.get_community_cards()[4]), True, white, green),(570 + 28,275))

    def main(self):
        #variable to control game loop
        stopped = False

        while not stopped:
            #sets round number based off how many player turns have occured
            data.increment_round(1 + data.get_turn() // 2)

            #sets up background
            screen.fill(blue) #background colour
            draw.rect(screen, green, Rect(150,100,700,400)) # draws green table
            draw.rect(screen, white, Rect(150,100,700,400),2) # white table outline

            # displays all cards and balances
            self.display_player_cards()
            self.display_balance()
            self.display_table_cards()
            self.display_round()

            #gets mouse pos for the event handler
            self.__mouse = mouse.get_pos()

            #loop for pygame events
            for e in event.get():
                if e.type == QUIT: # to quit the game
                    quit()

                if e.type == MOUSEBUTTONDOWN: # if they left click the mouse
                    self.handle_mouse()

                if e.type == KEYDOWN:  #
                    if e.key == K_1: # uses button 1
                        print("a")


            # uses the button function to make the 3 call, raise and fold buttons
            self.button(750,163,'Call',150,50)
            self.button(750,275,'Raise',150,50)
            self.button(750,388,'Fold',150,50)

            self.raise_button()
            self.ai_turn()


            self.check_win()

            # sets the clock and updates the display
            clock.tick(60)
            display.update()


#creates object of the class and then runs the main method
game_screen = GameScreen(display_width,display_height)
game_screen.main()
