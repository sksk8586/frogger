#from titlescreen import *
from config import *
import pygame
#from testing import *

def getSelectCharacter():
    pygame.init()
    selectedCharacter = ""
    # initialize screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # first paint screen blue
    screen.fill(BLUE)

    # display coin image
    coin_image = pygame.transform.scale(COIN_IMG, (25, 25))
    screen.blit(coin_image, (495, 25))

    # display number of coins
    with open("high_score.txt") as file:
        print("kailash31")
        data = file.read()
        myList = data.split(" ")
        coinpts = int(myList[1])
    numOfCoins = font3.render(f':{coinpts}', True, WHITE)
    screen.blit(numOfCoins, (525, 25))

    # display text CUSTOM CHAR.
    char_text = font3.render("CUSTOM CHAR.", True, WHITE)
    screen.blit(char_text, (400, 100))

    print("kailash2")
    print(pygame.mouse.get_pos())

    # setting up fly image and displaying details
    fly_image = pygame.transform.scale(FLY_IMG, (50, 50))
    screen.blit(fly_image, (100, 100))
    selectbuttonfly = pygame.Rect(100, 175, 50, 20)
    pygame.draw.rect(screen, PINK, selectbuttonfly)

    # setting up lizard image and displaying details
    LIZARD = pygame.image.load('assets/img/lizard.png')
    lizard_img = pygame.transform.scale(LIZARD, (50, 50))
    screen.blit(lizard_img, (200, 100))
    select_button_lizard = pygame.Rect(200, 175, 50, 20)
    pygame.draw.rect(screen, PINK, select_button_lizard)

    #set up selected text
    selected_txt = font3.render(("CHARACTER SELECTED"), True, WHITE)

    #set up error text
    error_txt = font3.render(("Sorry, you don't have enough coins, try another character"), True, WHITE)

    #setup back button
    Back_button = pygame.Rect(200, 600, BUTTON_WIDTH, BUTTON_HEIGHT)
    back_text = font2.render('Back', True, WHITE)
    pygame.draw.rect(screen, PURPLE, Back_button)
    screen.blit(back_text, (Back_button.x + (Back_button.width - back_text.get_width()) / 2,
                            Back_button.y + (Back_button.height - back_text.get_height()) / 2))

    # def Writetofile():
    #     with open("char.txt", mode="w") as file:
    #         file.write(f"{selectedCharacter} ")
    while True:
        for event in pygame.event.get():
            global game_state

            #user selects fly
            if selectbuttonfly.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                if (coinpts >= NUMBER_OF_COINS_FOR_FLY):
                    screen.blit(selected_txt, (400, 200))
                    selectedCharacter = "fly"
                else:
                    screen.blit(error_txt, (400, 200))

            if select_button_lizard.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                if (coinpts >= NUMBER_OF_COINS_FOR_LIZARD):
                    screen.blit(selected_txt, (400, 200))
                    selectedCharacter = "lizard"
                else:
                    screen.blit(error_txt, (400, 200))

            if Back_button.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                print("inside collide")
                game_state = "title_screen"
                return selectedCharacter
            pygame.display.flip()






