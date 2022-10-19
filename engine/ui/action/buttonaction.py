from pygame.locals import *
import random

class ButtonPressAction: 
    def __init__(self): 
        self.types = ["event"] 
        self.entity_state = None 
        self.name = "button_press_action" 
        self.children = [] 
        self.verbose = False
 
    def condition_to_act(self, event): 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        if event.type == MOUSEBUTTONDOWN: 
            # check whether the mouse button is down inside the button area 
            pos = event.pos 
            return self.entity_state.is_inside(pos) 
        return False 
 
    def act(self, event): 
        if self.condition_to_act(event): 
            for c in self.children: 
                #print(event)
                c.act(self.name)
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return


