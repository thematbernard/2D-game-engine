from pygame.locals import * 
 
class CloseFrameViewer(): 
    def __init__(self): 
        self.types = ["event"] 
        self.entity_state = None 
        self.name = "quit_action" 
        self.children = None
    
    def condition_to_act(self, event): 
        if self.entity_state.active == False: 
            return False 
        if event.type == QUIT:
                return True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return True
        return False 
 
    def act(self, event): 
        import engine.play.entity.frameview as fV
        if self.condition_to_act(event): 
            self.entity_state.terminate()
        return

