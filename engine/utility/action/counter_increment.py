class CounterIncrementAction: 
    def __init__(self): 
        self.types = ["event"] 
        self.entity_state = None 
        self.name = "counter_action" 
        self.children = [] 
        self.verbose = False
 
    def condition_to_act(self, event): 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        if event == "button_press_action": 
            return True
        if event == "alarm_action":
            return True 
        return False
    
    def act(self, event): 
        if self.condition_to_act(event):
            if event == "button_press_action":
                self.buttonClickIncrement()
            if event == "alarm_action":
                self.buttonClickIncrement()

            if self.verbose: 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return

    def buttonClickIncrement(self):
            number = int(self.entity_state.string)
            addOne = number + 1
            convertToString = str(addOne)
            self.entity_state.string = convertToString
    
