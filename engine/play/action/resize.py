from pygame.locals import *

class WindowResizeAction():
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.children = None
        self.name = "WindowResizeAction"
        self.verbose = False
        return

    def condition_to_act(self, event):
        if self.entity_state.active == False:
            return False
        if event.type == VIDEORESIZE:
            return True
        return False
    
    def act(self, event):
        if self.condition_to_act(event):
            self.entity_state.set_mode(event.size, self.entity_state.mode, self.entity_state.depth)
            if self.children != None:
                for c in self.children:
                    c.bounds = (0, 0, self.entity_state.dimensons[0], self.enetiy_state.dimensons[1])
        return