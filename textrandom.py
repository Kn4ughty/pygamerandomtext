# This program was created by Knaughty.
# It creates a window on screen with rapidly changing text, using a font specifed on line 23
# To run you will need python 3.1 and the pygame module (random module is default)
# To install pygame open a terminal and type "pip3 install pygame"
# Then to run open with python IDLE or something. I personally use sublime text so do whatever

# import pygame module in this program
import pygame
import random 

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

#Change "FPS" to change update speed
FPS = 15
length = 30

# create a font object.
# 1st parameter is the font file 2nd parameter is size of the font
font = pygame.font.Font('JetBrains Mono Regular Nerd Font Complete Mono.ttf', 32)

# define the RGB value for white, green, blue colour .
#you can invert the colours by renaming the variables.
white = (255, 255, 255)
black = (0, 0, 0)

# Sets window width and height. "S" stands for screen
SWidth = 800
SHeight = 100

# set the pygame window name
pygame.display.set_caption('RandomTextGen')

fpsClock = pygame.time.Clock()


# The letters avialble to be picked when randomising. Other examples commented out. 
# The random looking one (or boxes if you dont have the font) is for the "NotoSansBuginese-Regular.ttf" font.
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+~`1234567890-=[]{|;:,./<>?'
#letters = 'ABCDEFGHIJKLMNOPQRSTUVWXY/[]+'
#letters = 'ᨀᨁᨂᨃᨄᨅᨆᨇᨈᨉᨊᨋᨌᨍᨎᨏᨐᨑᨒᨓᨔᨕᨖ'

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((SWidth, SHeight), 0, 32)

# x has to be defined or else it complains
x = "a"
# create a text surface object,
# on which text is drawn on it.
text = font.render(x, True, black, black)
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object. (takes screen width and height and divides it by two)
textRect.center = (SWidth // 2 - length * 10, SHeight // 2)
 
# infinite loop
while True:
    # completely fill the surface object
    # with white color
    display_surface.fill(black)

    # Gets random letters.
    word = ' '
    for i in range(length):
        x = random.choice(letters)
        word = word + x

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    
    text = font.render(word, True, white, black)
    display_surface.blit(text, textRect)
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    # allows the program to be closed without a task manager.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    fpsClock.tick(FPS)
    # prints are for debugging.
    #print(fpsClock)
    #print(word)
    pygame.display.update()