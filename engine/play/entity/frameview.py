import pygame
from pygame.locals import *

class FrameViewer():
    def __init__(self, x=1280, y=720, mode = RESIZABLE | DOUBLEBUF, depth = 12, title = "Whack-A-Box Game!", name= "Game Window"):
        pygame.init()
        self.screen = pygame.display.set_mode( (x, y), mode, depth )
        pygame.display.set_caption(title)
        self.dimensons = [x, y]
        self.tilte = title
        self.actions = []
        self.name = name
        self.mode = mode
        self.depth = depth
        self.verbose = False
        self.active = True
        self.children = []
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return

    def terminate(self):
        from sys import exit
        if self.verbose:
            print(self.name + " terminating")
        pygame.quit()
        exit()
        return

    def insert_entity(self, e):
        for a in e.actions:
            if "display" in a.types:
                self.children.append(a)
        return True

    def setTitle(self, title):
        self.title = title
        pygame.display.set_caption(title)
        if self.verbose:
            print(self.name + " title change to " + title)
        return
    
    def set_mode(self, sz, mode, depth):
        self.screen = pygame.display.set_mode( sz, mode, depth)
        self.dimensons = [sz[0], sz[1]]
        self.mode = mode
        self.depth = depth
        if self.verbose:
            print(self.name + " new size = " + str(self.dimensons))
        return





            
