import pygame

class GameLoop():
    def __init__(self, name="Game Loop"):
        self.loop_content = []
        self.event_content = []
        self.display_content = []
        self.counter = 0
        self.name = name
        self.verbose = False
        self.active = True
        return

    
    def insertAction(self, a):
        if "event" in a.types:
            self.event_content.append(a)
            if self.verbose:
                print("/t" + self.name + " added " + a.name + " event action ")
        elif "loop" in a.types:
            self.loop_content.append(a)
            if self.verbose:
                print("/t" + self.name + " added " + a.name + " loop action ")
        elif "display" in a.types:
            self.display_content.append(a)
            if self.verbose:
                print("/t" + self.name + " added " + a.name + " display action ")
        
    def insertEntity(self, e):
        if self.verbose:
            print("inserting entity " + e.name)
        for a in e.actions:
            self.insertAction(a)
        return   
    
    def loop(self):
        #infinte loop
        while self.active:
            #look in events first
            events = pygame.event.get()
            for e in events:
                for a in self.event_content:
                    a.act(e)
            for a in self.loop_content:
                a.act(None)
            for a in self.display_content:
                a.act(None)
            #TroubleShooting
            if self.verbose:
                self.counter = self.counter + 1
                print(self.name + " counter " + str(self.counter))
        return
           

    
        
                
            
           
        