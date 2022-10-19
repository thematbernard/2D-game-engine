import pygame

class LoopAction():
    def __init__(self):
        self.types = ["loop"]
        self.entity_state = None
        self.children = []
        self.name = "looping action"
        self.verbose = False
        return

    def insert_action(self, a):
        if "loop" in a.types:
            self.children.append(a)

    def insert_entity(self, a):
        print(a.name)
        for a in a.types:
            if "loop" in a.types:
                self.children.append(a)
        return

    def condition_to_act(self, event):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True
    
    def act(self, event):
        if self.condition_to_act(event):
            self.entity_state.loop()
        return
