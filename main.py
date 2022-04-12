import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))

RED = (250,0,0)
BLUE = (0, 0, 250)
GREEN = (5, 156, 52)
YELLOW = (250, 250, 0)
WHITE = (250, 250, 250)
SKY = (145, 229, 255)
BLACK = (0,0,0)
pygame.draw.rect(screen,(SKY), (0,0,800,800))

class cloud:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        pygame.draw.circle(screen, (WHITE), (self.xpos, self.ypos), 50)
        pygame.draw.circle(screen, (WHITE), (self.xpos+35, self.ypos+10), 37)
        pygame.draw.circle(screen, (WHITE), (self.xpos-35, self.ypos+10), 37)
        
        pygame.draw.arc(screen, (BLUE), (self.xpos-37, self.ypos-75, 75, 75), 7*3.14/4, 5*3.14/4, 5)
        pygame.draw.arc(screen, (GREEN), (self.xpos-41, self.ypos-90, 85, 85), 7*3.14/4, 5*3.14/4, 5)
        pygame.draw.arc(screen, (YELLOW), (self.xpos-45, self.ypos-105, 95, 95), 7*3.14/4, 5*3.14/4, 5)
        pygame.draw.arc(screen, (RED), (self.xpos-49, self.ypos-120, 105, 105), 7*3.14/4, 5*3.14/4, 5)
        
class bird:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.arc(screen, (BLACK), (self.xpos, self.ypos, 15,15), 0, 3.14, 3)
        pygame.draw.arc(screen, (BLACK), (self.xpos+15, self.ypos, 15,15), 0, 3.14, 3)

        
cloud1 = cloud(400,400)
cloud2 = cloud(200,200)
cloud3 = cloud(575,525)
cloud4 = cloud(700, 200)
cloud5 = cloud(175, 600)

bird1 = bird(300, 200)
bird2 = bird(310, 215)
bird3 = bird(315, 185)
bird4 = bird(700, 500)
bird5 = bird(710, 515)
bird6 = bird(715, 485)

cloud1.draw()
cloud2.draw()
cloud3.draw()
cloud4.draw()
cloud5.draw()

bird1.draw()
bird2.draw()
bird3.draw()
bird4.draw()
bird5.draw()
bird6.draw()
pygame.display.flip()
    
#pygame.quit()
