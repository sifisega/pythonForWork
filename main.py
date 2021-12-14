import pygame
from pygame.locals import *

pygame.init()

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

Frames_Per_Second = pygame.time.Clock()
Vector = pygame.math.Vector2
Display_Surface = pygame.display.set_mode((WIDTH, HEIGHT))



class Segment(pygame.sprite.Sprite):
    '''
    A line drawn from two nodes
    node a is connected to the 'parent' while node b is for the 'child'
    '''
    def __init__(self, parent_node, vector):
        super().__init__()\
        self.node_a = Node(parent_node)
        self.vector = vector
        self.parent_node = parent_node

    def calc_node_b(self):
        dx = self.vector.length() + math.cos(vector())
        dy = self.vector.length() + math.sin(vector())


class Player(Segment):
    '''The player controlled segment'''
    def __init__(self):
        super().__init__()

    def move(self):
        self.position = pygame.mouse.get_pos()
        self.rect.center = self.position



class Node(pygame.sprite.Sprite):
    '''A single point on the 2d plane'''
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y



while True:
    for event in pygame.event.get():
        '''Checks all key_in events'''
        if event.type == QUIT:
            pygame.quit()

    Display_Surface.fill((0,0,0)) #resets surface


    pygame.display.update()
    Frames_Per_Second.tick(FPS)
