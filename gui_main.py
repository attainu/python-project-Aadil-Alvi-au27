import gc
import pygame, sys
import random
import time


class run:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((650,500))

        pygame.display.set_caption("Snakes And Ladders")
        
        # initializing Background Image
        self.Full_Background = "assets/images/full_bg.jpg"
        self.full_bg = pygame.image.load(self.Full_Background)
        self.Background = "assets/images/background.jpg"
        self.bg = pygame.image.load(self.Background)
        self.bx=150
        self.by=0

        #initializing Players
        self.green_src = "assets/images/green.png"
        self.green=pygame.image.load(self.green_src)
        self.blue_src = "assets/images/blue.png"
        self.blue=pygame.image.load(self.blue_src)
        self.g_x=100
        self.g_y=251
        self.b_x=100
        self.b_y=362
        
        #initializing Players names and fonts
        self.font1=pygame.font.SysFont("comicsansms",25)

        self.font2=pygame.font.SysFont("comicsansms",20)

        self.font3=pygame.font.SysFont("comicsansms",40)


        #initializing Dice
        self.dice_button_src = "assets/images/dice-ready.png"
        self.dice_button = pygame.image.load(self.dice_button_src)       
        self.dB_x=2
        self.dB_y=50


    def Display(self):
        self.screen.blit(self.full_bg,(0,500))
        self.screen.blit(self.bg,(self.bx,self.by))
        self.screen.blit(self.blue,(self.b_x,self.b_y))
        self.screen.blit(self.green,(self.g_x,self.g_y))
            
    def Dice_button(self):
        self.screen.blit(self.dice_button,(self.dB_x,self.dB_y))

    def dice_roll(self):
        dice_value = random.randint(1,6)
        if dice_value==1:
            dice=pygame.image.load("assets/images/dice1.png")
        elif dice_value==2:
            dice=pygame.image.load("assets/images/dice2.png")
        elif dice_value==3:
            dice=pygame.image.load("assets/images/dice3.png")
        elif dice_value==4:
            dice=pygame.image.load("assets/images/dice4.png")
        elif dice_value==5:
            dice=pygame.image.load("assets/images/dice5.png")
        elif dice_value==6:
            dice=pygame.image.load("assets/images/dice6.png")
        return(dice,dice_value)
    
    def players(self):
        msg1=self.font1.render("Player 1",True,(0,255,0))
        self.screen.blit(msg1,[5,251])
        msg2=self.font1.render("Player 2",True,(0,0,255))
        self.screen.blit(msg2,[5,362])

    def turns_green(self):
        msg3=self.font2.render("Your turn",True,(255,255,255))
        self.screen.blit(msg3,[20,300])
    def turns_Blue(self):
        msg3=self.font2.render("Your turn",True,(255,255,255))
        self.screen.blit(msg3,[20,400])

    
    def Act(self):  
        button=pygame.Rect(2,50,60,60)
        running=True
        turn="green"
        while running:
            self.screen.fill((0,255,195))
            self.Display()
            self.players()
            self.Dice_button()
            if turn=="green":
                self.turns_green()
            elif turn=="blue":
                self.turns_Blue()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    if button.collidepoint(mouse_pos):
                        self.dice_roll()
                        dice,dice_value=self.dice_roll()
                        self.screen.blit(dice,(20,120))
                    
                    # for green turn
                    if self.dice_roll() and turn=="green":
                        turn="blue"
                        if dice_value==6 and self.g_x==100 and self.g_y==251:
                            self.g_x=162 
                            self.g_y=447
                            turn="green"
                        elif self.g_x in range(162,358) and dice_value!=6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*dice_value)
                        elif self.g_x in range(162,358) and dice_value==6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*dice_value)
                            turn="green"
                        elif self.g_x==358 and dice_value!=6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*dice_value)
                        elif self.g_x==358 and dice_value==6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*5)
                            self.g_y-=49
                            turn="green"
                        elif self.g_x==407 and dice_value<=4 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):#7
                            self.g_x+=(49*dice_value)

                        elif self.g_x==407 and dice_value>4 and dice_value!=6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*4)
                            self.g_y-=49
                        elif self.g_x==407 and dice_value==6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*4)-(49*(dice_value-5))
                            self.g_y-=49
                            turn=="green"
                        elif self.g_x==456 and dice_value<=3 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):#8
                            self.g_x+=(49*dice_value)
                        elif self.g_x==456 and dice_value>3 and dice_value!=6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*3)-(49*(dice_value-4))
                            self.g_y-=49
                        elif self.g_x==456 and dice_value==6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*3)-(49*(dice_value-4))
                            self.g_y-=49
                            turn=="green"
                        elif self.g_x==505 and dice_value<=2 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):#9
                            self.g_x+=(49*dice_value)
                        elif self.g_x==505 and dice_value>2 and dice_value!=6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*2)-(49*(dice_value-3))
                            self.g_y-=49
                        elif self.g_x==505 and dice_value==6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*2)-(49*(dice_value-3))
                            self.g_y-=49
                            turn=="green"
                        elif self.g_x==554 and dice_value==1 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):#10
                            self.g_x+=(49*dice_value)
                        elif self.g_x==554 and dice_value>1 and dice_value!=6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49)-(49*(dice_value-2))
                            self.g_y-=49
                        elif self.g_x==554 and dice_value==6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49)-(49*(dice_value-2))
                            self.g_y-=49
                            turn=="green"
                        elif self.g_x>=603 and dice_value!=6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*(dice_value-1))
                            self.g_y-=49

                        elif self.g_x==603 and dice_value==6 and (self.g_y==447 or self.g_y==349 or self.g_y==251 or self.g_y==153 or self.g_y==55):
                            self.g_x+=(49*(dice_value-1))
                            self.g_y-=49
                            turn=="green" 

                    #Second Row
                        elif self.g_x>358 and self.g_x<=603 and dice_value!=6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value))
                        elif self.g_x>358 and self.g_x<=603 and dice_value==6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(5))
                            self.g_y-=49
                        elif self.g_x>407 and self.g_x<=603 and dice_value!=6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value))
                        elif self.g_x>407 and self.g_x<=603 and dice_value==6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value))  
                            turn="green"
                        elif self.g_x==407 and dice_value!=6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value)) 
                        elif self.g_x==407 and dice_value==6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(5))
                            self.g_y-=49
                            turn="green" 
                        elif self.g_x==358 and dice_value<5 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value)) 
                        elif self.g_x==358 and dice_value==5 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(4))+(49*(dice_value-5))
                            self.g_y-=49
                        elif self.g_x==358 and dice_value==6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(4))+(49*(dice_value-5))
                            self.g_y-=49
                            turn="green" 
                        elif self.g_x==309 and dice_value<4 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value)) 
                        elif self.g_x==309 and dice_value>=4 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(3))+(49*(dice_value-4))
                            self.g_y-=49
                        elif self.g_x==309 and dice_value==6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(3))+(49*(dice_value-4))
                            self.g_y-=49
                            turn="green" 
                        elif self.g_x==260 and dice_value<3 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value)) 
                        elif self.g_x==260 and dice_value>=3 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(2))+(49*(dice_value-3))
                            self.g_y-=49
                        elif self.g_x==260 and dice_value==6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(2))+(49*(dice_value-3))
                            self.g_y-=49
                            turn="green" 
                        elif self.g_x==211 and dice_value<2 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value)) 
                        elif self.g_x==211 and dice_value>=2 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49)+(49*(dice_value-2))
                            self.g_y-=49
                        elif self.g_x==211 and dice_value==6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49)+(49*(dice_value-2))
                            self.g_y-=49
                            turn="green" 
                        elif self.g_x==162 and dice_value!=6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value-1))
                            self.g_y-=49
                        elif self.g_x==162 and dice_value==6 and (self.g_y==398  or self.g_y==300 or self.g_y==202 or self.g_y==104 or self.g_y==6):
                            self.g_x-=(49*(dice_value-1))
                            self.g_y-=49
                            turn="green" 

                        # code for final row:
                        elif self.g_y==6 and (self.g_x==554 or self.g_x==603) and dice_value!=6:
                            self.g_x-=(49*dice_value)
                        elif self.g_y==6 and (self.g_x==554 or self.g_x==603) and dice_value==6:
                            self.g_x-=(49*dice_value)
                            turn="green"
                        elif self.g_y==6 and self.g_x==456 and dice_value<5:
                            self.g_x-=(49*dice_value)
                        elif self.g_y==6 and self.g_x==456 and dice_value==5:
                            self.g_x-=(49*dice_value)
                            if self.g_x==211 and self.g_y==6 and dice_value==5:
                                self.g_x=162
                                self.g_y=251
                        elif self.g_y==6 and self.g_x==456 and dice_value==6:
                            self.g_x=self.g_x
                        elif self.g_y==6 and self.g_x==505 and dice_value!=6:
                            self.g_x-=(49*dice_value)
                        elif self.g_y==6 and self.g_x==505 and dice_value==6:
                            self.g_x-=(49*dice_value)
                            if self.g_x==211 and self.g_y==6 and dice_value==6:
                                self.g_x=162
                                self.g_y=251

                        elif self.g_y==6 and self.g_x==407 and dice_value<6:
                            self.g_x-=(49*dice_value)
                            if self.g_x==211 and self.g_y==6 and dice_value==4:
                                self.g_x=162
                                self.g_y=251
                        elif self.g_y==6 and self.g_x==407 and self.g_x>=162 and dice_value==6:
                            self.g_x=self.g_x

                        elif self.g_y==6 and self.g_x==358 and self.g_x>=162 and dice_value>=5:
                            self.g_x=self.g_x
                        elif self.g_y==6 and self.g_x==358 and self.g_x>=162 and dice_value<5:
                            self.g_x-=(49*dice_value)
                            if self.g_x==211 and self.g_y==6 and dice_value==3:
                                self.g_x=162
                                self.g_y=251

                        elif self.g_y==6 and self.g_x==309 and self.g_x>=162 and dice_value>=4:
                            self.g_x=self.g_x
                        elif self.g_y==6 and self.g_x==309 and self.g_x>=162 and dice_value<4:
                            self.g_x-=(49*dice_value)
                            if self.g_x==211 and self.g_y==6 and dice_value==2:
                                self.g_x=162
                                self.g_y=251

                        elif self.g_y==6 and self.g_x==260 and self.g_x>=162 and dice_value>=3:
                            self.g_x=self.g_x
                        elif self.g_y==6 and self.g_x==260 and self.g_x>=162 and dice_value<3:
                            self.g_x-=(49*dice_value)
                            if self.g_x==211 and self.g_y==6 and dice_value==1:
                                self.g_x=162
                                self.g_y=251
                        elif self.g_y==6 and self.g_x==211 and self.g_x>=162 and dice_value>=2:
                            self.g_x=self.g_x


                    # for blue turn
                    elif self.dice_roll() and turn=="blue":
                        turn="green"                    
                        if dice_value==6 and self.b_x==100 and self.b_y==362:
                            self.b_x=162 
                            self.b_y=450
                            turn="blue"
                        #code for odd no of rows
                        elif self.b_x in range(162,358) and dice_value!=6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*dice_value)
                        elif self.b_x in range(162,358) and dice_value==6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*dice_value)
                            turn="blue"
                        elif self.b_x==358 and dice_value!=6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*dice_value)
                        elif self.b_x==358 and dice_value==6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*5)
                            self.b_y-=49
                            turn="blue"
                        elif self.b_x==407 and dice_value<=4 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):#7
                            self.b_x+=(49*dice_value)

                        elif self.b_x==407 and dice_value>4 and dice_value!=6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*4)
                            self.b_y-=49
                        elif self.b_x==407 and dice_value==6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*4)-(49*(dice_value-5))
                            self.b_y-=49
                            turn=="blue"
                        elif self.b_x==456 and dice_value<=3 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):#8
                            self.b_x+=(49*dice_value)
                        elif self.b_x==456 and dice_value>3 and dice_value!=6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*3)-(49*(dice_value-4))
                            self.b_y-=49
                        elif self.b_x==456 and dice_value==6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*3)-(49*(dice_value-4))
                            self.b_y-=49
                            turn=="blue"
                        elif self.b_x==505 and dice_value<=2 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):#9
                            self.b_x+=(49*dice_value)
                        elif self.b_x==505 and dice_value>2 and dice_value!=6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*2)-(49*(dice_value-3))
                            self.b_y-=49
                        elif self.b_x==505 and dice_value==6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*2)-(49*(dice_value-3))
                            self.b_y-=49
                            turn=="blue"
                        elif self.b_x==554 and dice_value==1 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):#10
                            self.b_x+=(49*dice_value)
                        elif self.b_x==554 and dice_value>1 and dice_value!=6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49)-(49*(dice_value-2))
                            self.b_y-=49
                        elif self.b_x==554 and dice_value==6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49)-(49*(dice_value-2))
                            self.b_y-=49
                            turn=="blue"
                        elif self.b_x>=603 and dice_value!=6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*(dice_value-1))
                            self.b_y-=49

                        elif self.b_x==603 and dice_value==6 and (self.b_y==450 or self.b_y==352 or self.b_y==254 or self.b_y==156 or self.b_y==58):
                            self.b_x+=(49*(dice_value-1))
                            self.b_y-=49
                            turn=="blue" 

                    #code for even numbers of rows 
                        elif self.b_x>358 and self.b_x<=603 and dice_value!=6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value))
                        elif self.b_x>358 and self.b_x<=603 and dice_value==6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(5))
                            self.b_y-=49
                        elif self.b_x>407 and self.b_x<=603 and dice_value!=6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value))
                        elif self.b_x>407 and self.b_x<=603 and dice_value==6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value))  
                            turn="blue"
                        elif self.b_x==407 and dice_value!=6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value)) 
                        elif self.b_x==407 and dice_value==6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(5))
                            self.b_y-=49
                            turn="blue" 
                        elif self.b_x==358 and dice_value<5 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value)) 
                        elif self.b_x==358 and dice_value==5 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(4))+(49*(dice_value-5))
                            self.b_y-=49
                        elif self.b_x==358 and dice_value==6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(4))+(49*(dice_value-5))
                            self.b_y-=49
                            turn="blue" 
                        elif self.b_x==309 and dice_value<4 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value)) 
                        elif self.b_x==309 and dice_value>=4 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(3))+(49*(dice_value-4))
                            self.b_y-=49
                        elif self.b_x==309 and dice_value==6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(3))+(49*(dice_value-4))
                            self.b_y-=49
                            turn="blue" 
                        elif self.b_x==260 and dice_value<3 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value)) 
                        elif self.b_x==260 and dice_value>=3 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(2))+(49*(dice_value-3))
                            self.b_y-=49
                        elif self.b_x==260 and dice_value==6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(2))+(49*(dice_value-3))
                            self.b_y-=49
                            turn="blue" 
                        elif self.b_x==211 and dice_value<2 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value)) 
                        elif self.b_x==211 and dice_value>=2 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49)+(49*(dice_value-2))
                            self.b_y-=49
                        elif self.b_x==211 and dice_value==6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49)+(49*(dice_value-2))
                            self.b_y-=49
                            turn="blue" 
                        elif self.b_x==162 and dice_value!=6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value-1))
                            self.b_y-=49
                        elif self.b_x==162 and dice_value==6 and (self.b_y==401  or self.b_y==303 or self.b_y==205 or self.b_y==107 or self.b_y==9):
                            self.b_x-=(49*(dice_value-1))
                            self.b_y-=49
                            turn="blue"

                        # code for final row:


                        elif self.b_y==9 and (self.b_x==554 or self.b_x==603) and dice_value!=6:
                            self.b_x-=(49*dice_value)
                        elif self.b_y==9 and (self.b_x==554 or self.b_x==603) and dice_value==6:
                            self.b_x-=(49*dice_value)
                            turn="blue"
                        elif self.b_y==9 and self.b_x==456 and dice_value<5:
                            self.b_x-=(49*dice_value)
                        elif self.b_y==9 and self.b_x==456 and dice_value==5:
                            self.b_x-=(49*dice_value)
                            if self.b_x==211 and self.b_y==9 and dice_value==5:
                                self.b_x=162
                                self.b_y=254
                        elif self.b_y==6 and self.b_x==456 and dice_value==6:
                            self.b_x=self.b_x
                        elif self.b_y==6 and self.b_x==505 and dice_value!=6:
                            self.b_x-=(49*dice_value)
                        elif self.b_y==9 and self.b_x==505 and dice_value==6:
                            self.b_x-=(49*dice_value)
                            if self.b_x==211 and self.b_y==9 and dice_value==6:
                                self.b_x=162
                                self.b_y=254

                        elif self.b_y==9 and self.b_x==407 and dice_value<6:
                            self.b_x-=(49*dice_value)
                            if self.b_x==211 and self.b_y==9 and dice_value==4:
                                self.b_x=162
                                self.b_y=254
                        elif self.b_y==9 and self.b_x==407 and self.b_x>=162 and dice_value==6:
                            self.b_x=self.b_x

                        elif self.b_y==9 and self.b_x==358 and self.b_x>=162 and dice_value>=5:
                            self.b_x=self.b_x
                        elif self.b_y==9 and self.b_x==358 and self.b_x>=162 and dice_value<5:
                            self.b_x-=(49*dice_value)
                            if self.b_x==211 and self.b_y==9 and dice_value==3:
                                self.b_x=162
                                self.b_y=254

                        elif self.b_y==9 and self.b_x==309 and self.b_x>=162 and dice_value>=4:
                            self.b_x=self.b_x
                        elif self.b_y==9 and self.b_x==309 and self.b_x>=162 and dice_value<4:
                            self.b_x-=(49*dice_value)
                            if self.b_x==211 and self.b_y==9 and dice_value==2:
                                self.b_x=162
                                self.b_y=254

                        elif self.b_y==9 and self.b_x==260 and self.b_x>=162 and dice_value>=3:
                            self.b_x=self.b_x
                        elif self.b_y==9 and self.b_x==260 and self.b_x>=162 and dice_value<3:
                            self.b_x-=(49*dice_value)
                            if self.b_x==211 and self.b_y==9 and dice_value==1:
                                self.b_x=162
                                self.b_y=254
                        elif self.b_y==9 and self.b_x==211 and self.b_x>=162 and dice_value>=2:
                            self.b_x=self.b_x
        
            pygame.display.update()

            if self.g_x==162 and self.g_y==6:
                self.screen.fill((50,153,213))
                value = self.font3.render("Green won",True,(255,255,102))
                
                self.screen.blit(value,[250,200])

                running=False

            if self.b_x==162 and self.b_y==9:
                self.screen.fill((50,153,213))
                value = self.font3.render("Blue won",True,(255,255,102))
                
                self.screen.blit(value,[250,200])

                running=False
            time.sleep(1)
        pygame.quit()
        quit()
    


