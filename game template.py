import time


import pygame
from pygame import *
import sys



pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("My Game")

class player(object):
    def __init__(self, X_POS, Y_POS, width, height):
        self.X_POS = X_POS
        self.Y_POS = Y_POS
        self.width = width
        self.height = height
        self.Y_GRAV = 0.5
        self.JUMP_HEIGHT = 10
        self.Y_VEL = self.JUMP_HEIGHT
        self.X_VEL = 4
        self.dx = 0
        self.dy = 0

        self.walkingLEFT = False
        self.walkingRIGHT = False
        self.jumping = False
        self.attacking_1 = False
        self.steps = 0
        self.standing = True
        self.standing_ani = 0
        self.jumping_ani = 0
        self.attacking_1_ani = 0
        self.facing = 1
        self.fired = False

    def walking_RIGHT(self, SCREEN):

        if self.X_POS < 1280 - self.width :
            self.X_POS += self.X_VEL




        if self.steps + 1 >= 32:
            self.steps = 0

        SCREEN.blit(RIGHT[self.steps // 4], (self.X_POS, self.Y_POS))
        self.steps += 1






    def walking_LEFT(self, SCREEN):

        if self.X_POS > 0 :
            self.X_POS -= self.X_VEL
            self.walkingLEFT = True
            self.standing = False


        if self.steps + 1 >= 32:
            self.steps = 0



        SCREEN.blit(LEFT[self.steps // 4], (self.X_POS, self.Y_POS))
        self.steps += 1









    def STANDING(self, SCREEN):
        if self.standing_ani + 1 >= 48:
            self.standing_ani = 0
            self.jumping = False




        SCREEN.blit(IDLE[self.standing_ani // 8], (self.X_POS, self.Y_POS))
        self.standing_ani += 1
        self.jumping_ani = 0











    def JUMPING(self):
        if self.jumping_ani + 1 >= 80:
            self.jumping_ani = 0

        self.Y_POS -= self.Y_VEL
        self.Y_VEL -= self.Y_GRAV
        if self.Y_VEL < -self.JUMP_HEIGHT:
            self.jumping = False
            self.Y_VEL = self.JUMP_HEIGHT

        if not self.walkingLEFT and not self.walkingRIGHT and not self.attacking_1:
            SCREEN.blit(IDLE[1], (self.X_POS, self.Y_POS))

















    def ATTACKING_1(self):


        if self.attacking_1_ani + 1 >= 35:
            self.attacking_1_ani = 0
            self.attacking_1 = False



        if self.facing == 1:
            SCREEN.blit(ATTACK_RIGHT[self.attacking_1_ani // 5], (self.X_POS, self.Y_POS))
            self.attacking_1_ani += 1




        if self.facing == -1:
            image = ATTACK_LEFT[self.attacking_1_ani // 5]
            SCREEN.blit(image, (self.X_POS + self.width - image.get_width(), self.Y_POS))
            self.attacking_1_ani += 1





class projectile(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 5 * self.facing
        self.shooting_anim = 0




    def shot(self, SCREEN):

        if self.shooting_anim  >= 45*3:
            self.shooting_anim = 0





        if self.facing == 1:
            SCREEN.blit(FIRE_BALL[self.shooting_anim //3], (self.x, self.y))
        else:
            SCREEN.blit(FIRE_BALL_LEFT[self.shooting_anim //3], (self.x, self.y))
        self.shooting_anim += 1
        self.x += self.vel

        if self.x < 0 or self.x > 1280:
            FIREBALLS.pop(FIREBALLS.index(self))


wizard = player(400, 453, 48, 64)
#fireball = projectile(wizard.X_POS+10, wizard.Y_POS+5, 64, 64)

FIREBALLS = []





'''X_POS, Y_POS = 400, 453


Y_GRAV = 1
JUMP_HEIGHT = 15
Y_VEL = JUMP_HEIGHT

X_VEL = 5

walkingLEFT = False
walkingRIGHT = False
jumping = False


steps = 0'''



BACKGROUND = pygame.transform.scale(pygame.image.load("assets/background3.png"), (1280, 720))

LEFT = [pygame.transform.scale(pygame.image.load("assets/Wizard/L 1.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/L 2.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/L 3.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/L 4.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/L 5.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/L 6.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/L 7.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/L 8.png"), (wizard.width, wizard.height))]

RIGHT = [pygame.transform.scale(pygame.image.load("assets/Wizard/R 1.png"), (wizard.width, wizard.height)),
         pygame.transform.scale(pygame.image.load("assets/Wizard/R 2.png"), (wizard.width, wizard.height)),
         pygame.transform.scale(pygame.image.load("assets/Wizard/R 3.png"), (wizard.width, wizard.height)),
         pygame.transform.scale(pygame.image.load("assets/Wizard/R 4.png"), (wizard.width, wizard.height)),
         pygame.transform.scale(pygame.image.load("assets/Wizard/R 5.png"), (wizard.width, wizard.height)),
         pygame.transform.scale(pygame.image.load("assets/Wizard/R 6.png"), (wizard.width, wizard.height)),
         pygame.transform.scale(pygame.image.load("assets/Wizard/R 7.png"), (wizard.width, wizard.height)),
         pygame.transform.scale(pygame.image.load("assets/Wizard/R 8.png"), (wizard.width, wizard.height))]

IDLE = [pygame.transform.scale(pygame.image.load("assets/Wizard/idle/i1.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/idle/i2.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/idle/i3.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/idle/i4.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/idle/i5.png"), (wizard.width, wizard.height)),
        pygame.transform.scale(pygame.image.load("assets/Wizard/idle/i6.png"), (wizard.width, wizard.height))]

JUMPING = [pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j1.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j2.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j3.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j4.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j5.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j6.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j7.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j8.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j9.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j10.png"), (wizard.width, wizard.height)),
           pygame.transform.scale(pygame.image.load("assets/Wizard/jump/j11.png"), (wizard.width, wizard.height))]

ATTACK_RIGHT = [pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_1.png"), (49, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_2.png"), (46, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_3.png"), (44, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_4.png"), (44, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_5.png"), (110, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_6.png"), (99, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_7.png"), (98, wizard.height))]


ATTACK_LEFT = [pygame.transform.flip(image, True, False) for image in ATTACK_RIGHT]



#fix the image shifting probelm
print("fix line 236!!!")
'''for image in ATTACK_LEFT:
    image = image.subsurface((image.get_width() - image.get_width(), 0), image.get_size())'''


ATTACK_1_testing = [pygame.image.load("assets/Wizard/attack1/a1_1.png"),
          pygame.image.load("assets/Wizard/attack1/a1_2.png"),
          pygame.image.load("assets/Wizard/attack1/a1_3.png"),
          pygame.image.load("assets/Wizard/attack1/a1_4.png"),
          pygame.image.load("assets/Wizard/attack1/a1_5.png"),
          pygame.image.load("assets/Wizard/attack1/a1_6.png"),
          pygame.image.load("assets/Wizard/attack1/a1_7.png")]

FIRE_BALL = []
for i in range(1, 46):
    image_path = f"assets/fireball/FireBallsprite_{i:02}.png"
    image = pygame.image.load(image_path)
    scaled_image = pygame.transform.scale(image, (64, 64))
    FIRE_BALL.append(scaled_image)

FIRE_BALL_LEFT = [pygame.transform.flip(img, True, False) for img in FIRE_BALL]








while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(BACKGROUND, (0, 0))




    for fireball in FIREBALLS[:]:

        #pygame.time.delay(100)
        #last = pygame.time.get_ticks()  # remove this if you want to try it working
        #now = pygame.time.get_ticks()  # remove this if you want to try it working


        #if now - last >= cooldown:  # remove this if you want to try it working




        fireball.shot(SCREEN)




    keys = pygame.key.get_pressed()

    #cooldown = 100  # remove this if you want to try it workin

    if keys[pygame.K_e]:

        wizard.attacking_1 = True
        wizard.standing = False

    if wizard.attacking_1_ani == 20:
        if wizard.facing == 1:
            FIREBALLS.append(projectile(wizard.X_POS + 80, wizard.Y_POS + 3, 64, 64, wizard.facing))
        else:
            FIREBALLS.append(projectile(wizard.X_POS - 64, wizard.Y_POS + 3, 64, 64, wizard.facing))


























    if keys[pygame.K_SPACE]:
        wizard.jumping = True


    if keys[pygame.K_a]:
        wizard.walkingLEFT = True
        wizard.standing = False
        wizard.facing = -1
    else:
        wizard.walkingLEFT = False


    if keys[pygame.K_d]:
        wizard.walkingRIGHT = True
        wizard.standing = False
        wizard.facing = 1
    else:
        wizard.walkingRIGHT = False


    if not (wizard.walkingLEFT or wizard.walkingRIGHT or wizard.jumping or wizard.attacking_1):
        wizard.standing = True
    else:
        wizard.standing = False



    if wizard.attacking_1:
        wizard.ATTACKING_1()

    if wizard.jumping:
        wizard.JUMPING()

    if wizard.walkingLEFT and not wizard.walkingRIGHT and not wizard.attacking_1:
        wizard.walking_LEFT(SCREEN)

    if wizard.walkingRIGHT and not wizard.walkingLEFT and not wizard.attacking_1:
        wizard.walking_RIGHT(SCREEN)

    if wizard.standing or (wizard.walkingLEFT and wizard.walkingRIGHT):
        wizard.STANDING(SCREEN)















    pygame.display.update()
    CLOCK.tick(60)
