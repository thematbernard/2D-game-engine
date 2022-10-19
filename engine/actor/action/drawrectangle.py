import pygame
import engine.actor.entity.rectangle as rectangle
import engine.play.entity.gameloop as gameLoop

class Draw_Rectangle:
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.children = []
        self.name = "Draw Rectangle Action"
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
           self.draw_rect(data)
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return

    def draw_rect(self, screen):
        pygame.draw.rect(screen, self.entity_state.color, self.entity_state.dimensions)
        return
        
    
        

