
import pygame

print("kailash11")
# Define other colors...

pygame.init()

WIDTH, HEIGHT = 600, 712
TITLE_FONT_SIZE = 48
BUTTON_FONT_SIZE = 20
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
FROG_ICON = pygame.image.load('assets/img/tropical-frop.png')
DEFAULT_IMAGE_SIZE = (80, 80)
NUMBER_OF_COINS_FOR_FLY = 10
NUMBER_OF_COINS_FOR_LIZARD = 20

WHITE = (254, 250, 224)
BLACK = (0,0,0)
BLUE = (44, 140, 153)
PURPLE = (199, 184, 234)
PINK = (216, 167, 202)
RED = (180, 101, 111)
BLUEGREY = (55, 63, 81)
BLUEPOP = (127, 126, 255)
GREEN = (40, 54, 24)
LIGHT = (96, 108,   56)
ORGANGE = (221, 161, 94)
DARKEROR = (188, 108, 37)
# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frogger')

game_state = 'title_screen'

y_car = 50
print("kailash12")

FROG_IMAGE = pygame.image.load('assets/img/frog1.png')
FLY_IMG = pygame.image.load('assets/img/fly.png')
COIN_IMG = pygame.image.load("assets/img/coin.png")

# Set up the fonts
title_font = pygame.font.SysFont('custom_font', TITLE_FONT_SIZE)
retro_path = r"C:\Users\sharv\Downloads\RETROTECH.ttf"
retro_font = pygame.font.Font(retro_path, 100)
font2_path =  r"C:\Users\sharv\Downloads\game_over.ttf"
font2 = pygame.font.Font(font2_path, 50)
font3_path =  r"C:\Users\sharv\Downloads\Gameplay.ttf"
font3 = pygame.font.Font(font3_path, 20)
font4_path =  r"C:\Users\sharv\Downloads\Gamer.ttf"
font4 = pygame.font.Font(font4_path, 100)
norm_path = r"C:\Users\sharv\Downloads\Kid Games.ttf"
norm_path_font = pygame.font.Font(norm_path, 100)


