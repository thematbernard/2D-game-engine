from turtle import color
import pygame

class circle:
    def __init__(self, x, y, width, radius, name = "circle"):
        self.color = color
        self.actions = []
        self.width = width
        self.center_point = [x, y]
        self.radius = radius
        self.color = (0, 0, 255)
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