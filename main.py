
// Save this MINI_GAME File in Local C: drive

import pygame
import random
import math
import time  
from pygame import mixer
clock = pygame.time.Clock()
mixer.init()
pygame.init()

mixer.music.load('C:\Mini_game\Green_bg.jpgBrave Pilots (Menu Screen).ogg')

mixer.music.play(-1)
screen =pygame.display.set_mode((820,600));
running=True
pygame.display.set_caption('space SHooter Game')
icon = pygame.image.load('C:\Mini_game\Green_bg.jpgspaceship.png')
pygame.display.set_icon(icon)


background2 = pygame.image.load('C:\Mini_game\Green_bg.jpgPurple.jpg')
# C:\Mini_game\Green_bg.jpgBackground2.png

background1 = pygame.image.load('C:\Mini_game\Green_bg.jpgOrange.jpg')
background3 = pygame.image.load('C:\Mini_game\Green_bg.jpgGreen_bg.jpg')
background0 = pygame.image.load('C:\Mini_game\Green_bg.jpgBlue.jpg')





alienimg =  pygame.image.load('C:\Mini_game\Green_bg.jpgAlien.png')    
alienimg1 =  pygame.image.load('C:\Mini_game\Green_bg.jpgAlien.png')    
alienimg2 =  pygame.image.load('C:\Mini_game\Green_bg.jpgAlien.png')    
alienimg3 =  pygame.image.load('C:\Mini_game\Green_bg.jpgAlien.png')    


bulletimg =  pygame.image.load('C:\Mini_game\Green_bg.jpgBullet.png')


 
battery0_img = pygame.image.load('C:\Mini_game\Green_bg.jpgBattery_0.png')
battery1_img = pygame.image.load('C:\Mini_game\Green_bg.jpgBattery_1.png')
battery2_img = pygame.image.load('C:\Mini_game\Green_bg.jpgBattery_2.png')
battery3_img = pygame.image.load('C:\Mini_game\Green_bg.jpgBattery_3.png')
Blaster_img = pygame.image.load('C:\Mini_game\Green_bg.jpgBoom.png')

live_img = pygame.image.load('C:\Mini_game\Green_bg.jpgicons8-life-48.png')
heart=5


alienimg =[]
alienimg1 =[]
alienimg2 =[]
alienimg3 =[]
alienX=[]
alienY=[]
alienspeedX=[]
alienspeedY=[]

no_of_aliens=6

for i in range(no_of_aliens):
    alienimg.append(pygame.image.load('C:\Mini_game\Green_bg.jpgAlien4.png'))
    alienimg1.append(pygame.image.load('C:\Mini_game\Green_bg.jpgAlien3.png'))
    alienimg2.append(pygame.image.load('C:\Mini_game\Green_bg.jpgAlien2.png'))
    alienX.append(random.randint(0,736))
    alienY.append(random.randint(30,150))
    alienspeedX.append(0.1)
    alienspeedY.append(50)

for i in range(no_of_aliens):
    if(i==0 or i==1):
        alienimg3.append(pygame.image.load('C:\Mini_game\Green_bg.jpgAlien3.png'))
    elif(i==2 or i==3):
         alienimg3.append(pygame.image.load('C:\Mini_game\Green_bg.jpgAlien2.png'))
    elif(i==4):
         alienimg3.append(pygame.image.load('C:\Mini_game\Green_bg.jpgAlien4.png'))
    else:
         alienimg3.append(pygame.image.load('C:\Mini_game\Green_bg.jpgAlien.png'))
    
 

check =False
spaceshipX = 370;
spaceshipY = 480;
ChangeX=0
ChangeY=0
bulletX = 386  
bulletY= 448

score =0
k=0
b=False
font_score = pygame.font.SysFont('Verdana' , 32 , 'bold')

font_over = pygame.font.SysFont('Verdana' , 512 , 'bold')
font_shift = pygame.font.SysFont('Verdana' , 16 , 'bold')
font_level = pygame.font.SysFont('Verdana' , 48 , 'bold')
font_heart = pygame.font.SysFont('Verdana' , 64 , 'Bold')
level=0


    
    

def Gameover():
    mixer.music.load('C:\Mini_game\Green_bg.jpgmixkit-arcade-fast-game-over-233.wav')
    mixer.music.play()
    img_over = font_score.render('GAME OVER',True,'white')
    screen.blit(img_over,(300 , 250)) 
    pygame.time.delay(3000) 
def live():
    x= 600
    y=500
    for s in range(heart):
        screen.blit(live_img , (x+(s*40), y))

    
heart_text = font_heart.render(f'Lives : {heart}', True , (79, 192, 141))


def score_text():
    
    
    if(level==1):
         level_text = font_level.render(f'Level : {level+1}',True,( 0, 0, 0))
         img = font_score.render(f'Score : {score} ',True,(0 ,0, 0))
    else:
        level_text = font_level.render(f'Level : {level+1}',True,(79, 192, 141))
        
        img = font_score.render(f'Score : {score} ',True,(79, 192, 141))
    screen.blit(level_text,(20,500))
    screen.blit(img,(10,10)) 

def shift_text():
   
    if(level==1):
        shift_img = font_shift.render(f'Press Shift + Enter',True,(40, 40, 43))
    elif(level==2):
        shift_img = font_shift.render(f'Press Shift + Enter',True,(255, 229, 180))
    else:
        shift_img = font_shift.render(f'Press Shift + Enter',True,'white')
    
    screen.blit(shift_img,(650,65))


def player():
    if(level==0):
        spaceshipimg =  pygame.image.load('C:\Mini_game\Green_bg.jpgspaceship1.png')
        screen.blit(spaceshipimg,(spaceshipX , spaceshipY))
    elif(level==1):
        spaceshipimg =  pygame.image.load('C:\Mini_game\Green_bg.jpgspaceship2.png')
        screen.blit(spaceshipimg,(spaceshipX , spaceshipY))
    else:
        spaceshipimg =  pygame.image.load('C:\Mini_game\Green_bg.jpgspaceship3.png')
        screen.blit(spaceshipimg,(spaceshipX , spaceshipY))
        
def bullet():
    screen.blit(bulletimg , (bulletX , bulletY))
    b=True
 

         


while running :
    
    
    if(level==0):
        screen.blit(background0 , (0,0))
        
    elif(level==1):
        screen.blit(background1 , (0,0))
    elif(level==2):
        screen.blit(background2 , (0,0))
    else:
        screen.blit(background3 , (0,0))
        
    live()     
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:  
            running=False
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                ChangeX-=0.5
            if event.key==pygame.K_RIGHT:
                ChangeX=0.5
            if event.key==pygame.K_UP:
                ChangeY-=0.5
            if event.key==pygame.K_DOWN:
                ChangeY=0.5
            if event.key==pygame.K_SPACE:
                if check is False:
                   check=True
                   bulletX=spaceshipX+16
                   bulletY=spaceshipY-32

        # if k > 10 and not shift_enter_rendered:
        #     shift_text()
        #     shift_enter_rendered = True
            
        if k>30:
            if keys[pygame.K_RSHIFT] and keys[pygame.K_RETURN]:
               k = 0
               level+=1
             
        
        
                     
                     

      

        if event.type==pygame.KEYUP:
            if event.key in[pygame.K_LEFT , pygame.K_RIGHT]:
              ChangeX=0 
            if event.key in[pygame.K_DOWN , pygame.K_UP]:
              ChangeY=0 
       

             
        
    spaceshipX+=ChangeX
    spaceshipY+=ChangeY

    if spaceshipX<=0 :
        spaceshipX=0
    elif spaceshipX>=800:
        spaceshipX=720
    
    if spaceshipY>=480:
        spaceshipY=480
    elif spaceshipY<=300:
        spaceshipY=300

    for i in range(no_of_aliens):
       if alienY[i]>420 : 
        heart-=1;
        if heart==0:
            for j in range(no_of_aliens):
                 # GAme Over
                alienY[j]=2000
            Gameover()
            pygame.time.delay(5000)
            running=False
        else: 
            screen.blit(heart_text,(400,250))
            pygame.time.delay(1000) 
            for j in range(no_of_aliens):
                alienX[j] = random.randint(0,736)
                alienY[j] = random.randint(30,150)
            continue;   
       alienX[i]+=alienspeedX[i]
       if alienX[i]<=0:
            alienspeedX[i]=1
            alienY[i]+=alienspeedY[i]
            
       if alienX[i]>=736:
            alienspeedX[i]=-1
            alienY[i]+=alienspeedY[i]
       distance = math.sqrt(math.pow(bulletX-alienX[i] , 2)+math.pow(bulletY-alienY[i] , 2))
       if distance< 27 :
           check=False
           alienX[i] = random.randint(100,300)
           alienY[i] = random.randint(30,150)
           if bulletY > 25 : 
             score+=1
             k+=1 # Activate the animation
           b=False
       if(level==0):
        screen.blit(alienimg[i],(alienX[i] , alienY[i]))
       elif(level==1):
        screen.blit(alienimg1[i],(alienX[i] , alienY[i]))
       elif(level==2):
        screen.blit(alienimg2[i],(alienX[i] , alienY[i]))
       elif(level==3):
        screen.blit(alienimg3[i],(alienX[i] , alienY[i]))
         


       
        
       if(k<=10):
           screen.blit(battery0_img , (750,5))
       
       elif(k<=20):
          screen.blit(battery1_img , (750,5))
       
       elif(k<=30):
          screen.blit(battery2_img , (750,5))
       else:
          screen.blit(battery3_img , (750,5))
          shift_text()

   
    player()
    
    if bulletY<=0:
        bulletY=448
        check=False
    if check:
       bullet()
       bulletY-=5

    score_text()
    pygame.display.update()
