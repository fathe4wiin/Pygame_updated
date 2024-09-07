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

    def walking_RIGHT(self, SCREEN):

        if wizard.X_POS < 1280 - wizard.width :
            wizard.X_POS += wizard.X_VEL




        if wizard.steps + 1 >= 32:
            wizard.steps = 0

        SCREEN.blit(RIGHT[wizard.steps // 4], (wizard.X_POS, wizard.Y_POS))
        wizard.steps += 1






    def walking_LEFT(self, SCREEN):

        if wizard.X_POS > 0 :
            wizard.X_POS -= wizard.X_VEL
            wizard.walkingLEFT = True
            wizard.standing = False


        if wizard.steps + 1 >= 32:
            wizard.steps = 0



        SCREEN.blit(LEFT[wizard.steps // 4], (wizard.X_POS, wizard.Y_POS))
        wizard.steps += 1









    def STANDING(self, SCREEN):
        if wizard.standing_ani + 1 >= 48:
            wizard.standing_ani = 0
            wizard.jumping = False




        SCREEN.blit(IDLE[wizard.standing_ani // 8], (wizard.X_POS, wizard.Y_POS))
        wizard.standing_ani += 1
        wizard.jumping_ani = 0











    def JUMPING(self):
        if wizard.jumping_ani + 1 >= 80:
            wizard.jumping_ani = 0

        wizard.Y_POS -= wizard.Y_VEL
        wizard.Y_VEL -= wizard.Y_GRAV
        if wizard.Y_VEL < -wizard.JUMP_HEIGHT:
            wizard.jumping = False
            wizard.Y_VEL = wizard.JUMP_HEIGHT

        if not wizard.walkingLEFT and not wizard.walkingRIGHT:
            SCREEN.blit(IDLE[1], (wizard.X_POS, wizard.Y_POS))

















    def ATTACKING_1(self):
        if wizard.attacking_1_ani + 1 >= 35:
            wizard.attacking_1_ani = 0
            wizard.attacking_1 = False


        SCREEN.blit(ATTACK_1[wizard.attacking_1_ani // 5], (wizard.X_POS, wizard.Y_POS))
        wizard.attacking_1_ani += 1


    def fireball(self):
        pass


















wizard = player(400, 453, 48, 64)






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

ATTACK_1 = [pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_1.png"), (49, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_2.png"), (46, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_3.png"), (44, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_4.png"), (44, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_5.png"), (110, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_6.png"), (99, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_7.png"), (98, wizard.height))]


ATTACK_1_testing = [pygame.image.load("assets/Wizard/attack1/a1_1.png"),
          pygame.image.load("assets/Wizard/attack1/a1_2.png"),
          pygame.image.load("assets/Wizard/attack1/a1_3.png"),
          pygame.image.load("assets/Wizard/attack1/a1_4.png"),
          pygame.image.load("assets/Wizard/attack1/a1_5.png"),
          pygame.image.load("assets/Wizard/attack1/a1_6.png"),
          pygame.image.load("assets/Wizard/attack1/a1_7.png")]

FIRE_BALL = [pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_01.png"), (32, 32)),
             pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_02.png"), (32, 32)),
             pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_03.png"), (32, 32)),
             pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_04.png"), (32, 32)),
             pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_05.png"), (32, 32)),
             pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_06.png"), (32, 32)),
             pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_07.png"), (32, 32)),
             pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_08.png"), (32, 32)),
             pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_09.png"), (32, 32)),
             pygame.transform.scale(pygame.image.load("assets/fireball/fireBallsprite_10.png"), (32, 32))]



#wizard_rect = IDLE.get_rect(center = (wizard.X_POS, wizard.Y_POS))



















'''
MARIO_STANDING = pygame.transform.scale(pygame.image.load("assets/me_mario.png"), (48, 64))
'''





while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(BACKGROUND, (0, 0))



    keys = pygame.key.get_pressed()

    if keys[pygame.K_e]:
        wizard.attacking_1 = True
        wizard.standing = False




    if keys[pygame.K_SPACE]:
        wizard.jumping = True


    if keys[pygame.K_a]:
        wizard.walkingLEFT = True
        wizard.standing = False
    else:
        wizard.walkingLEFT = False


    if keys[pygame.K_d]:
        wizard.walkingRIGHT = True
        wizard.standing = False
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
