class Counter:
    def __init__(self, number, name = "basic_counter_entity"):
        self.actions = []
        self.number = number
        self.color = (0, 255, 50)
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return



    