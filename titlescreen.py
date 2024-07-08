import pygame
import random
# from testing import *
from tutorialScreen import tutorialScreen1
from config import *
from customizechara import getSelectCharacter
from v7 import Playgame
selectedChr = ""
print("kailash71")
pygame.init()

car_list = []

# Set up the buttons
how_to_play_button = pygame.Rect(75, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
play_game_button = pygame.Rect(184, 575, BUTTON_WIDTH, BUTTON_HEIGHT)
customize_character_button = pygame.Rect(300, 500, BUTTON_WIDTH, BUTTON_HEIGHT)


# Set up the button text
how_to_play_text = font2.render('How to Play', True, WHITE)

play_game_text = font2.render('Play Game', True, WHITE)
customize_character_text = font2.render('Customize Character', True, WHITE)
print ("kailash300")

# with open("high_score.txt") as file:
#     print("kailash31")
#     data = file.read()
#     myList = data.split(" ")
#     coinpts = int(myList[1])

# Set up the title text
title_text = retro_font.render('Frogger', True, ORGANGE)
tut_text1 = font3.render('The only player control is the 4 direction joystick used to navigate the frog; each push in a direction' , True, WHITE)
tut_text2 = font3.render('causes the frog to hop once in that direction. On the bottom half of the screen the player must', True, WHITE)
tut_text3 = font3.render("guide the frog between opposing lanes of trucks, cars, and other vehicles, to avoid becoming roadkill.", True, WHITE)
#char_text = font3.render("CUSTOM CHAR.", True, WHITE)
#coinstxt = font3.render(f':{coinpts}', True, WHITE)
# fly = False
game_state = 'title_screen'



# Fill the screen with white
screen.fill(WHITE)
screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, HEIGHT / 4))

# Draw the buttons
pygame.draw.rect(screen, GREEN, how_to_play_button)
pygame.draw.rect(screen, GREEN, play_game_button)
pygame.draw.rect(screen, GREEN, customize_character_button)

# Draw the button text
screen.blit(how_to_play_text, (how_to_play_button.x + (how_to_play_button.width - how_to_play_text.get_width()) / 2,
                               how_to_play_button.y + (
                                       how_to_play_button.height - how_to_play_text.get_height()) / 2))
screen.blit(play_game_text, (play_game_button.x + (play_game_button.width - play_game_text.get_width()) / 2,
                             play_game_button.y + (play_game_button.height - play_game_text.get_height()) / 2))
screen.blit(customize_character_text, (
    customize_character_button.x + (customize_character_button.width - customize_character_text.get_width()) / 2,
    customize_character_button.y + (customize_character_button.height - customize_character_text.get_height()) / 2))

#putting the image
icon_image = pygame.transform.scale(FROG_ICON, DEFAULT_IMAGE_SIZE)
frog_image= pygame.transform.scale(FROG_IMAGE, (300,300))
fly_image = pygame.transform.scale(FLY_IMG, (20,20))

screen.blit(icon_image, (0, 170))
screen.blit(frog_image, (115, 200))

# setup back button
Back_button = pygame.Rect(200, 600, BUTTON_WIDTH, BUTTON_HEIGHT)
back_text = font2.render('Back', True, WHITE)


def Writetofile():
    print("entered write to file")
    with open("char.txt", mode="w") as file:
        file.write(f"{selectedChr}")
    print("exit write to file")


def tutorialScreen():
    #print("in func")
    pygame.init()
    print("in howtoplay")
    global game_state
    screen.fill(PINK)
    screen.blit(tut_text1, (50,100))
    screen.blit(tut_text2, (50, 200))
    screen.blit(tut_text3, (50, 300))
    pygame.draw.rect(screen, BLUE, Back_button)
    screen.blit(back_text, (Back_button.x + (Back_button.width - back_text.get_width()) / 2,
                                   Back_button.y + (Back_button.height - back_text.get_height()) / 2))

    running = True
    while running:
        # Handle events
        print("inside while")
        for event in pygame.event.get():
            if Back_button.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                game_state = "title_screen"
                with open("titlescreen.py") as file:
                    exec(file.read())
            pygame.display.flip()


def move_listcar():
    for i in car_list:
        print(car_list)
        i.move()

# Set up the main game loop
running = True
while running:
    # Handle events
    print("inside while")
    for event in pygame.event.get():
        #print(f"eventtype = {event.type}")
        if event.type == pygame.QUIT:
            print("i am quitttting the gae")
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse button ddown")
            if game_state == "title_screen":
                if how_to_play_button.collidepoint(event.pos):
                    game_state = 'how_to_play'
                elif play_game_button.collidepoint(event.pos):
                    print("kailash14")
                    game_state = 'game'
                elif customize_character_button.collidepoint(event.pos):
                    print("kailash30")
                    game_state = 'customize_character'
            print(game_state)

    if game_state == "how_to_play":
        tutorialScreen1()
        with open("titlescreen.py") as file:
            exec(file.read())
    if game_state == "customize_character":
        # customizeChar()
        # with open("customizechara.py") as file:
        #     print("kailash1")
        #     exec(file.read())
        selectedChr = getSelectCharacter()
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        Writetofile()

        print("after getSelectedCharacter")
        with open("titlescreen.py") as file:
            exec(file.read())
    if game_state == "game":
        print("kailash15")
        Playgame()
        print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
        with open("titlescreen.py") as file:
            exec(file.read())
        # with open("v7.py") as file:
        #     exec(file.read())
        # PlayGame(selectedChr)
        # pygame.display.flip()
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()