class DeactivateEntityAction: 
    def __init__(self): 
        self.types = ["event"] 
        self.entity_state = None 
        self.name = "deactivate_action" 
        self.children = [] 
        self.verbose = False
 
    def condition_to_act(self, event): 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == True: 
            return True 
        return False
    
    def act(self, event): 
        self.entity_state.active = False
        return