import pygame, sys, random
from pygame.locals import *
pygame.init()

##—————PRESETS
FPS = 60
fpsClock = pygame.time.Clock()


DWidth = 1300
DHeight = 650

DISPLAY = pygame.display.set_mode((DWidth, DHeight), 0, 32)
pygame.display.set_caption = "Game Window_Zombocalypse"

#pygame.mixer.music.load('GameMusic.wav')
#mrpygame.mixer.music.play(-1)

# Above is the pygame setup
##————LOADING stuff

door = pygame.image.load("Door.png")
opendoor = pygame.image.load("opendoor.png")
key1 = pygame.image.load("keyyy.png")

p1Right = pygame.image.load("lookright.gif")
p1Left = pygame.image.load("lookleft.gif")
p1RightLeft = pygame.image.load("lookrightstepleft.gif")
p1RightRight = pygame.image.load("lookrightstepright.gif")
p1LeftRight = pygame.image.load("lookleftstepright.gif")
p1LeftLeft = pygame.image.load("lookleftstepleft.gif")
heart = pygame.image.load("Heart.png")
emptyheart = pygame.image.load("Blackheart.png")

Mummyright = pygame.image.load("Mummy_Right.png")
Mummyleft = pygame.image.load("Mummy_Left.png")
arrow = pygame.image.load("BoostIcon.png")

coinpickup = pygame.mixer.Sound("Coinpick.wav")
zombie = pygame.image.load("Zombie.png")

Fireguyright = pygame.image.load("fireball.png")
Ghostleft = pygame.image.load("ghost.png")
Ghostright = pygame.image.load("ghostright.png")
grunt = pygame.mixer.Sound("grunt.wav")

spikesright = pygame.image.load("spikesright.png")
spikesleft = pygame.image.load("spikesleft.png")

bat = pygame.image.load("bat.png")
coin = pygame.image.load('coin.png')
#constant vars
level1 = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
Yellow = (255, 255, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
LIGHTNING = (204, 255, 255)
speed = 3
mspeed = 3
n = 5
j = 5
k = 6
coinone = True
Ghost = Ghostleft
font_choice = pygame.font.SysFont("Black Ops", 50, True, True)
#Variables that change


youwin = False
level2 = False
Lose = False
Pause = False
Startup = True

scoretimer = 0.0

Greyback = True
bgtimer = 0
steppin = p1RightRight
direction = p1Right
steppinl=p1Left
score = 0
timer = 0 
pausetimer = 0
step = 24
dx = 60
dy = 170
gx = 1200
gy = 450
drectx = 95
drecty = 198
w = 25
h = 730
face = p1Right
side = 0
keygot = j
zrectx = 41
zrecty = 41
zrectx1 = 41
zrecty1 = 45
zrectx2 = 41
zrecty2 = 45
zrectx3 = 41
zrecty3 = 45
zrectx4 = 41
zrecty4 = 45
zrectx5 = 41
zrecty5 = 45
zrectx6 = 41
zrecty6 = 45
zomdir = 0
#zomdir1 = 0
#zomdir2 = 0
#zomdir3 = 0
#zomdir4 = 0
#zomdir5 = 0
#zomdir6 = 0
lives=3
mrectx=750
mrecty=500
firex = 720
firey = 570
fdir=1
batx = 353
baty = 500
batdir = 0
####Function
def walls(wx, wy, ww, wh): #wall loop
    pygame.draw.rect(DISPLAY, BLACK, (wx, wy, ww, wh))
    
def coins(coinx, coiny, coinnum, score): #coin loop
    coinnum = pygame.Rect(coinx+1, coiny, 28, 32)
    DISPLAY.blit(coin, (coinx, coiny))
    return coinnum

def main():
    fpsClock.tick(FPS)
    if Greyback == True:
        DISPLAY.fill(GRAY)
    else:
        DISPLAY.fill(RED)
        bgtimer = bgtimer + 1
    if bgtimer == 10:
        Greyback = True
        bgtimer = 0
    #level 1 stuff starts
    ghost=pygame.Rect(gx+25, gy+8, 43, 39)#Ghost
    DISPLAY.blit(Ghost, (gx, gy))

    
    passage=pygame.draw.rect(DISPLAY, BLACK, (540, 130, 20, 250))

    spike1 = pygame.Rect(1220, 211, 50, 50)
    spike2 = pygame.Rect(1265, 392, 30, 50)
    spike3 = pygame.Rect(1160, 391, 25, 50)
    DISPLAY.blit(spikesright, (1234, 211))
    DISPLAY.blit(spikesleft, (1220, 210))
    DISPLAY.blit(spikesright, (1149, 390))
    DISPLAY.blit(spikesleft, (1265, 390))

    
    wall1 = walls(0, 0, 20, DHeight)   #Black walls
    wall2 = walls(0, DHeight - 20, DWidth, 20) 
    wall3 = walls(0, 0, DWidth, 20)
    wall4 = walls(DWidth - 20, 0, 20, 790)
    wall5 = walls(150, 0, 20, 490)
    wall6 = walls(300, 530, 20, 100)
    wall7 = walls(350, 150, 20, 230)
    wall8 = walls(350, 360, 210, 20)
    wall9= walls(450, 360, 20, 150)

    wall10 = walls(690, 250, 20, 600)
    wall11 = walls(540, 130, 600, 20)
    wall12 = walls(1140, 130, 20, 500)
    wall13 = walls(820, 300, 200, 20)



    #EXAMPLE
#    def things_dodged(count):
#    font = pygame.font.SysFont(None, 25)
#    text = font.render("Dodged: "+str(count), True, black)
#    gameDisplay.blit(text,(0,0)

    DISPLAY.blit(arrow, (542, 300))
    DISPLAY.blit(arrow, (542, 210))    
    wall1right= pygame.Rect(0, 0, 20, DHeight)  # collision boxes for walls,     
    wall2up=pygame.Rect(0, DHeight - 20, DWidth, 20) #the side/up/down refers to
    wall3down=pygame.Rect(0, 0, DWidth, 20)     #where on the wall(so up is the 
    wall4left=pygame.Rect(DWidth - 21, 0, 20, 790)#top)
    wall5left = pygame.Rect(150, 0, 10, 487)
    wall5right=pygame.Rect(160, 0, 10, 487)
    wall5down=pygame.Rect(152, 480, 16, 10)
    wall6left=pygame.Rect(300, 533, 10, 97)
    wall6right=pygame.Rect(310, 533, 10, 97)
    wall6up=pygame.Rect(304, 530, 12, 10)
    wall7left=pygame.Rect(350, 153, 10, 224)
    wall7right=pygame.Rect(360, 153, 10, 224)
    wall7up=pygame.Rect(354, 150, 13, 10)
    wall7down=pygame.Rect(354, 370, 13, 10)
    wall8up=pygame.Rect(353, 360, 205, 10)
    wall8down=pygame.Rect(353, 370, 205, 10)
    wall8right=pygame.Rect(550, 362, 10, 14)
    wall9left=pygame.Rect(450, 364, 10, 144)
    wall9right=pygame.Rect(460, 364, 10, 144)
    wall9down=pygame.Rect(452, 500, 14, 12)
    wall10left=pygame.Rect(690, 253, 10, 397)
    wall10right=pygame.Rect(700, 253, 10, 397)
    wall10up=pygame.Rect(692, 249, 16, 10)
    wall11up=pygame.Rect(543, 130, 614, 10)
    wall11down=pygame.Rect(543, 140, 614, 10)
    wall12left=pygame.Rect(1140, 133, 10, 500)
    wall12right=pygame.Rect(1150, 133, 10, 500)
    passageleft=pygame.Rect(540, 133, 17, 244)
    wall13up=pygame.Rect(823, 300, 194, 10)
    wall13down=pygame.Rect(823, 310, 194, 10)
    wall13left=pygame.Rect(820, 304, 10, 13)
    wall13right=pygame.Rect(1010, 304, 10, 13)
    #Level 1 stuff stops
    ##----------SCORING
    if lives==3:                            #blits hearts
        DISPLAY.blit(heart, (1100, 0))
        DISPLAY.blit(heart, (1150, 0))
        DISPLAY.blit(heart, (1200, 0))
    if lives==2:
        DISPLAY.blit(heart, (1150, 0))
        DISPLAY.blit(heart, (1200, 0))
        DISPLAY.blit(emptyheart, (1100, 0))
    if lives==1:
        DISPLAY.blit(heart, (1200, 0))
        DISPLAY.blit(emptyheart, (1150, 0))
        DISPLAY.blit(emptyheart, (1100, 0))
    if lives==0:
        Lose=True
    if keygot==j:                       #If you haven't got the key
        keyrect = pygame.Rect(800, 563, 35, 35)
        DISPLAY.blit(key1, (800, 560))
        DISPLAY.blit(door, (1180, 540))
    elif keygot == k:                   #If you copped it
        DISPLAY.blit(key1, (1050, 0))
        keyrect = pygame.Rect(8000, 23333, 1, 1)
        DISPLAY.blit(opendoor, (1180, 535))
        
#----------------character
        
    charRect = pygame.Rect(drectx,drecty, 54, 56)#caracter collision box
    DISPLAY.blit(face, (dx, dy)) #d=deadpool, creates character !!!!!!!!!!!!
    #level 1 start
#------------------door/key collision
    
    doorRect = pygame.Rect(1180, 540, 88, 89)
    if charRect.colliderect(keyrect) == True:
        keygot = k
        coinpickup.play()
        
#-------------------coin

    coins(70, 30, coinone, score)
#    if charRect.colliderect(coinone) == True:
#        score = score + 10
#        coinx = -100
#------------------zombie
    
    zomr = pygame.Rect(zrectx, zrecty, 52, 62)#zombies
    DISPLAY.blit(zombie, (zrectx-21, zrecty-15))

    
 #   zomr1 = pygame.Rect(zrectx1, zrecty1, 52, 62)
 #   DISPLAY.blit(zombie, (zrectx1-21, zrecty1-15))
    
        
 #   zomr2 = pygame.Rect(zrectx2, zrecty2, 52, 62)
 #   DISPLAY.blit(zombie, (zrectx2-21, zrecty2-15))
    
      
 #   zomr3 = pygame.Rect(zrectx3, zrecty3, 52, 62)
 #   DISPLAY.blit(zombie, (zrectx3-21, zrecty3-15))

      
 #   zomr4 = pygame.Rect(zrectx4, zrecty4, 52, 62)
 #   DISPLAY.blit(zombie, (zrectx4-21, zrecty4-15))

      
 #   zomr5 = pygame.Rect(zrectx5, zrecty5, 52, 62)
 #   DISPLAY.blit(zombie, (zrectx5-21, zrecty5-15))

      
 #   zomr6 = pygame.Rect(zrectx6, zrecty6, 52, 62)
 #   DISPLAY.blit(zombie, (zrectx6-21, zrecty6-15))
    

##----------ENVIRONMENT COLLISION
    if charRect.colliderect(wall5left)==True:  #if hits left side of wall cant go right
        rightkeyability=k
    elif charRect.colliderect(wall6left)==True:
        rightkeyability=k
    elif charRect.colliderect(wall7left)==True:
        rightkeyability=k
    elif charRect.colliderect(wall4left)==True:
        rightkeyability=k
    elif charRect.colliderect(wall9left)==True:
        rightkeyability=k
    elif charRect.colliderect(wall10left)==True:
        rightkeyability=k
    elif charRect.colliderect(passageleft)==True:
        rightkeyability=k
    elif charRect.colliderect(wall12left)==True:
        rightkeyability=k
    elif charRect.colliderect(wall13left)==True:
        rightkeyability=k
    else:
        rightkeyability=j
        
    if charRect.colliderect(wall5right)==True: #if hits right side of wall cant go left
        leftkeyability=k
    elif charRect.colliderect(wall6right)==True:
        leftkeyability=k
    elif charRect.colliderect(wall7right)==True:
        leftkeyability=k
    elif charRect.colliderect(wall1right)==True:
        leftkeyability=k
    elif charRect.colliderect(wall8right)==True:
        leftkeyability=k
    elif charRect.colliderect(wall9right)==True:
        leftkeyability=k
    elif charRect.colliderect(wall10right)==True:
        leftkeyability=k
    elif charRect.colliderect(wall12right)==True:
        leftkeyability=k
    elif charRect.colliderect(wall13right)==True:
        leftkeyability=k
    else:
        leftkeyability=j

    if charRect.colliderect(wall2up)==True: #if hits top side of wall cant go down
        downkeyability=k
    elif charRect.colliderect(wall6up)==True:
        downkeyability=k
    elif charRect.colliderect(wall7up)==True:
        downkeyability=k
    elif charRect.colliderect(wall8up)==True:
        downkeyability=k
    elif charRect.colliderect(wall10up)==True:
        downkeyability=k
    elif charRect.colliderect(wall11up)==True:
        downkeyability=k
    elif charRect.colliderect(wall13up)==True:
        downkeyability=k
    else:
        downkeyability=j
        
    if charRect.colliderect(wall3down)==True: #if hits bottom side of wall cant go up
        upkeyability=k
    elif charRect.colliderect(wall5down)==True:
        upkeyability=k
    elif charRect.colliderect(wall7down)==True:
        upkeyability=k
    elif charRect.colliderect(wall8down)==True:
        upkeyability=k
    elif charRect.colliderect(wall9down)==True:
        upkeyability=k
    elif charRect.colliderect(wall11down)==True:
        upkeyability=k
    elif charRect.colliderect(wall13down)==True:
        upkeyability=k
    else:
        upkeyability=j
    #level 1 stop

##----------MOVEMENT
    key = pygame.key.get_pressed() # create an array that holds all the positions of the keys
    if key[pygame.K_UP] == True and upkeyability==j:# check if the position of pygame.K_UP in the keys array is True
                     # if it is true, it means this key is pressed
                     dy-=speed
                     drecty-=speed
                     checkUp = True
    if key[pygame.K_DOWN] == True and downkeyability==j:#if pressing key and not
                     dy+=speed                          #in wall
                     drecty+=speed
                     checkDown = True
    if key[pygame.K_LEFT] == True and leftkeyability==j:
                     dx-=speed
                     drectx-=speed
                     direction = p1Left
                     checkLeft = True
    if key[pygame.K_RIGHT] == True and rightkeyability==j:
                     dx+=speed
                     drectx+=speed
                     direction = p1Right
                     checkRight = True
    if key[pygame.K_SPACE] == True:
        Pause=True              ################################
                                #####HLIWRESF AKFHDSLKAJFJAFK
                                ################################
#-----------steps
    if key[pygame.K_DOWN] == True or key[pygame.K_RIGHT] == True or key[pygame.K_UP] == True:
        step = step + 1 
        if step > 25 and direction == p1Right:
            if steppin == p1Right or steppin == p1RightLeft:
                steppin = p1RightRight
                face = p1RightRight
                step = 0
            elif steppin == p1RightRight:
                steppin = p1RightLeft
                face = p1RightLeft
                step = 0
                
    if key[pygame.K_DOWN] == True or key[pygame.K_LEFT] == True or key[pygame.K_UP] == True:
        step = step + 1 
        if step > 25 and direction == p1Left:
            if steppinl == p1Left or steppinl == p1LeftLeft:
                steppinl = p1LeftRight
                face = p1LeftRight
                step = 0
            elif steppinl == p1LeftRight:
                steppinl = p1LeftLeft
                face = p1LeftLeft
                step = 0
    if key[pygame.K_DOWN] == False and key[pygame.K_RIGHT] == False and key[pygame.K_UP] ==  False and key[pygame.K_LEFT] == False:
        if direction == p1Left:
            face = p1Left
        elif direction == p1Right:
            face = p1Right


##----------ZOMBIE
       #   zomdir=random.randrange(0, 3)    #0=down, 1=up, 2=left, 3=right
    if zomdir==0:#go down
        zrecty=zrecty+4
    elif zomdir==1:#up
        zrecty=zrecty-4
    elif zomdir==2:#left
        zrectx=zrectx-4
    elif zomdir==3:#right
        zrectx=zrectx+4
    #level 1 start
    if zomr.colliderect(wall5left)==True:#collisions
        zrectx=zrectx-4
        zomdir=random.randint(0, 2)
        if zomdir==2:
            zomdir=3
    elif zomr.colliderect(wall6left)==True:
        zrectx=zrectx-4
        zomdir=random.randint(0, 2)
        if zomdir==2:
            zomdir=3
    elif zomr.colliderect(wall7left)==True:
        zrectx=zrectx-4
        zomdir=random.randint(0, 2)
        if zomdir==2:
            zomdir=3
    elif zomr.colliderect(wall4left)==True:
        zrectx=zrectx-4
        zomdir=random.randint(0, 2)
        if zomdir==2:
            zomdir=3
    elif zomr.colliderect(wall9left)==True:
        zrectx=zrectx-4
        zomdir=random.randint(0, 2)
        if zomdir==2:
            zomdir=3
    elif zomr.colliderect(wall10left)==True:
        zrectx=zrectx-4
        zomdir=random.randint(0, 2)
        if zomdir==2:
            zomdir=3
    elif zomr.colliderect(passageleft)==True:
        zrectx=zrectx-4
        zomdir=random.randint(0, 2)
        if zomdir==2:
            zomdir=3
    elif zomr.colliderect(wall12left)==True:
        zrectx=zrectx-4
        zomdir=random.randint(0, 2)
        if zomdir==2:
            zomdir=3
    elif zomr.colliderect(wall13left)==True:
        zrectx=zrectx-4
        zomdir=random.randint(0, 2)
        if zomdir==2:
            zomdir=3
    
        
    if zomr.colliderect(wall5right)==True:
        zrectx=zrectx+4
        zomdir=random.randint(0, 2)
    elif zomr.colliderect(wall6right)==True:
        zrectx=zrectx+4
        zomdir=random.randint(0, 2)
    elif zomr.colliderect(wall7right)==True:
        zrectx=zrectx+4
        zomdir=random.randint(0, 2)
    elif zomr.colliderect(wall1right)==True:
        zrectx=zrectx+4
        zomdir=random.randint(0, 2)
    elif zomr.colliderect(wall8right)==True:
        zrectx=zrectx+4
        zomdir=random.randint(0, 2)
    elif zomr.colliderect(wall9right)==True:
        zrectx=zrectx+4
        zomdir=random.randint(0, 2)
    elif zomr.colliderect(wall10right)==True:
        zrectx=zrectx+4
        zomdir=random.randint(0, 2)
    elif zomr.colliderect(wall12right)==True:
        zrectx=zrectx+4
        zomdir=random.randint(0, 2)
    elif zomr.colliderect(wall13right)==True:
        zrectx=zrectx+4
        zomdir=random.randint(0, 2)
    

    if zomr.colliderect(wall2up)==True:
        zrecty=zrecty-4
        zomdir=random.randint(1, 3)
    elif zomr.colliderect(wall6up)==True:
        zrecty=zrecty-4
        zomdir=random.randint(1, 3)
    elif zomr.colliderect(wall7up)==True:
        zrecty=zrecty-4
        zomdir=random.randint(1, 3)
    elif zomr.colliderect(wall8up)==True:
        zrecty=zrecty-4
        zomdir=random.randint(1, 3)
    elif zomr.colliderect(wall10up)==True:
        zrecty=zrecty-4
        zomdir=random.randint(1, 3)
    elif zomr.colliderect(wall11up)==True:
        zrecty=zrecty-4
        zomdir=random.randint(1, 3)
    elif zomr.colliderect(wall13up)==True:
        zrecty=zrecty-4
        zomdir=random.randint(1, 3)

        
        
    if zomr.colliderect(wall3down)==True:
        zrecty=zrecty+4
        zomdir=random.randint(1, 3)
        if zomdir==1:
            zomdir=0
    elif zomr.colliderect(wall5down)==True:
        zrecty=zrecty+4
        zomdir=random.randint(1, 3)
        if zomdir==1:
            zomdir=0
    elif zomr.colliderect(wall7down)==True:
        zrecty=zrecty+4
        zomdir=random.randint(1, 3)
        if zomdir==1:
            zomdir=0
    elif zomr.colliderect(wall8down)==True:
        zrecty=zrecty+4 
        zomdir=random.randint(1, 3)
        if zomdir==1:
            zomdir=0
    elif zomr.colliderect(wall9down)==True:
        zrecty=zrecty+4
        zomdir=random.randint(1, 3)
        if zomdir==1:
            zomdir=0
    elif zomr.colliderect(wall11down)==True:
        zrecty=zrecty+4
        zomdir=random.randint(1, 3)
        if zomdir==1:
            zomdir=0
    elif zomr.colliderect(wall13down)==True:
        zrecty=zrecty+4
        zomdir=random.randint(1, 3)
        if zomdir==1:
            zomdir=0
        #level 1 stop
                                ####################
                                ####################
 ##----------CHARACTER COLLISION ##################
    if charRect.colliderect(zomr)==True and timer>50:#If char/zombie collision
        lives=lives-1
        timer=0
        Greyback = False
        grunt.play()
        
    
  
    if charRect.colliderect(doorRect) == True and keygot==k:#door collisions
        youwin=True
    
    elif charRect.colliderect(doorRect) == True:
        text = font_choice.render("Snag the key!", True, Yellow, None)
        textRect = text.get_rect()
        textRect.centerx, textRect.centery = DISPLAY.get_rect().centerx, DISPLAY.get_rect().centery
        DISPLAY.blit(text, textRect)
        #level 1 start
#   fdir=random.randrange(0, 3)    #0=down, 1=up, 2=left, 3=right
    if spike1.colliderect(charRect) and timer>30:
        grunt.play()
        Greyback = False
        timer = 0
        lives = lives - 1
    if spike2.colliderect(charRect) and timer>30:
        grunt.play()
        Greyback = False
        timer = 0
        lives = lives - 1
    if spike3.colliderect(charRect) and timer>30:
        grunt.play()
        Greyback = False
        timer = 0
        lives = lives - 1

##----------FIRE
    fire=pygame.Rect(firex, firey, 50, 55)#fire dude
    DISPLAY.blit(Fireguyright, (firex, firey))
    if fire.colliderect(wall12left):
        fdir=0
        firex=firex-3
    if fire.colliderect(wall10right):
        fdir=1
        firex=firex+3
    if fire.colliderect(wall2up):
        fdir=2
        firey=firey-3
    if fire.colliderect(wall11down):
        fdir=3
        firey=firey+3

        
    if fdir==0:
        firey=firey+5
    if fdir==1:
        firey=firey-5
    if fdir==2:
        firex=firex-5
    if fdir==3:
        firex=firex+5

##----------MUMMY
    mum1= pygame.Rect(mrectx+1, mrecty, 52, 69)#mummy
    
    if mum1.colliderect(wall10right) or mum1.colliderect(wall12left):
        mspeed=-mspeed
        #level 1 stop
    if mspeed >0:
        DISPLAY.blit(Mummyright, (mrectx, mrecty))
    elif mspeed<0:
        DISPLAY.blit(Mummyleft, (mrectx, mrecty))
    mrectx=mrectx+mspeed
    if charRect.colliderect(mum1) and timer>50:
        lives=lives-1
        timer=0
        Greyback = False
        grunt.play()
    if charRect.colliderect(fire) and timer>50:
        lives=lives-1
        timer=0
        Greyback = False
        grunt.play()
    timer=timer+1


##----------BAT
    #level 1 start
    batr = pygame.Rect(batx+1, baty, 68, 45)#bat
    DISPLAY.blit(bat, (batx, baty))

    if batr.colliderect(wall8down):
        batdir = 0
    if batr.colliderect(wall11down):
        batdir = 0
    if batr.colliderect(wall2up) and batx > 400:
        batdir = 2
        baty = baty - 3
    if batr.colliderect(wall2up) and batx < 400:
        batdir = 3
        baty = baty - 3
    if batr.colliderect(wall10left):
        batdir = 1
        batx = batx - 3
    if batr.colliderect(wall6right):
        batdir = 1
        batx = batx + 3
    if batr.colliderect(charRect) and timer >= 50:
        grunt.play()
        Greyback = False
        timer = 0
        lives = lives - 1
        #level 1 stop


# 0 = down, 1 = up, 2 = left, 3 = right
    if batdir==0:
        baty=baty+5
    if batdir==1:
        baty=baty-5
    if batdir==2:
        batx=batx-5
    if batdir==3:
        batx=batx+5

##----------GHOST
    if gx - 12 > dx:#ghost movement
        gx = gx - 1
        Ghost = Ghostleft
    elif gx - 12 == dx:
        Ghost = Ghostleft
    else:
        gx = gx + 1
        Ghost = Ghostright
        
        
    if gy - 20 < dy:
        gy = gy + 1
    
    else:
        gy = gy - 1
    if ghost.colliderect(charRect) and timer > 50:
        grunt.play()
        Greyback = False
        timer = 0
        lives = lives - 1


#-----------SCORE



    score1text = font_choice.render('Score:', True, Yellow, None)
    score1Rect = score1text.get_rect()
    score1Rect.centerx, score1Rect.centery = (100, 15)
    DISPLAY.blit(score1text, score1Rect)


    scoretext = font_choice.render(str(score), True, Yellow, None)
    scoreRect = scoretext.get_rect()
    if score >= 0 and score < 10:
       scoreRect.centerx, scoreRect.centery =(175, 17) 
    if score >= 10 and score < 100:
        scoreRect.centerx, scoreRect.centery =(190, 17)
    if score >= 100 and score < 1000:
        scoreRect.centerx, scoreRect.centery =(130, 15)
    if score >= 1000 and score < 10000:
        scoreRect.centerx, scoreRect.centery =(130, 15)
    DISPLAY.blit(scoretext, scoreRect)


#---------------TIMER

    time1text = font_choice.render('Time:', True, Yellow, None)
    time1Rect = time1text.get_rect()
    time1Rect.centerx, time1Rect.centery = (700, 15)
    DISPLAY.blit(time1text, time1Rect)
    scoretimer = scoretimer + .15    
##----------INTRO       
    while Startup == True:
        DISPLAY.fill(GRAY)

        text = font_choice.render("1 is start 1Player, SPACE for pause", True, Yellow, None)
        textRect = text.get_rect()
        textRect.centerx, textRect.centery = DISPLAY.get_rect().centerx, DISPLAY.get_rect().centery
        DISPLAY.blit(text, textRect)
        key = pygame.key.get_pressed()
        if key[pygame.K_1] == True:
            Startup = False
            youwin = False#reset all variables
            Lose = False
            level2 = False
            Greyback = True
            bgtimer = 0
            steppin = p1RightRight
            direction = p1Right
            steppinl = p1Left
            step = 24
            score = 0
            timer = 0
            dx = 60
            dy = 170
            drectx = 95
            drecty = 198
            w = 25
            h = 730
            face = p1Right
            keygot = j
            zrectx = 41
            zrecty = 41
            zrectx1 = 41
            zrecty1 = 45
            zrectx2 = 41
            zrecty2 = 45
            zrectx3 = 41
            zrecty3 = 45
            zrectx4 = 41
            zrecty4 = 45
            zrectx5 = 41
            zrecty5 = 45
            zrectx6 = 41
            zrecty6 = 45
            zomdir = 0
            zomdir1 = 0
            zomdir2 = 0
            zomdir3 = 0
            zomdir4 = 0
            zomdir5 = 0
            zomdir6 = 0
            lives = 3
            firex = 720
            firey = 570
            fdir = 1
            batx = 353
            baty = 500
            batdir = 0
            gx = 1200
            gy = 450
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    while Pause == True:
        DISPLAY.fill(GRAY)

        text = font_choice.render("Paused, press 0 to continue, m for restart menu.", True, Yellow, None)
        textRect = text.get_rect()
        textRect.centerx, textRect.centery = DISPLAY.get_rect().centerx, DISPLAY.get_rect().centery
        DISPLAY.blit(text, textRect)
        key = pygame.key.get_pressed()
        if key[pygame.K_0] == True:
            Pause = False
        if key[pygame.K_m] == True:
            Pause=False
            Startup=True
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    while youwin == True:#victory
        DISPLAY.fill(GREEN)
        text = font_choice.render("You Win! press R to restart", True, Yellow, None)
        textRect = text.get_rect()
        textRect.centerx, textRect.centery = DISPLAY.get_rect().centerx, DISPLAY.get_rect().centery
        DISPLAY.blit(text, textRect)
        key = pygame.key.get_pressed() # create an array that holds all the positions of the keys
        if key[pygame.K_r] == True:
            youwin = False#reset all variables
            Lose = False
            level2 = False
            Pause = False
            Startup = True
            steppin = p1RightRight
            direction = p1Right
            steppinl = p1Left
            Greyback = True
            bgtimer = 0
            step = 24
            score = 0
            timer = 0
            dx = 60
            dy = 170
            drectx = 95
            drecty = 198
            w = 25
            h = 730
            face = p1Right
            keygot = j
            zrectx = 41
            zrecty = 41
            zrectx1 = 41
            zrecty1 = 45
            zrectx2 = 41
            zrecty2 = 45
            zrectx3 = 41
            zrecty3 = 45
            zrectx4 = 41
            zrecty4 = 45
            zrectx5 = 41
            zrecty5 = 45
            zrectx6 = 41
            zrecty6 = 45
            zomdir = 0
            zomdir1 = 0
            zomdir2 = 0
            zomdir3 = 0
            zomdir4 = 0
            zomdir5 = 0
            zomdir6 = 0
            lives = 3
            firex = 720
            firey = 570
            fdir = 1
            batx = 353
            baty = 500
            batdir = 0
            gx = 1200
            gy = 450
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    while Lose == True:#failure
        DISPLAY.fill(RED)
        text = font_choice.render("Take the L, R to restart", True, Yellow, None)
        textRect = text.get_rect()
        textRect.centerx, textRect.centery = DISPLAY.get_rect().centerx, DISPLAY.get_rect().centery
        DISPLAY.blit(text, textRect)
        key = pygame.key.get_pressed() # create an array that holds all the positions of the keys
        if key[pygame.K_r] == True:
            Lose = False
            youwin = False
            level2 = False
            Pause = False
            Startup = True
            Greyback = True
            bgtimer = 0
            steppin = p1RightRight
            direction = p1Right
            steppinl = p1Left
            step = 24
            score = 0
            timer = 0
            dx = 60
            dy = 170
            drectx = 95
            drecty = 198
            w = 25
            h = 730
            face = p1Right
            side = 0
            keygot=j
            zrectx = 41
            zrecty = 41
            zrectx1 = 41
            zrecty1 = 45
            zrectx2 = 41
            zrecty2 = 45
            zrectx3 = 41
            zrecty3 = 45
            zrectx4 = 41
            zrecty4 = 45
            zrectx5 = 41
            zrecty5 = 45
            zrectx6 = 41
            zrecty6 = 45
            zomdir = 0
            zomdir1 = 0
            zomdir2 = 0
            zomdir3 = 0
            zomdir4 = 0
            zomdir5 = 0
            zomdir6 = 0
            lives = 3
            firex = 720
            firey = 570
            fdir = 1
            batx = 353
            baty = 500
            batdir = 0
            gx = 1200
            gy = 450
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

main()
    #THREE LIFE CLUB:
    #ZAK
