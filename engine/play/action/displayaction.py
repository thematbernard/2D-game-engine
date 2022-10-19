import pygame

class DisplayAction():
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.children = []
        self.name = "Display Screen Action"
        self.verbose = False
        return

    def insert_action(self, a):
        if "display" in a.types:
            self.children.append(a)

    def insert_entity(self, e):
        for a in e.actions:
            if "display" in a.types:
                self.children.append(a)
        return

    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True
    
    def act(self, data):
        if self.condition_to_act(data):
            self.entity_state.screen.fill((0, 0, 0))
            for t in self.children:
                t.act(self.entity_state.screen)
            pygame.display.flip()
        return

