import pygame

class rectangle:
    def __init__(self, x, y, width, height, name = "rectangle"):
        self.actions = []
        self.dimensions = [x, y, width, height]
        self.color = (255, 0, 0)
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return

    def setColor(self, color):
        self.color = color
        return
    



