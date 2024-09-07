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

    def walking(self, SCREEN):

        if wizard.walkingRIGHT and wizard.walkingLEFT:
            SCREEN.blit(IDLE[wizard.standing_ani // 8], (wizard.X_POS, wizard.Y_POS))
            wizard.standing_ani += 1

            wizard.walkingLEFT = False
            wizard.walkingRIGHT = False
            wizard.standing = True

        if wizard.steps + 1 >= 32:
            wizard.steps = 0

        if wizard.standing_ani + 1 >= 48:
            wizard.standing_ani = 0

        if wizard.jumping_ani + 1 >= 44:
            wizard.jumping_ani = 0



        if wizard.walkingRIGHT == True and not wizard.attacking_1 :

            SCREEN.blit(RIGHT[wizard.steps // 4], (wizard.X_POS, wizard.Y_POS))
            wizard.steps += 1

        if wizard.walkingLEFT == True and not wizard.attacking_1:

            SCREEN.blit(LEFT[wizard.steps // 4], (wizard.X_POS, wizard.Y_POS))
            wizard.steps += 1



            wizard.walkingLEFT = False
            wizard.walkingRIGHT = False
            wizard.standing = True


        if wizard.attacking_1_ani + 1 >= 35:
            wizard.attacking_1_ani = 0
            wizard.attacking_1 = False
            wizard.standing = False




        if wizard.attacking_1 == True:
            SCREEN.blit(ATTACK_1[wizard.attacking_1_ani // 5], (wizard.X_POS, wizard.Y_POS))
            wizard.attacking_1_ani += 1
            wizard.walkingLEFT = False
            wizard.walkingRIGHT = False
            wizard.standing = True



        elif not wizard.walkingLEFT and not wizard.walkingRIGHT and not wizard.attacking_1:
            SCREEN.blit(IDLE[wizard.standing_ani // 8], (wizard.X_POS, wizard.Y_POS))
            wizard.standing_ani += 1
            wizard.jumping_ani = 0








        '''elif wizard.jumping:

            SCREEN.blit(JUMPING[wizard.jumping_ani // 4], (wizard.X_POS, wizard.Y_POS))
            wizard.jumping_ani += 1'''





    def abbs(self):
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

ATTACK_1 = [pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_1.png"), (wizard.width, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_2.png"), (wizard.width, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_3.png"), (wizard.width, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_4.png"), (wizard.width, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_5.png"), (wizard.width, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_6.png"), (wizard.width, wizard.height)),
          pygame.transform.scale(pygame.image.load("assets/Wizard/attack1/a1_7.png"), (wizard.width, wizard.height))]



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

    if keys[pygame.K_a] and keys[pygame.K_d]:


        wizard.steps = 0
        wizard.standing = True
        wizard.walking(SCREEN)

    else:
        if keys[pygame.K_d] and wizard.X_POS < 1280 - wizard.width:
            wizard.X_POS += wizard.X_VEL

            wizard.walkingRIGHT = True
            wizard.walkingLEFT = False
            wizard.walking(SCREEN)

        if keys[pygame.K_a] and wizard.X_POS > 0:
            wizard.X_POS -= wizard.X_VEL
            wizard.walkingLEFT = True
            wizard.walkingRIGHT = False
            wizard.walking(SCREEN)





    if keys[pygame.K_e]:
        wizard.walkingRIGHT = False
        wizard.walkingLEFT = False
        wizard.attacking_1 = True
        wizard.abbs()



    if keys [pygame.K_SPACE]:
        wizard.jumping = True
        wizard.standing = False

    if wizard.jumping:
        wizard.Y_POS -= wizard.Y_VEL
        wizard.Y_VEL -= wizard.Y_GRAV
        if wizard.Y_VEL < -wizard.JUMP_HEIGHT:
            wizard.jumping = False
            wizard.Y_VEL = wizard.JUMP_HEIGHT






    else:

        wizard.steps = 0
        wizard.standing = True
        wizard.walking(SCREEN)


    wizard.X_POS += wizard.dx
    wizard.Y_POS += wizard.dy
























    pygame.display.update()
    CLOCK.tick(60)
