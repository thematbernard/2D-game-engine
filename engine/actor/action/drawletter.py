import pygame
import engine.actor.entity.letter as letter
import engine.play.entity.gameloop as gameLoop

class Draw_Letter:
    def __init__(self):

        self.types = ["display"]
        self.entity_state = None
        self.children = []
        self.name = "Draw Letter Action"
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
           self.draw_letter(data)
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return

    def draw_letter(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 40)
        drawnLetter = font.render(str(self.entity_state.letter), True, self.entity_state.color)
        screen.blit(drawnLetter, self.entity_state.location)
        return