class HeadsUpDisplay:
    def __init__(self, x, y, string, name = "hud_entity"):
        self.actions = []
        self.location = [x, y]
        self.string = string
        self.color = (0, 255, 50)
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return
