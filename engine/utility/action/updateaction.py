class UpdateAction: 
    def __init__(self): 
        self.types = ["loop"] 
        self.entity_state = None 
        self.name = "update_action" 
        self.children = [] 
        self.verbose = False
 
    def act(self, event): 
        self.entity_state.current_time = self.entity_state.tick()
        return True
