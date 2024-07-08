from config import *

def tutorialScreen1():
    #print("in func")

    pygame.init()

    title_text = retro_font.render('Frogger', True, ORGANGE)
    tut_text1 = font3.render(
        'The only player control is the 4 direction joystick used to navigate the frog; each push in a direction', True,
        WHITE)
    tut_text2 = font3.render(
        'causes the frog to hop once in that direction. On the bottom half of the screen the player must', True, WHITE)
    tut_text3 = font3.render(
        "guide the frog between opposing lanes of trucks, cars, and other vehicles, to avoid becoming roadkill.", True,
        WHITE)

    Back_button = pygame.Rect(200, 600, BUTTON_WIDTH, BUTTON_HEIGHT)
    back_text = font2.render('Back', True, WHITE)

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
                # with open("titlescreen.py") as file:
                #     exec(file.read())
                return
            pygame.display.flip()