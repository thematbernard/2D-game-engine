from turtle import color
import pygame


class letter:
    def __init__(self, x, y, letter, name = "basic letter entity"):
        self.color = color
        self.actions = []
        self.location = [x, y]
        self.font_size = 20
        self.letter = letter
        self.color = (0, 255, 50)
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

    