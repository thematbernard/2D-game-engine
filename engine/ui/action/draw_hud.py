import pygame

class Draw_HUD:
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.children = []
        self.name = "Draw_hud_Action"
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
           self.draw_hud(data)

        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return

    def draw_hud(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 30)
        Hud = font.render(str(self.entity_state.string), True, self.entity_state.color)
        screen.blit(Hud, self.entity_state.location)
        return