import random
from config import *
# from titlescreen import selectedChr
#from testing import *
# from titlescreen import fly, lizard
# from customizechara import fly, lizard
print("kailash100")

print("kailash10")
def Playgame():
    WHITE = (254, 250, 224)
    BLACK = (0 , 0 , 0)
    BLUE = (44, 140, 153)
    PURPLE = (199, 184, 234)
    PINK = (216, 167, 202)
    RED = (255,0,0)
    BLUEGREY = (55, 63, 81)
    BLUEPOP = (127, 126, 255)
    GREEN = (40, 54, 24)
    LIGHT = (96, 108,   56)
    ORGANGE = (221, 161, 94)
    DARKEROR = (188, 108, 37)
    print("kailash21")
    pygame.init()
    print("kailash22")
    #find water slash sound
    crash_sound = pygame.mixer.Sound("assets/sounds/crash_sound.mp3")
    music = pygame.mixer.Sound("assets/sounds/mainmusic.mp3")
    levelup = pygame.mixer.Sound("assets/sounds/level_up.mp3")

    print("kailash23")
    def willCarsClash(listOfCars, myCar, direction):
        print("kailash17")
        for car in listOfCars:
            #print(car.direction)
            if direction == "ltr":
                if car.y == myCar.y:
                    if car.x < 200:
                        return True
            else:
                # print("in if")
                if car.y == myCar.y:
                    if car.x > (Game.width -150):
                        return True

    def willLogsClash(listOfWood, myWood, direction):
        for wood in listOfWood:
            if direction == "ltr":
                if wood.y == myWood.y:
                    if wood.x < 200:
                        return True
            else:
                # print("in if")
                if wood.y == myWood.y:
                    if wood.x > (Game.width -150):
                        return True


    class Object:
        print("kailash25")
        def __init__(self):
            print("kailash26")
            self.direction = random.choice(["rtl", "ltr"])
            # self.direction = "ltr"
            self.speed = 5

        def show(self):
            if self.direction == 'ltr':
                Game.dsply.blit(self.image, (self.x, self.y))
            else:
                Game.dsply.blit(pygame.transform.flip(
                    self.image, True, False), (self.x, self.y))

        def move(self):
            if self.direction == 'ltr':
                self.x += self.speed
            else:
                self.x -= self.speed
        print("kailash27")

    class Coin():
        def __init__(self):
            self.coinpic = 'assets/img/coin.png'
            self.image = pygame.image.load(self.coinpic)
            self.x = random.choice([120, 170, 220, 270, 320, 370,420,470, 520,570])#random.randint(50,550)
            print(self.x)

            # self.y = 462.5
            self.y = random.choice([362.5, 412.5, 462.5, 512.5, 562.5, 612.5,662.5])
            print(self.y)
            self.coinpts = 0
            with open("high_score.txt") as file:
                data = file.read()
                myList = data.split(" ")
                self.coinpts = int(myList[1])
                print('here')
            print(self.x)

        def show(self):
            Game.dsply.blit(self.image, (self.x,self.y))

        def reset(self):
            self.x = random.choice([120, 170, 220, 270, 320, 370,420, 470, 520,570])
            print(self.x)

            # self.y = 462.5
            self.y = random.choice([362.5, 412.5, 462.5, 512.5, 562.5, 612.5, 662.5])

        def count(self):
            self.coinpts += 1

    class Wood(Object):
        def __init__(self):
            super().__init__()
            if self.direction == 'ltr':
                self.x = - 50
                self.y = random.choice([80, 180, 280])
            else:
                self.x = Game.width + 50
                self.y = random.choice([130, 230])
            self.image = pygame.image.load('assets/img/wood.png')


    class Car(Object):
        cars_pic = ['car1.png', 'car2.png', 'car3.png', 'car4.png']

        def __init__(self):
            super().__init__()
            if self.direction == 'ltr':
                self.x = - 50
                self.y = random.choice([400, 500, 600])
                #self.y = random.choice([400])
            else:
                self.x = Game.width + 50
                self.y = random.choice([450, 550])
                #self.y = 550
            self.selected_car = 'assets/img/' + random.choice(Car.cars_pic)
            self.image = pygame.image.load(self.selected_car)


    class Frog:
        def __init__(self,img_dir):
            self.x = Game.width / 2 - 50
            self.y = Game.height - 60
            self.image = pygame.image.load(img_dir)
            self.image_update = pygame.transform.scale(self.image, (65,47))
            self.speed = 50
            # self.area = Game.dsply.blit(self.image_update, (self.x, self.y))
            self.moving = ''

        def show(self):
            self.area = Game.dsply.blit(self.image_update, (self.x, self.y))

        def move(self):
            if self.moving == 'ltr':
                self.x += 5
            elif self.moving == 'rtl':
                self.x -= 5



    class Game:
        print("kailash3xx")
        coinpic = 'assets/img/coin.png'
        image = pygame.image.load(coinpic)
        x = 650
        y = 700
        width = 600
        level = 1
        height = 712
        dsply = pygame.display.set_mode((width, height))
        fps = 30
        frog_count = 5
        highscore = 0
        bg = pygame.image.load('assets/img/top-view-of-the-city-with-a-desert-vector-22982786.jpg')
        clock = pygame.time.Clock()
        font = pygame.font.Font('assets/font/atari_full.ttf', 32)
        font2 = pygame.font.Font('assets/font/atari_full.ttf', 18)
        font3_path = r"C:\Users\sharv\Downloads\Gamer.ttf"
        font3 = pygame.font.Font(font3_path, 50)
        with open("high_score.txt") as file:
            data = file.read()
            myList = data.split(" ")
            highscore = myList[0]

            is_gameOver = False
        # destenations = [[20, 50], [140, 170], [260, 290], [380, 410], [500, 530]]
        #print("kailashv7")
        @staticmethod
        def play():
            print("kailash19")
            Game.is_gameOver = False
            # if fly:
            #frog = Frog("assets/img/fly.png")
            # elif lizard:
            with open("char.txt") as file:
                data = file.read()
            if not data:
                frog = Frog("assets/img/frog.png")
            else:
                frog = Frog(f"assets/img/{data}.png")
            global coin
            coin = Coin()

            cars = []
            woods = []
            pygame.mixer.Sound.play(music, loops=-1)

            Game.dsply.blit(Game.image, (Game.x, Game.y))
            while True:
                # self.dsply.blit(Game.image, (Game.x, Game.y))
                if Game.level > int(Game.highscore):
                    Game.highscore = Game.level
                    with open("high_score.txt", mode="w") as file:
                        file.write(f"{Game.highscore} ")
                        file.write(f"{coin.coinpts}")

                # Game.dsply.blit(Game.bg, (0, 0))  # Clear the screen
                scoretext = Game.font3.render(f'Level:{Game.level}', True, WHITE)
                scorerect = scoretext.get_rect()
                scorerect.center = (200, 20)

                highscoretext = Game.font3.render(f'High Score:{Game.highscore}', True, WHITE)
                highscorerect = highscoretext.get_rect()
                highscorerect.center = (Game.width / 2 + 100, 20)

                coinstxt = Game.font3.render(f':{coin.coinpts}', True, WHITE)
                coinstxtrect = coinstxt.get_rect()
                coinstxtrect.center = (550, 660)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            frog.x -= 50
                        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            frog.x += 50
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                            frog.y -= 50
                            if frog.y == 302:
                                frog.y -= 20
                        # elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        #     frog.y += 50
                            if frog.y == 332:
                                frog.y += 20
                        frog.moving = ''

                # print(Game.level)
                if random.random() < (Game.level * 0.05):
                    if len(cars) == 0:
                        cars.append(Car())
                    myNewCar = Car()
                    # print(myNewCar.direction)
                    if not willCarsClash(cars,myNewCar, direction = myNewCar.direction):
                        cars.append(myNewCar)

                coinpic = 'assets/img/coin.png'
                image = pygame.image.load(coinpic)

                if random.random() < 0.1:
                    if len(woods) == 0:
                        woods.append(Wood())
                    MyWood = Wood()
                    if not willLogsClash(woods, MyWood, direction = MyWood.direction):
                        woods.append(MyWood)

                for car in cars:
                    car.move()

                for wood in woods:
                    wood.move()

                Game.dsply.blit(Game.bg, (0, 0))
                coin.show()
                for car in cars:
                    car.show()

                for wood in woods:
                    wood.show()



                frog.show()

                if frog.area.colliderect(pygame.Rect(coin.x, coin.y, 25, 25)):
                    coin.reset()
                    coin.count()
                    with open("high_score.txt", mode = "w") as file:
                        file.write(f"{Game.highscore} ")
                        file.write(f"{coin.coinpts}")
                if frog.y > 400:
                    for car in cars:
                        if frog.area.colliderect(pygame.Rect(car.x, car.y, 100, 51)):
                            # print(car.y)
                            pygame.mixer.pause()
                            pygame.mixer.Sound.play(crash_sound)
                            pygame.mixer.music.stop()

                            Game.is_gameOver = True

                elif frog.y < 300 and frog.y > 80:
                    if len(woods) >= 1:
                        for wood in woods:
                            if frog.area.colliderect(pygame.Rect(wood.x, wood.y, 201, 51)):
                                #print("in if hello")
                                frog.moving = wood.direction
                                frog.move()

                        if not any(frog.area.colliderect(pygame.Rect(wood.x, wood.y, 201, 51)) for wood in woods):
                            # print("wood")
                            pygame.mixer.pause()
                            pygame.mixer.Sound.play(crash_sound)
                            pygame.mixer.music.stop()
                            Game.is_gameOver = True



                    # print(Game.level)

                elif frog.y < 80:
                    pygame.mixer.Sound.set_volume(music, 0.2)
                    pygame.mixer.Sound.play(levelup)
                    frog.y = (Game.height - 60)
                    frog.x = Game.width /2 -50
                    Game.level += 1
                    pygame.mixer.Sound.set_volume(music, 0.8)

                back_text = Game.font2.render('Back', True, WHITE)
                back_button = pygame.Rect(10, 10, 100, 50)
                pygame.draw.rect(screen, BLUE, back_button)
                screen.blit(back_text, (back_button.x + (back_button.width - back_text.get_width()) / 2,
                                        back_button.y + (back_button.height - back_text.get_height()) / 2))

                if back_button.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.pause()
                    # with open("titlescreen.py") as file:
                    #     print("kailash8")
                    #     exec(file.read())
                    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
                    return
                Game.dsply.blit(scoretext, scorerect)
                Game.dsply.blit(highscoretext, highscorerect)
                Game.dsply.blit(image, (500, 650))
                Game.dsply.blit(coinstxt, coinstxtrect)
                if Game.is_gameOver:
                    if Game.is_gameOver:
                        # print("in if")
                        Game.level = 1
                        text1 = Game.font.render('Game Over!', True, RED)
                        text2 = Game.font2.render('press any key  to continue', True, RED)




                    textRect1 = text1.get_rect()
                    textRect1.center = (Game.width / 2, Game.height / 2)
                    textRect2 = text2.get_rect()
                    textRect2.center = (Game.width / 2, Game.height / 2 + 50)


                    while True:
                        Game.dsply.blit(text1, textRect1)
                        Game.dsply.blit(text2, textRect2)


                        frog.show()
                        pygame.display.update()
                        Game.clock.tick(Game.fps)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                            elif event.type == pygame.KEYDOWN:
                                print("kailash16")
                                Game.play()

                        if back_button.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                            # print("in if 1")
                            pygame.mixer.pause()
                            with open("titlescreen.py") as file:
                                print("kailash9")
                                exec(file.read())

                pygame.display.update()
                Game.clock.tick(30)
                print("kailash28a")
        print("kailash28b")
    print("kailash28c")
    pygame.display.set_caption('Frogger')
    # print("kailash5")
    Game.play()
    if __name__ == "__main__":
        print("kailash4")
        # pygame.display.set_caption('Frogger')
        # print("kailash5")
        # Game.play()