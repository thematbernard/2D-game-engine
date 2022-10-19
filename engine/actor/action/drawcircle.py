import pygame
import engine.actor.entity.circle as circle
import engine.play.entity.gameloop as gameLoop

class Draw_Circle:
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.children = []
        self.name = "Draw Circle Action"
        self.verbose = False
        return

    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
           self.draw_circ(data)
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return

    def draw_circ(self, screen):
        pygame.draw.circle(screen, self.entity_state.color, self.entity_state.center_point, self.entity_state.radius)
        return