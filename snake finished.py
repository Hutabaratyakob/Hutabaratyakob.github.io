'''
Jacob Hutabarat & Delanie Howes - Snake Game MyVersion 2018.
This game makes use to the PyGame package in Python and uses the Arrow keys to control the snake.
This version of the snake game was modified from the tutorial posted by Syntec (on behalf of TheNewBoston.com)
All modifications and changes we made are commented in-line under the lable title *CHANGE* .
'''




import pygame
import time
import random

pygame.init()

white = (255,255,255)#color definitions
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800 #size of the window
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

icon = pygame.image.load('apple2.png')#images for the game
pygame.display.set_icon(icon)

img = pygame.image.load('snakehead2.png')
appleimg = pygame.image.load('apple2.png')

clock = pygame.time.Clock() #counting

AppleThickness = 30
block_size = 20
FPS = 60 #frames per second; critically affects speed; *CHANGED* to 60 to make game smoother


direction = "right"

#adds text font for title and messagse
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def pause(): #creates the ablitiy to pause the entire program whilst also adding a pause frame

    paused = True
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")

    message_to_screen("Press C to continue or Q to quit.",
                      black,
                      25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)
        
        clock.tick(5)
                    

def score(score): # places score on the screen
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def randAppleGen(): #generates apple position
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0

    return randAppleX,randAppleY



def game_intro(): #main menu

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
   
        gameDisplay.fill(white) #*CHANGE* title and directions have been modifed
        message_to_screen("Slither REMIX",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30)

        message_to_screen("The more apples you eat, the longer you get",
                          black,
                          10)

        message_to_screen("If you run into yourself, or the edges, you die!",
                          black,
                          50)
        message_to_screen("You can adjust the difficulty: easy/medium/hard = T/Y/U",
                          black,
                          90)

        message_to_screen("Press T/Y/U to play, P to pause or Q to quit.",
                          black,
                          180)
    
        pygame.display.update()
        clock.tick(15)
        
        


def snake(block_size, snakelist): # visual asthetic that signifies the snake is turning

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False
   
    
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = block_size * speedreducer #change in x; affects speed of snakehead
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()
    
    while not gameExit:

        if gameOver == True:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()
            

        while gameOver == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                                                    #*CHANGED* added difficutly keybindings
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        '''
                    if event.key == pygame.K_t:
                        speedreducer = 0.25
                        gameLoop()

                    if event.key == pygame.K_y:
                        speedreducer = 0.20
                        gameLoop()

                    if event.key == pygame.K_u:
                        speedreducer = 0.15
                        gameLoop()
'''
        
        for event in pygame.event.get(): #speed control and key bindings
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size * speedreducer
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size * speedreducer
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size * speedreducer
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size * speedreducer
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0: #sets window boundaries
            gameOver = True
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)

        
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        snake(block_size, snakeList)

        score(snakeLength-1)

        
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            
            

        
            
        
        

        clock.tick(FPS)
        
    pygame.quit()
    quit()

game_intro()
gameLoop()
