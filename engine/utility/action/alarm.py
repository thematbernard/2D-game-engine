class Alarm:
    def __init__(self, allotted_time):
        self.types = ["loop"]
        self.allotted_time = allotted_time
        self.name = "alarm_action"
        self.verbose = False
        self.active = True
        self.children = []
        return

    def condition_to_act(self, event):
        #print(self.entity_state.current_time)
        self.change_allot_time()
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        if self.entity_state.current_time >= self.allotted_time:
            #print("alarm hit 2000 miliseconds")
            return True
        return False
    
    def act(self, event): 
        self.change_allot_time()
        if self.condition_to_act(event):
            for c in self.children:
                c.act(self.name)          

            if self.verbose: 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return

    def change_allot_time(self):
        if self.allotted_time >= 500:
            self.alloted_time = self.allotted_time = self.entity_state.allotted_time
        return